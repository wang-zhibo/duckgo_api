#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Author: zhibo.wang
# E-mail: gm.zhibo.wang@gmail.com
# Date  :
# Desc  :

import json
import time
import random
import asyncio

from fastapi import APIRouter, Request, responses, status, File, UploadFile, \
    Header, HTTPException

from my_logger import MyLogger as Logger

from itertools import islice
from duckduckgo_search import AsyncDDGS
from pydantic import BaseModel, Field
from config import CID_LIST



logger = Logger("blueprint_v1_log")

blueprint_v1 = APIRouter()


@blueprint_v1.on_event("startup")
async def startup_event():
    # global motor_base
    # motor_base = MotorBase()
    # global redis_session
    # redis_session = RedisSession()
    pass

@blueprint_v1.on_event("shutdown")
async def shutdown_event():
    # motor_base = None
    # redis_session = None
    pass



@blueprint_v1.get("/test")
async def index():
    res = {"test": 1}
    return responses.JSONResponse(content=res)



class DdgoFields(BaseModel):
    q: str          = Field(..., description="搜索关键词")
    max_results: int       = Field(..., description="返回数据数量")


async def clean_k_max(item):
    max_results = 3
    q = item.q
    try:
        max_results = item.max_results
    except:
        pass
    return q, max_results


async def is_valid_ddgo_cid(cid: str) -> bool:
    return True if cid in CID_LIST else False


#### ddgo_search ####

@blueprint_v1.post("/ddgo/search", tags=['ddgo'], description='ddgo_search', summary='ddgo_search')
async def ddgo_search(item: DdgoFields):
    end_res = []
    try:
        q, max_results = await clean_k_max(item)
        ddgs_gen = await AsyncDDGS().text(q, safesearch='Off', timelimit='y', backend="lite")
        results = [r for r in islice(ddgs_gen, max_results)]
        end_res = results
    except Exception as e:
        logger.error(f"ddgo_search error: {e}")
    return end_res


@blueprint_v1.get("/ddgo/search", tags=['ddgo'], description='ddgo_search', summary='ddgo_search')
async def ddgo_search(q: str, max_results: int=3):
    end_res = []
    try:
        ddgs_gen = await AsyncDDGS().text(q, safesearch='Off', timelimit='y', backend="lite")
        results = [r for r in islice(ddgs_gen, max_results)]
        end_res = results
    except Exception as e:
        logger.error(f"ddgo_search error: {e}")
    return end_res


#### ddgo_search ####


#### ddgo_answers ####

@blueprint_v1.post("/ddgo/search/answers", tags=['ddgo'], description='ddgo_answers', summary='ddgo_answers')
async def search_answers(item: DdgoFields):
    end_res = []
    try:
        q, max_results = await clean_k_max(item)
        ddgs_gen = await AsyncDDGS().answers(q)
        results = [r for r in islice(ddgs_gen, max_results)]
        end_res = results
    except Exception as e:
        logger.error(f"ddgo search answers error: {e}")
    return end_res


@blueprint_v1.get("/ddgo/search/answers", tags=['ddgo'], description='ddgo_answers', summary='ddgo_answers')
async def search_answers(q: str, max_results: int=3):
    end_res = []
    try:
        ddgs_gen = await AsyncDDGS().answers(q)
        results = [r for r in islice(ddgs_gen, max_results)]
        end_res = results
    except Exception as e:
        logger.error(f"ddgo search answers error: {e}")
    return end_res


#### ddgo_answers ####



#### ddgo_images ####


@blueprint_v1.post("/ddgo/search/images", tags=['ddgo'], description='ddgo_images', summary='ddgo_images')
async def search_images(item: DdgoFields):
    end_res = []
    try:
        q, max_results = await clean_k_max(item)
        ddgs_gen = await AsyncDDGS().images(q, safesearch='Off', timelimit=None)
        results = [r for r in islice(ddgs_gen, max_results)]
        end_res = results
    except Exception as e:
        logger.error(f"ddgo search images error: {e}")
    return end_res


@blueprint_v1.get("/ddgo/search/images", tags=['ddgo'], description='ddgo_images', summary='ddgo_images')
async def search_images(q: str, max_results: int=3):
    end_res = []
    try:
        ddgs_gen = await AsyncDDGS().images(q, safesearch='Off', timelimit=None)
        results = [r for r in islice(ddgs_gen, max_results)]
        end_res = results
    except Exception as e:
        logger.error(f"ddgo search images error: {e}")
    return end_res

#### ddgo_images ####


#### ddgo_videos ####

@blueprint_v1.post("/ddgo/search/videos", tags=['ddgo'], description='ddgo_videos', summary='ddgo_videos')
async def search_videos(item: DdgoFields):
    end_res = []
    try:
        q, max_results = await clean_k_max(item)
        ddgs_gen = await AsyncDDGS().videos(q, safesearch='Off', timelimit=None, resolution="high")
        results = [r for r in islice(ddgs_gen, max_results)]
        end_res = results
    except Exception as e:
        logger.error(f"ddgo search videos error: {e}")
    return end_res


@blueprint_v1.get("/ddgo/search/videos", tags=['ddgo'], description='ddgo_videos', summary='ddgo_videos')
async def search_videos(q: str, max_results: int=3):
    end_res = []
    try:
        ddgs_gen = await AsyncDDGS().videos(q, safesearch='Off', timelimit=None, resolution="high")
        results = [r for r in islice(ddgs_gen, max_results)]
        end_res = results
    except Exception as e:
        logger.error(f"ddgo search videos error: {e}")
    return end_res

#### ddgo_videos ####



#### ddgo_news ####

@blueprint_v1.post("/ddgo/search/news", tags=['ddgo'], description='ddgo_news', summary='ddgo_news')
async def search_news(item: DdgoFields):
    end_res = []
    try:
        q, max_results = await clean_k_max(item)
        ddgs_gen = await AsyncDDGS().news(q, safesearch='Off', timelimit=None)
        results = [r for r in islice(ddgs_gen, max_results)]
        end_res = results
    except Exception as e:
        logger.error(f"ddgo search news error: {e}")
    return end_res


@blueprint_v1.get("/ddgo/search/news", tags=['ddgo'], description='ddgo_news', summary='ddgo_news')
async def search_news(q: str, max_results: int=3):
    end_res = []
    try:
        ddgs_gen = await AsyncDDGS().news(q, safesearch='Off', timelimit=None)
        results = [r for r in islice(ddgs_gen, max_results)]
        end_res = results
    except Exception as e:
        logger.error(f"ddgo search news error: {e}")
    return end_res

#### ddgo_news ####
