from threading import Thread, Lock as ThLock
import logging, logging.config
import time
import os
from random import randrange
import common_tools as ctools
import queue
from dicom_fix_issue_info import ProcessPerformance
from multiprocessing import Process, Lock
from multiprocessing import JoinableQueue, Queue, Manager
import json


MAX_NUMBER_OF_THREADS = os.cpu_count() + 1
MAX_EXEPTION_MESSAGE_LENGTH = 1024


class StudyThread(Thread):
    number_of_inst_processed: int = 1
    number_of_st_processed: int = 1
    number_of_all_studies: int = 1
    number_of_all_instances: int = 1
    thread_number = 1
    instance_counter_lock = ThLock()
    start_time = time.time()
    performance_history: list = []
    whole_performace = ProcessPerformance()
    
    @staticmethod
    def initialize_statics():
        StudyThread.number_of_inst_processed = 1
        StudyThread.number_of_st_processed = 1
        StudyThread.number_of_all_studies = 1
        StudyThread.number_of_all_instances = 1
        StudyThread.thread_number = 1
        StudyThread.start_time = time.time()
        StudyThread.performance_history = []
        StudyThread.whole_performace = ProcessPerformance()

    def __init__(self, queue: Queue, **kwarg):
        Thread.__init__(self, **kwarg)
        self._queue = queue

    def run(self): 
        logger = logging.getLogger(__name__)
        while True:
            (study_processor, args) = self._queue.get()
            logger.info('Start fixing study({}) out of {}'.format(
                StudyThread.number_of_st_processed,
                StudyThread.number_of_all_studies,))
            study_uids = []
            for elem in args[1]:
                study_uids.append(elem[0])
            try:
                perf = study_processor(*args)
                with StudyThread.instance_counter_lock:
                    StudyThread.performance_history.append(perf)
                    StudyThread.number_of_inst_processed +=\
                        perf.fix.size
                    StudyThread.whole_performace += perf
                    StudyThread.number_of_st_processed += len(args[1])
            except BaseException as err:
                perf = ProcessPerformance()
                logger.error(err, exc_info=True)
            progress = float(StudyThread.number_of_inst_processed) /\
                float(StudyThread.number_of_all_instances)
            time_point = time.time()
            time_elapsed = round(time_point - StudyThread.start_time)
            time_left = round(
                StudyThread.number_of_all_instances -
                StudyThread.number_of_inst_processed
                ) * time_elapsed / float(StudyThread.number_of_inst_processed)
            header = '{}/{})Study was fix/convert-ed successfully'.format(
                StudyThread.number_of_st_processed,
                StudyThread.number_of_all_studies)
            logger.info(header)
            for st in study_uids:
                logger.info('\t\t\t{}'.format(st))
            progress_string = ctools.ShowProgress(
                progress, time_elapsed, time_left, 60,
                '\t\tInstace progress', False)
            logger.info(progress_string)
            logger.info(
                'For this chunk of studies with <{}> threads {}'.format(
                    StudyThread.thread_number, str(perf))
            )
            logger.info(
                'For for all studies so far with <{}> threads {}'.format(
                    StudyThread.thread_number,
                    str(StudyThread.whole_performace)))
            self._queue.task_done()
    
    def run_serial(self): 
        logger = logging.getLogger(__name__)
        while True:
            (study_processor, args) = self._queue.get()
            logger.info('Start fixing study({}) out of {}'.format(
                StudyThread.number_of_st_processed,
                StudyThread.number_of_all_studies,))
            study_uids = []
            for elem in args[1]:
                study_uids.append(elem[0])
            try:
                perf = study_processor(*args)
                with StudyThread.instance_counter_lock:
                    StudyThread.performance_history.append(perf)
                    StudyThread.number_of_inst_processed +=\
                        perf.fix.size
                    StudyThread.whole_performace += perf
                    StudyThread.number_of_st_processed += len(args[1])
            except BaseException as err:
                perf = ProcessPerformance()
                logger.error(err, exc_info=True)
            progress = float(StudyThread.number_of_inst_processed) /\
                float(StudyThread.number_of_all_instances)
            time_point = time.time()
            time_elapsed = round(time_point - StudyThread.start_time)
            time_left = round(
                StudyThread.number_of_all_instances -
                StudyThread.number_of_inst_processed
                ) * time_elapsed / float(StudyThread.number_of_inst_processed)
            header = '{}/{})Study was fix/convert-ed successfully'.format(
                StudyThread.number_of_st_processed,
                StudyThread.number_of_all_studies)
            logger.info(header)
            for st in study_uids:
                logger.info('\t\t\t{}'.format(st))
            progress_string = ctools.ShowProgress(
                progress, time_elapsed, time_left, 60,
                '\t\tInstace progress', False)
            logger.info(progress_string)
            logger.info(
                'For this chunk of studies with <{}> threads {}'.format(
                    StudyThread.thread_number, str(perf))
            )
            logger.info(
                'For for all studies so far with <{}> threads {}'.format(
                    StudyThread.thread_number,
                    str(StudyThread.whole_performace)))
            self._queue.task_done()


class WorkerThread(Thread):

    def __init__(self, queue: queue.Queue, **kwarg):
        Thread.__init__(self, **kwarg)
        self.output = []
        self._queue = queue
        self._kill = False

    def run(self):
        logger = logging.getLogger(__name__)
        time_interval_for_log = 30 * 20
        tic = time.time() - randrange(0, time_interval_for_log)
        while not self._kill:
            toc = time.time()
            if (toc - tic) > time_interval_for_log:
                tic = toc
                logger.info(
                    "new task out of {} in queue".format(
                        self._queue.qsize()+1))
            (work_fun, args) = self._queue.get()
            if work_fun is None or args is None:
                continue
            try:
                out = work_fun(*args)
                self.output.append((args, out,))
            except BaseException as err:
                msg = str(err)
                if len(msg) > MAX_EXEPTION_MESSAGE_LENGTH:
                    msg = self.chop_message(MAX_EXEPTION_MESSAGE_LENGTH, msg)
                logger.error(msg, exc_info=True)
            self._queue.task_done()
    def kill(self):
        self._kill = True

    def chop_message(self, lnegth_in_chars: int, msg: str) -> str:
        h_l = lnegth_in_chars/2
        choped_msg = msg[:h_l] + '[.....]' + msg[-h_l:]
        return choped_msg


class ThreadPool:
    def __init__(self, max_number_of_threads: int,
                 thread_name_prifix: str = ''):
        self._queue = JoinableQueue()
        self._thread_pool = []
        self.output = []
        self._lock = ThLock()
        
        for i in range(max_number_of_threads):
            self._thread_pool.append(self._create_th(
                '{}{:02d}'.format(thread_name_prifix, i)
            ))

    def _create_th(self, th_name) -> WorkerThread:
        t = WorkerThread(self._queue, name=th_name)
        t.daemon = True
        t.start()
        return t

    @property
    def queue(self):
        return self._queue

    def kill_them_all(self):
        logger = self._sahred_data[logger]
        logger.debug('killing all threads')
        for t in self._thread_pool:
            t.kill()
        for t in self._thread_pool:
            # I'm putting none to push queue out of block
            self._queue.put((None, None))
        for t in self._thread_pool:
            t.join()
        logger.debug('collecting all output data from threads')
        for t in self._thread_pool:
            self.output.extend(t.output)  
        logger.debug('threads all finished')


class WorkerProcess(Process):

    def __init__(self, queue: JoinableQueue, res_queue: Queue,
                 log_config: dict, **kwarg):
        Process.__init__(self, **kwarg)
        self.output = res_queue
        self._queue = queue
        self._kill = False
        self._log_config = log_config

    def run(self):
        if self._log_config is not None:
            logging.config.dictConfig(self._log_config)
        logger = logging.getLogger(__name__)
        time_interval_for_log = 30 * 20
        tic = time.time() - randrange(0, time_interval_for_log)
        n = 0
        logger.info('Process started')
        while True:
            n += 1
            toc = time.time()
            if (toc - tic) > time_interval_for_log:
                tic = toc
                logger.info(
                    "new task out of {} in queue".format(
                        self._queue.qsize()+1))
            (work_fun, args) = self._queue.get()
            # print(work_fun)
            if work_fun is None or args is None:
                break
            try:
                out = work_fun(*args)
                # print('putting type {} into the queue'.format(type(out)))
                self.output.put((args, out,))
                # print('successful'.format(type(out)))
            except BaseException as err:
                msg = str(err)
                # print('Afshin ---- > {}'.format(msg))
                if len(msg) > MAX_EXEPTION_MESSAGE_LENGTH:
                    msg = self.chop_message(MAX_EXEPTION_MESSAGE_LENGTH, msg)
                logger.error(msg, exc_info=True)

            self._queue.task_done()

    def kill(self):
        self._kill = True

    def chop_message(self, lnegth_in_chars: int, msg: str) -> str:
        h_l = lnegth_in_chars/2
        choped_msg = msg[:h_l] + '[.....]' + msg[-h_l:]
        return choped_msg


class ProcessPool:
    def __init__(self, max_number_of_processs: int, logger_config: dict = None,
                 process_name_prifix: str = ''):
        self.logger = logging.getLogger(__name__)
        self._queue = JoinableQueue()
        self._res_queue = Queue()
        self._process_pool = []
        self.output = []
        if logger_config is None:
            self._logger_config = None
        else:
            self._logger_config = logger_config
        for i in range(max_number_of_processs):
            self._process_pool.append(self._create_pr(
                '{}{:02d}'.format(process_name_prifix, i)
            ))

    def _create_pr(self, th_name) -> WorkerProcess:
        t = WorkerProcess(
            self._queue, self._res_queue, self._logger_config, name=th_name)
        t.daemon = True
        t.start()
        return t

    @property
    def queue(self):
        return self._queue

    def kill_them_all(self):
        logger = logging.getLogger(__name__)
        logger.debug('killing all processs')
        print('killing all processs')
        for t in self._process_pool:
            # I'm putting none to push queue out of block
            self._queue.put((None, None))
        # for t in self._process_pool:
        #     t.join()
        logger.debug('collecting all output data from processs')
        self._res_queue.put(None)
        result = self._res_queue.get()
        while result is not None:
            self.output.append(result)
            result = self._res_queue.get() 
        logger.debug('processs all finished')
