# encoding: utf-8
"""
@author: chenxiyue
@contact: chenxiyue@kuaishou.com
@software: PyCharm
@file: resume_api.py
@time: 2024/7/4 19:32
"""
import logging

from flask import Blueprint, render_template

resume = Blueprint('resume', __name__, url_prefix="/api/resume")

logger = logging.getLogger(__name__)


@resume.route('/abc')
def index():
    return render_template('index.html')


@resume.route('/upload', methods=['POST'])
def upload_resume():
    """ 上传简历接口 """

