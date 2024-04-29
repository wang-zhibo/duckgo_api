#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Author : zhibo.wang
# E-mail : gm.zhibo.wang@gmail.com
# Date   :
# Desc   :


import subprocess
from my_logger import MyLogger as Logger



def check_tag(tag):
    cmd = "ps -ef | grep python | grep -v grep | grep '{0}'".format(tag)
    status = subprocess.getoutput(cmd).split("\n")
    status = [i for i in status if i]
    c = False if len(status) > 0 else True
    return c


def run_cmd(cmd, path):
    status = True
    try:
        subprocess.check_call(cmd, shell=True, cwd=path)
    except Exception:
        status = False
    return status


def run():
    logger = Logger('check_server')
    check_list = [
        "duckgo_fastapi_server.py",
    ]
    for i in check_list:
        if check_tag(i):
            cmd = "python {0} &".format(i)
            run_cmd(cmd, None)
            logger.info("start {}".format(i))


if __name__ == "__main__":
    run()

