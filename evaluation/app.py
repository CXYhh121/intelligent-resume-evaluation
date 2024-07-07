# encoding: utf-8
"""
@author: chenxiyue
@contact: chenxiyue@kuaishou.com
@software: PyCharm
@file: app.py
@time: 2024/7/2 15:36
"""
import traceback

from flask import Flask, current_app, session
from flask_cas import CAS

from evaluation.api.resume_api import resume
from evaluation.models.dbs import mysql as db
from evaluation.common.log_config import log_init
from evaluation.config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.config['SECRET_KEY'] = '123'

app.config['SQLALCHEMY_POOL_RECYCLE'] = 120
app.config['SQLALCHEMY_POOL_SIZE'] = 300
app.config['SQLALCHEMY_MAX_OVERFLOW'] = 100
app.config['CORS_SUPPORTS_CREDENTIALS'] = True
db.init_app(app)


log_init()

cas = CAS(app, '/cas')
app.config['CAS_SERVER'] = 'https://sso.corp.kuaishou.com'
app.config['CAS_AFTER_LOGIN'] = '/'
app.config['CAS_VALIDATE_ROUTE'] = '/cas/p3/serviceValidate'


app.register_blueprint(resume)

@app.route("/health")
def health_check():
    return "ok"


@app.route("/status")
def status_check():
    return "ok"


@app.route("/init")
def init_check():
    return "ok"


@app.before_request
def before_action():
    if not current_app.config['ATTACH_JOB_AT_INTI']:
        session['CAS_USERNAME'] = 'chenxiyue'


@app.after_request
def after_action(res):
    try:
        db.session.close()
        db.session.rollback()
        db.session.commit()
    except Exception:
        traceback.format_exc()
    finally:
        return res