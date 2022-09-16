import functools
import logging


def result_or_err_msg(func):
    """装饰器：返回正常结果或错误信息"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
        except Exception as err:
            return str(err)
        else:
            return res

    return wrapper


def result_and_err_msg(func):
    """装饰器：返回正常结果及错误信息"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
        except Exception as err:
            return None, str(err)
        else:
            return res, None

    return wrapper


def result_or_err(func):
    """装饰器：返回正常结果或错误对象"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
        except Exception as err:
            return err
        else:
            return res

    return wrapper


def result_and_err(func):
    """装饰器：返回正常结果及错误对象"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
        except Exception as err:
            return None, err
        else:
            return res, None

    return wrapper


def singleton(cls):
    """类装饰器：单例模式"""
    _instance = {}

    def _singleton(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return _singleton


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.info('call %s():' % func.__name__)
        return func(*args, **kwargs)

    return wrapper


def retry(timeout: int = 10, limit: int = None, interval=0.5):
    def _retry_with_timeout(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as ex:
                pass


def on_exit(func):
    """注册推出时要执行的函数-支持多次注册"""
    import atexit
    atexit.register(func)
    return func


def timeout(func):
    """限制执行时间"""
    pass
