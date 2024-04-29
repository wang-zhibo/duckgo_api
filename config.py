#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Author: zhibo.wang
# E-mail: gm.zhibo.wang@gmail.com
# Date  :
# Desc  :

import os
import multiprocessing


HOST = "0.0.0.0"
PORT = 9400
# WORKER = False
WORKER = True


if WORKER:

    WORKER_NUM = 2
    RELOAD = False
else:
    WORKER_NUM = 1
    RELOAD = True


# 访问白名单  暂未开启
WHITE_LIST_IP = ["127.0.0.1"]

# 请求时 校验 cid 是否存在
CID_LIST = ["ddgo"]
