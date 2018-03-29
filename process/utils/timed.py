import functools
import logging
import inspect
import time

logger = logging.getLogger(__name__)


def timed(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        caller_frame = inspect.stack()[1]
        frame_info = inspect.getframeinfo(caller_frame[0])
        override = dict(function=fn.__name__, module=fn.__module__, lineno=frame_info.lineno)
        logger.info('starting function', extra=dict(override=override))
        t1 = time.time()
        result = fn(*args, **kwargs)
        t2 = time.time()
        logger.info('function halted', extra=dict(override=override, seconds='{:.3f}'.format(t2-t1)))
        return result
    return wrapper
