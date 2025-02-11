#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import asyncio
import aiofiles
import fnmatch
from pathlib import Path


async def find_pyc_files():
    """异步生成所有 .pyc 文件路径"""
    for root, _, filenames in os.walk(Path.cwd()):
        for pyc_file in fnmatch.filter(filenames, '*.pyc'):
            yield os.path.join(root, pyc_file)


async def delete_file(file_path):
    """异步删除单个文件"""
    try:
        async with aiofiles.open(file_path, mode="r"):  # 检查文件是否存在
            os.remove(file_path)
            print(f"已删除: {file_path}")
            return 1
    except (OSError, FileNotFoundError) as e:
        print(f"删除失败: {file_path}, 错误: {e}")
        return 0


async def delete_pyc_files():
    """主协程：并发删除所有 .pyc 文件"""
    pyc_files_deleted = 0

    # 批量任务收集
    delete_tasks = [delete_file(file_path) async for file_path in find_pyc_files()]

    if delete_tasks:
        results = await asyncio.gather(*delete_tasks)
        pyc_files_deleted = sum(results)

    print(f"共删除 {pyc_files_deleted} 个 .pyc 文件" if pyc_files_deleted else "未找到 .pyc 文件")


if __name__ == "__main__":
    asyncio.run(delete_pyc_files())

