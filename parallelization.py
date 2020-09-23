from threading import Thread, Lock
import logging
import time
import os
from random import randrange
import common_tools as ctools
from queue import Queue
from dicom_fix_issue_info import ProcessPerformance

MAX_NUMBER_OF_THREADS = os.cpu_count() + 1
MAX_EXEPTION_MESSAGE_LENGTH = 1024


class StudyThread(Thread):
    number_of_inst_processed: int = 1
    number_of_st_processed: int = 1
    number_of_all_studies: int = 1
    number_of_all_instances: int = 1
    instance_counter_lock = Lock()
    start_time = time.time()
    performance_history: list = []
    whole_performace = ProcessPerformance()

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
            header = '{}/{})Study {} was fix/convert-ed successfully'.format(
                StudyThread.number_of_st_processed,
                StudyThread.number_of_all_studies, study_uids)
            progress_string = ctools.ShowProgress(
                progress, time_elapsed, time_left, 60, header, False)
            logger.info(progress_string)
            logger.info('For this chunk of studies {}'.format(str(perf)))
            logger.info('For for all studies {}'.format(str(
                StudyThread.whole_performace)))
            self._queue.task_done()


class WorkerThread(Thread):

    def __init__(self, queue: Queue, **kwarg):
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
        self._queue = Queue()
        self._thread_pool = []
        self.output = []
        self._lock = Lock()
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
        logger = logging.getLogger(__name__)
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