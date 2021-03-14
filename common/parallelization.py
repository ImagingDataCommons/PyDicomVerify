import gc
import inspect
import logging
import multiprocessing
import os
import queue
import sys
import threading
import time
import traceback
from datetime import timedelta
import common.common_tools as ctools
from dicom_fix_issue_info import (
    # CLASSES
    ProcessPerformance,
)
from multiprocessing import (
    # SUBMODULES
    JoinableQueue,
    Process,
    Queue,
    cpu_count,
    Lock,
)
from random import (
    # VARIABLES
    randrange,
)
from threading import Thread
from threading import Lock as ThLock


MAX_NUMBER_OF_THREADS = os.cpu_count() + 1
MAX_EXEPTION_MESSAGE_LENGTH = 1024

class Periodic:

    def __init__(self, f, args: list, period_in_sec: int):
        self._kill_timer: bool = False
        self._function = f
        self._args = args
        self.period_in_sec = period_in_sec

    def start(self):
        if self._args is None:
            self._function()
        else:
            self._function(self._args)
        if not self._kill_timer:
            threading.Timer(self.period_in_sec, self.start).start()

    def kill_timer(self):
        self._kill_timer = True


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
                gc.collect()
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

    def __init__(self, queue: JoinableQueue, res_queue: Queue, lock: Lock,
                 status_log_interval: int,
                 **kwarg):
        Process.__init__(self, **kwarg)
        self.output = res_queue
        self._queue = queue
        self._kill = False
        self._lock = lock
        self.start_time = time.time()
        self.time_interval = status_log_interval
        self.current_loop_start_time = time.time()
        self.last_log_time = time.time() - \
            randrange(0, self.time_interval)
        self.kill_status_thread = False
        self.task_timeout = 60 * 30
        self.current_task = (None, None)
        self.task_timeout_last_log_time = time.time()

    def run(self):
        logger = logging.getLogger(__name__)
        self.kill_status_thread = False
        t = threading.Thread(target=self.log_status)
        t.start()
        n = 0
        while True:
            self.current_loop_start_time = time.time()
            n += 1
            # toc = time.time()
            # if (toc - tic) > time_interval_for_log:
            #     tic = toc
            #     logger.info(
            #         "new task out of {} in queue".format(
            #             self._queue.qsize()+1))
            # with self._lock:
                # if qsz < 2000 and qsz > 0:
                #     logger.info(
                #         "before task out of {} in queue".format(qsz))
            self.current_task = self._queue.get()
            (work_fun, args) = self.current_task
            
            # if sys.platform == "linux" or sys.platform == "linux2" or\
            #         sys.platform == "win32":
            #     qsz = self._queue.qsize()
            #     # with self._lock:
            #     if qsz % 1000 == 0 and qsz > 0:
            #         logger.info(
            #             "picked a task ({}) out of {} "
            #             "remaining in queue".format(
            #                 work_fun.__name__, qsz))
            # else:
            #     qsz = None
            if work_fun is None or args is None:
                self._queue.task_done()
                break
            try:
                out = work_fun(*args)
                self.output.put((args, out,))
            except BaseException as err:
                arg_labels = inspect.getfullargspec(work_fun)
                msg = str(err)
                if len(msg) > MAX_EXEPTION_MESSAGE_LENGTH:
                    msg = self.chop_message(MAX_EXEPTION_MESSAGE_LENGTH, msg)
                msg += '\n\t -> Function {} list of arguments:'.format(
                    work_fun.__name__)
                for arg_l, arg in zip(arg_labels[0], args):
                    if isinstance(arg, tuple) or isinstance(arg, list):
                        if len(arg) > 0:
                            arg = arg[0]
                    if isinstance(arg, str):
                        msg += ('\n\t\t\t{} = "{}"'.format(arg_l, arg))
                    else:
                        msg += ('\n\t\t\t{} = {}'.format(arg_l, arg))
                logger.error(msg, exc_info=True)
            finally:
                self._queue.task_done()
        # logging.getLogger().setLevel(logging.INFO)
        self.kill_status_thread = True
        t.join(10)
        self.output.close()  # will stop the thread running the queeu anf flush
        self.output.join_thread()
        logger.debug('returning from the run')
        return

    def kill(self):
        self._kill = True

    def chop_message(self, lnegth_in_chars: int, msg: str) -> str:
        h_l = lnegth_in_chars/2
        choped_msg = msg[:h_l] + '[.....]' + msg[-h_l:]
        return choped_msg
    
    def log_status(self):
        logger = logging.getLogger(__name__)
        while not self.kill_status_thread:
            toc = time.time()
            log_elapsed_time = toc - self.last_log_time
            timeout_log_elapsed_time = toc - self.task_timeout_last_log_time
            el_time = toc - self.current_loop_start_time
            el_time_total = toc - self.start_time
            if log_elapsed_time > self.time_interval:
                if sys.platform == "linux" or sys.platform == "linux2" or\
                        sys.platform == "win32":
                    qsz = self._queue.qsize()
                else:
                    qsz = None
                logger.info(
                    "Time since the creation of process :{}, time since"
                    " the start of the current task {}, "
                    "number of tasks left {}".format(
                        timedelta(seconds=el_time_total),
                        timedelta(seconds=el_time),
                        qsz))
                self.last_log_time = time.time()
            if self.task_timeout < el_time and\
                    self.task_timeout < timeout_log_elapsed_time:
                self.task_timeout_last_log_time = time.time()
                (work_fun, args) = self.current_task
                if work_fun is None:
                    continue
                arg_labels = inspect.getfullargspec(work_fun)
                msg = 'TIMEOUT this task has taken {} so far: '\
                    '\n\t -> Function {} list of arguments:'.format(
                        timedelta(seconds=el_time),
                        work_fun.__name__)
                for arg_l, arg in zip(arg_labels[0], args):
                    if isinstance(arg, tuple) or isinstance(arg, list):
                        if len(arg) > 0:
                            arg = arg[0]
                    if isinstance(arg, str):
                        msg += ('\n\t\t\t{} = "{}"'.format(arg_l, arg))
                    else:
                        msg += ('\n\t\t\t{} = {}'.format(arg_l, arg))
                logger.error(msg, exc_info=True)

            time.sleep(5)



class ProcessPool:
    def __init__(self, max_number_of_processs: int,
                 process_name_prifix: str = ''):
        self.logger = logging.getLogger(__name__)
        self._queue = JoinableQueue()
        self._res_queue = Queue()
        self._process_pool = []
        self.output = []
        self._lock = Lock()
        self._processes_count = max_number_of_processs
        for i in range(max_number_of_processs):
            self._process_pool.append(self._create_pr(
                '{}{:02d}'.format(process_name_prifix, i)
            ))

    def _create_pr(self, th_name) -> WorkerProcess:
        t = WorkerProcess(
            self._queue, self._res_queue, self._lock, name=th_name,
            status_log_interval=self._processes_count * 20)
        t.daemon = True
        t.start()
        return t

    @property
    def queue(self):
        return self._queue

    def kill_them_all(self, timeout=5):
        logger = logging.getLogger(__name__)
        logger.debug('closing all processs')
        for t in self._process_pool:
            # I'm putting none to push queue out of block
            self._queue.put((None, None))        
        logger.debug('collecting all output data from processs')
        self._res_queue.put(None)
        if sys.platform == "linux" or sys.platform == "linux2" or\
                    sys.platform == "win32":
                output_count = self._res_queue.qsize()
        else:
            output_count = None
        
        # result = self._res_queue.get()
        collected = 0
        number_of_none_outputs = 0
        none_indeces = []
        while True:
            try:
                result = self._res_queue.get(timeout)
                collected += 1
            except queue.Empty:
                if output_count is not None:
                    if collected < output_count:
                        continue
                    else:
                        break
                else:
                    break
            if result is None:
                number_of_none_outputs += 1
                none_indeces.append(collected - 1)
            else:
                self.output.append(result)
        logger.info(
            'from all {} ouputs {} were collected {} '
            'of them were None. None indeces: {}'.format(
                output_count, len(self.output),
                number_of_none_outputs, none_indeces)
            )
        logger.debug('data were collected waiting for processses to join')
        for t in self._process_pool:
            t.join(timeout)
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

    def get_status(self) -> str:
        stat = ''
        input_qsz = self._queue.qsize()
        output_qsz = self._res_queue.qsize()
        stat += ("{} processes with inputs ({}) and outputs({})\n".format(
            len(self._process_pool), input_qsz, output_qsz))
        for ps in self._process_pool:
            name = ps.name
            st = 'alive' if ps.is_alive() else 'dead'
            stat += ('\t\tps {} is {}\n'.format(name, st))
        return stat


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
            except BaseException as err:
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