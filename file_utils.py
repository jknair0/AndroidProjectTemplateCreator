import os
from re import sub
from shutil import rmtree

def list_recursively(directory_path):
    if not exists(directory_path):
        return
    for root, _, files in os.walk(directory_path):
        for file in files:
            yield os.path.join(root, file)


def delete_recursive(directory_path):
    if not exists(directory_path):
        return
    rmtree(directory_path)

def join_path(rootPath, subPath):
    if not subPath:
        return rootPath
    if subPath[0] == '/' or subPath[1] == '\\':
        subPath = subPath[1:]
    return os.path.join(rootPath, subPath)

def exists(path):
    return os.path.exists(path)

def rename(fromFileOrDir, toFileOrDir):
    if not exists(fromFileOrDir):
        return
    os.rename(fromFileOrDir, toFileOrDir)