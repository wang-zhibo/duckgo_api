#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import concurrent.futures
import fnmatch


def find_pyc_files():
    """生成器：查找所有 .pyc 文件路径"""
    for root, _, filenames in os.walk(os.getcwd()):
        for pyc_file in fnmatch.filter(filenames, '*.pyc'):
            yield os.path.join(root, pyc_file)


def delete_file(file_path):
    """删除单个文件"""
    try:
        os.remove(file_path)
        print(f"已删除: {file_path}")
        return 1
    except OSError as e:
        print(f"删除失败: {file_path}, 错误: {e}")
        return 0


def delete_pyc_files():
    """多线程删除 .pyc 文件"""
    total_deleted = 0

    # 使用线程池进行并发删除
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # 并行执行删除任务并统计删除的数量
        results = executor.map(delete_file, find_pyc_files())
        total_deleted = sum(results)

    print(f"共删除 {total_deleted} 个 .pyc 文件" if total_deleted else "未找到 .pyc 文件")


if __name__ == "__main__":
    delete_pyc_files()

