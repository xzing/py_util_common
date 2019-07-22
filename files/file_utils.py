#!/usr/bin/python3
# -*- coding:utf-8 -*-


import os


def overwrite_to(s_file_path, s_content):
    if os.path.exists(s_file_path):
        os.remove(s_file_path)
    produ_f = open(s_file_path, "a")
    produ_f.write(f"{s_content}\n")
    produ_f.close()


def remove_file(s_file_path):
    if os.path.exists(s_file_path):
        os.remove(s_file_path)
    else:
        print(f"{s_file_path} file not exist")


def append_to_new_line(s_file_path, s_content):
    if os.path.exists(s_file_path):
        produ_f = open(s_file_path, "a+")
        produ_f.write(f"\n{s_content}\n")
        produ_f.close()
    else:
        raise IOError(f"{s_file_path} file not exist")


def append_to(s_file_path, s_content):
    if os.path.exists(s_file_path):
        produ_f = open(s_file_path, "a+")
        produ_f.write(s_content)
        produ_f.close()
    else:
        raise IOError(f"{s_file_path} file not exist")
