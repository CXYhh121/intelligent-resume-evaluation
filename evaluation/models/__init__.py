# encoding: utf-8
"""
@author: chenxiyue
@contact: chenxiyue@126.com
@software: PyCharm
@file: __init__.py.py
@time: 2024/7/2 15:35
"""
from functools import wraps

from flask import current_app, Flask

from evaluation.config import DevConfig
from evaluation.models.dbs import mysql as db

class AppModel():
    APP_RUN_MODE = 'debug'


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevConfig)
    db.init_app(app)
    return app


app = create_app()


def sqlalchemy_context(app):
    def add_context(func):
        @wraps(func)
        def do_job(*args, **kwargs):
            if not current_app:
                app.app_context().push()
            result = func(*args, **kwargs)
            return result
        return do_job
    return add_context


def shutdown_session(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result, msg = func(*args, **kwargs)
        db.session.close()
        return result, msg
    return wrapper


def shutdown_session_single(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        db.session.close()
        return result
    return wrapper