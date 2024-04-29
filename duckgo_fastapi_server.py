#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Author: zhibo.wang
# E-mail: gm.zhibo.wang@gmail.com
# Date  :
# Desc  :


import os
import arrow
import time
import pytz
import datetime
import asyncio
import uvicorn
from fastapi import FastAPI

from blueprints import blueprint_v1

from config import HOST, PORT, WORKER_NUM, RELOAD, WORKER


description = """
_________________
### 项目说明：
    docugo search

### xx
    x
_________________
"""


app = FastAPI(
    docs_url="/docs",
    redoc_url="/redoc",
    title='docugo search接口文档',
    description=description,
    version="0.0.1",
)


app.include_router(blueprint_v1, prefix="/api/v1")


timezone = pytz.timezone("Asia/Shanghai")


@app.middleware("http")
async def set_timezone(request, call_next):
    client_timezone = "Asia/Shanghai"

    if client_timezone:
        arrow.now(tz=client_timezone).format('YYYY-MM-DD HH:mm:ss')

    response = await call_next(request)
    response.headers["date"] = arrow.now().format('YYYY-MM-DD HH:mm:ss')

    return response



if __name__ == '__main__':
    name_app = os.path.splitext(os.path.basename(__file__))[0]
    """
    if WORKER is False:
        import socket, webbrowser
        host_name = socket.gethostname()
        ip_address = socket.gethostbyname(host_name)
        if ip_address is None:
            ip_address = "127.0.0.1"
        webbrowser.open(f"http://{ip_address}:{PORT}/docs")
        webbrowser.open(f"http://{ip_address}:{PORT}/redoc")
    """
    uvicorn.run(
        app=f"{name_app}:app",
        host=HOST,
        port=PORT,
        workers=WORKER_NUM,
        reload=RELOAD,
        headers=[
            ("server", "")
        ]
    )

