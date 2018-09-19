# -*- coding: utf-8 -*-
import logging


# def log():
#     logger = logging.getLogger('testlog')
#
#     #  这里进行判断，如果logger.handlers列表为空，则添加，否则，直接去写日志
#     if not logger.handlers:
#         streamhandler = logging.StreamHandler()
#         streamhandler.setLevel(logging.ERROR)
#         formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
#         streamhandler.setFormatter(formatter)
#         logger.addHandler(streamhandler)
#
#     logger.error(msg)
#
#
# if __name__ == '__main__':
#     log('hi')
#     log('hi too')
#     log('hi three')

#
# import logging
#
#
#
#
#
# ch = logging.StreamHandler()
# ch.setLevel(logging.INFO)
#
# fh = logging.FileHandler('mysql.log')
# #fh.setLevel(logging.WARNING)
#
#
# #formatter
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# #bind formatter to ch
# ch.setFormatter(formatter)
# fh.setFormatter(formatter)
#
# logger = logging.getLogger("Mysql")
# logger.setLevel(logging.DEBUG) #logger 优先级高于其它输出途径的
#
#
# #add handler   to logger instance
# logger.addHandler(ch)
# logger.addHandler(fh)
#
#
#
#
#
# logger.debug("test ....")
# logger.info("test info ....")
# logger.warning("start to run db backup job ....")
# logger.error("test error ....")

import logging

# 为日志函数添加一个name，每次调用时传入不同的日志名
# def my_log():
#     logger = logging.getLogger()
#     logger.handlers.clear()
#
#     ch = logging.StreamHandler()
#     ch.setLevel(logging.ERROR)
#     fmt = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#     ch.setFormatter(fmt)
#
#     logger.addHandler(ch)
#
#     return logger
#
#
# my_log().error('run one')
# my_log().error('run two')
# my_log().error('run three')
import logging


def my_log():
    logger = logging.getLogger('mysql.log')
    # 判断logger是否已经添加过handler，是则直接返回logger对象，否则执行handler设定以及addHandler(ch)
    if not logger.handlers:
        ch = logging.StreamHandler()
        ch.setLevel(logging.ERROR)
        fmt = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(fmt)

        logger.addHandler(ch)

    return logger


my_log().error('run one')
my_log().error('run two')
my_log().error('run three')