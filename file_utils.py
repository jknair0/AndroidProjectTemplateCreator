import os
from shutil import rmtree
from tabnanny import verbose

from isort import file
from log_utils import log

def list_recursively(directory_path):
    if not exists(directory_path):
        return
    for root, _, files in os.walk(directory_path):
        for file in files:
            yield os.path.join(root, file)


def delete_recursive(directory_path, verbose = True):
    if not exists(directory_path):
        log("delete failed for {}".format(directory_path))
        return
    if verbose:
        log("deleting {}".format(directory_path))
    rmtree(directory_path)

def delete(file_name, verbose=True):
    if not exists(file_name):
        log("delete failed for {}".format(file_name))
        return
    if verbose:
        log("deleting {}".format(file_name))
    os.remove(file_name)

def join_path(rootPath, subPath):
    if not subPath:
        return rootPath
    if subPath[0] == '/' or subPath[1] == '\\':
        subPath = subPath[1:]
    return os.path.join(rootPath, subPath)

def exists(path):
    return os.path.exists(path)

def rename(fromFileOrDir, toFileOrDir, verbose = True):
    if not exists(fromFileOrDir):
        log("rename failed: {} to {}".format(fromFileOrDir, toFileOrDir))
        return
    if verbose:
        log("renaming {} to {}".format(fromFileOrDir, toFileOrDir))
    os.rename(fromFileOrDir, toFileOrDir)