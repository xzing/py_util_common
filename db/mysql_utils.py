#!/usr/bin/python3
# -*- coding:utf-8 -*-


# pip3 install mysql-connector
import mysql.connector


def connect_db():
    print("链接数据库 >>>")
    return mysql.connector.connect(
        host=host,
        port=port,
        user=user,
        passwd=pass_code,
        database=database
    )


if __name__ == '__main__':
    host = ""
    port = ""
    user = ""
    pass_code = ""
    database = ""
