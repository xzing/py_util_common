#!/usr/bin/python3
# -*- coding:utf-8 -*-


# 去除字符串首尾空白
def trim_str(s):
    if isinstance(s, str):
        return s.strip()
    else:
        return ''
