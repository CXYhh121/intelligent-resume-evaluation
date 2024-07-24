# encoding: utf-8
"""
@author: chenxiyue
@contact: chenxiyue@126.com
@software: PyCharm
@file: config.py
@time: 2024/7/2 15:37
"""


class Config(object):
    SQLALCHEMY_POOL_SIZE = 100
    SQLALCHEMY_POOL_RECYCLE = 60 * 3  # 自动回收连接的秒数
    ATTACH_JOB_AT_INTI = False  # 默认不启动aps
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://emas_48070_v1_rw:Kv1s6ASUwPVXoR80TkqZxrIh1GlvnEHf@cluster01.proxysql.staging.internal:6032/emas?charset=utf8"


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProdConfig(Config):
    DEBUG = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:XfWvEv2!@10.2.8.3:3306/mysql?charset=utf8"