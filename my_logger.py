#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Author: zhibo.wang
# E-mail: gm.zhibo.wang@gmail.com
# Date  :
# Desc  : pip install loguru



import os
from functools import wraps
from time import perf_counter

from loguru import logger



class MyLogger:
    """
    根据时间、文件大小切割日志
    """

    def __init__(self, file_name, log_dir='logs', max_size=10, retention='7 days'):
        # file_name 日志文件名称, log_dir 日志文件目录
        # retention 保留最新7天的log
        self.file_name = file_name
        self.log_dir = log_dir
        self.max_size = max_size
        self.retention = retention
        self.logger = self.configure_logger()

    def configure_logger(self):
        """

        Returns:

        """
        # 创建日志目录
        os.makedirs(self.log_dir, exist_ok=True)

        shared_config = {
            "level": "DEBUG",
            "enqueue": True,
            "backtrace": True,
            "format": "{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
        }

        # 添加按照日期和大小切割的文件 handler
        logger.add(
            sink=f"{self.log_dir}/{self.file_name}.log",
            rotation=f"{self.max_size} MB",
            retention=self.retention,
            compression="zip",
            encoding='utf-8',
            diagnose=True,
            colorize=True,
            **shared_config
        )

        # 配置按照等级划分的文件 handler 和控制台输出
        logger.add(sink=self.get_log_path, **shared_config)

        return logger

    def get_log_path(self, message: str) -> str:
        """
        根据等级返回日志路径
        Args:
            message:

        Returns:

        """
        log_level = message.record["level"].name.lower()
        log_file = f"{log_level}.log"
        log_path = os.path.join(self.log_dir, log_file)

        return log_path

    def __getattr__(self, level: str):
        return getattr(self.logger, level)

    def log_decorator(self, msg="快看, 异常了, 别唧唧哇哇, 快排查"):
        """
             日志装饰器，记录函数的名称、参数、返回值、运行时间和异常信息
        Args:
            logger: 日志记录器对象

        Returns:
            装饰器函数

        """

        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                self.logger.info(f'-----------分割线-----------')
                self.logger.info(f'调用 {func.__name__} args: {args}; kwargs:{kwargs}')
                start = perf_counter()  # 开始时间
                try:
                    result = func(*args, **kwargs)
                    end = perf_counter()  # 结束时间
                    duration = end - start
                    self.logger.info(f"{func.__name__} 返回结果：{result}, 耗时：{duration:4f}s")
                    return result
                except Exception as e:
                    self.logger.exception(f"{func.__name__}: {msg}")
                    self.logger.info(f"-----------分割线-----------")
                    # raise e

            return wrapper

        return decorator

    def log_decorator_async(self, msg="快看, 异常了, 别唧唧哇哇, 快排查"):
        """
             日志装饰器，记录函数的名称、参数、返回值、运行时间和异常信息
        Args:
            logger: 日志记录器对象

        Returns:
            装饰器函数

        """

        def decorator(func):
            @wraps(func)
            async def wrapper(*args, **kwargs):
                self.logger.info(f'-----------分割线-----------')
                self.logger.info(f'调用 {func.__name__} args: {args}; kwargs:{kwargs}')
                start = perf_counter()  # 开始时间
                try:
                    result = await func(*args, **kwargs)
                    end = perf_counter()  # 结束时间
                    duration = end - start
                    self.logger.info(f"{func.__name__} 返回结果：{result}, 耗时：{duration:4f}s")
                    return result
                except Exception as e:
                    self.logger.exception(f"{func.__name__}: {msg}")
                    self.logger.info(f"-----------分割线-----------")
                    # raise e

            return wrapper

        return decorator


"""
if __name__ == '__main__':
    log = MyLogger("test_log")


    @log.log_decorator("神马  出错了!!!")
    def test_zero_division_error(a, b):
        return a / b

    @log.log_decorator()
    def test_error():
        import json
        json.loads("asdasd")

    for i in range(1):
        log.error('错误信息')
        log.critical('严重错误信息')
        test_zero_division_error(1, 0)
        test_error()
        log.debug('调试信息')
        log.info('普通信息')
        log.success('成功信息')
        log.warning('警告信息')
"""
