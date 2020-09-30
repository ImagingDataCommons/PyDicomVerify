from __future__ import absolute_import, division, unicode_literals
from threading import Thread, Lock as ThLock
import logging, logging.config
import time
import os
from random import randrange
import common_tools as ctools
import queue
from dicom_fix_issue_info import ProcessPerformance
import multiprocessing
from multiprocessing import Process
from multiprocessing import JoinableQueue, Queue
import sys
import threading
import traceback


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
        time_interval_for_log = 30 * 20 * 10
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
                  **kwarg):
        Process.__init__(self, **kwarg)
        self.output = res_queue
        self._queue = queue
        self._kill = False

    def run(self):
        logger = logging.getLogger(__name__)
        # tic = time.time() - randrange(0, time_interval_for_log)
        n = 0
        while True:
            n += 1
            toc = time.time()
            # if (toc - tic) > time_interval_for_log:
            #     tic = toc
            #     logger.info(
            #         "new task out of {} in queue".format(
            #             self._queue.qsize()+1))
            (work_fun, args) = self._queue.get()
            if work_fun is None or args is None:
                break
            try:
                out = work_fun(*args)
                self.output.put((args, out,))
            except BaseException as err:
                msg = str(err)
                if len(msg) > MAX_EXEPTION_MESSAGE_LENGTH:
                    msg = self.chop_message(MAX_EXEPTION_MESSAGE_LENGTH, msg)
                logger.error(msg, exc_info=True)

            self._queue.task_done()
        logger.debug('returning from the run')
        return

    def kill(self):
        self._kill = True

    def chop_message(self, lnegth_in_chars: int, msg: str) -> str:
        h_l = lnegth_in_chars/2
        choped_msg = msg[:h_l] + '[.....]' + msg[-h_l:]
        return choped_msg


class ProcessPool:
    def __init__(self, max_number_of_processs: int,
                 process_name_prifix: str = ''):
        self.logger = logging.getLogger(__name__)
        self._queue = JoinableQueue()
        self._res_queue = Queue()
        self._process_pool = []
        self.output = []
        for i in range(max_number_of_processs):
            self._process_pool.append(self._create_pr(
                '{}{:02d}'.format(process_name_prifix, i)
            ))

    def _create_pr(self, th_name) -> WorkerProcess:
        t = WorkerProcess(
            self._queue, self._res_queue, name=th_name)
        # t.daemon = True
        t.start()
        return t

    @property
    def queue(self):
        return self._queue

    def kill_them_all(self):
        logger = logging.getLogger(__name__)
        logger.debug('closing all processs')
        for t in self._process_pool:
            # I'm putting none to push queue out of block
            self._queue.put((None, None))
        logger.debug('collecting all output data from processs')
        self._res_queue.put(None)
        result = self._res_queue.get()
        while result is not None:
            self.output.append(result)
            result = self._res_queue.get()
        logger.debug('data were collected waiting for processses to join')
        for t in self._process_pool:
            t.join()
        logger.debug('Processses joined successfully -  now closing them all')
        for t in self._process_pool:
            try:
                t.close()
            except ValueError as err:
                logger.error(err, exc_info=True)
                logger.info(
                    'Closing the process was not seuccessful.'
                    ' I will terminate it')
                t.terminate()
        logger.debug('processs all closed')


class MultiProcessingHandler(logging.Handler):

    def __init__(self, name, sub_handler=None):
        super(MultiProcessingHandler, self).__init__()

        if sub_handler is None:
            sub_handler = logging.StreamHandler()
        self.sub_handler = sub_handler

        self.setLevel(self.sub_handler.level)
        self.setFormatter(self.sub_handler.formatter)
        self.filters = self.sub_handler.filters

        self.queue = multiprocessing.Queue(-1)
        self._is_closed = False
        # The thread handles receiving records asynchronously.
        self._receive_thread = threading.Thread(target=self._receive, name=name)
        self._receive_thread.daemon = True
        self._receive_thread.start()

    def setFormatter(self, fmt):
        super(MultiProcessingHandler, self).setFormatter(fmt)
        self.sub_handler.setFormatter(fmt)

    def _receive(self):
        while True:
            try:
                if self._is_closed and self.queue.empty():
                    break

                record = self.queue.get(timeout=0.2)
                self.sub_handler.emit(record)
            except (KeyboardInterrupt, SystemExit):
                raise
            except (BrokenPipeError, EOFError):
                break
            except queue.Empty:
                pass  # This periodically checks if the logger is closed.
            except:
                traceback.print_exc(file=sys.stderr)

        self.queue.close()
        self.queue.join_thread()

    def _send(self, s):
        self.queue.put_nowait(s)

    def _format_record(self, record):
        # ensure that exc_info and args
        # have been stringified. Removes any chance of
        # unpickleable things inside and possibly reduces
        # message size sent over the pipe.
        if record.args:
            record.msg = record.msg % record.args
            record.args = None
        if record.exc_info:
            self.format(record)
            record.exc_info = None

        return record

    def emit(self, record):
        try:
            s = self._format_record(record)
            self._send(s)
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)

    def close(self):
        if not self._is_closed:
            self._is_closed = True
            self._receive_thread.join(5.0)  # Waits for receive queue to empty.

            self.sub_handler.close()
            super(MultiProcessingHandler, self).close()


def install_mp_handler(logger=None):
    """Wraps the handlers in the given Logger with an MultiProcessingHandler.
    :param logger: whose handlers to wrap. By default, the root logger.
    """
    if logger is None:
        logger = logging.getLogger()

    for i, orig_handler in enumerate(list(logger.handlers)):
        handler = MultiProcessingHandler(
            'mp-handler-{0}'.format(i), sub_handler=orig_handler)

        logger.removeHandler(orig_handler)
        logger.addHandler(handler)


def uninstall_mp_handler(logger=None):
    """Unwraps the handlers in the given Logger from a MultiProcessingHandler wrapper
    :param logger: whose handlers to unwrap. By defaul, the root logger.
    """
    if logger is None:
        logger = logging.getLogger()

    for handler in logger.handlers:
        if isinstance(handler, MultiProcessingHandler):
            orig_handler = handler.sub_handler
            logger.removeHandler(handler)
            logger.addHandler(orig_handler)