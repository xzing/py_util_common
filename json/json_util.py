#!/usr/bin/python3
# -*- coding:utf-8 -*-


import json


def load_json_file(file_name):
    with open(file_name) as json_file:
        return json.load(json_file)
