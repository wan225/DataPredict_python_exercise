# -*- coding: utf-8 -*-
# @Time  : 2021/2/24 5:30 PM
# @Author : wan

# 数据库配置
HOST = 'localhost'
PORT = '3306'
DATABASE = 'test'    # 数据库名
USERNAME = 'root'       # 用户名
PASSWORD = ''           # 密码

DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,
                                                                                        password=PASSWORD, host=HOST,
                                                                                        port=PORT, db=DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True
