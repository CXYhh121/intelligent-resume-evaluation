# encoding: utf-8
"""
@author: chenxiyue
@contact: chenxiyue@kuaishou.com
@software: PyCharm
@file: resume_api.py
@time: 2024/7/4 19:32
"""
import logging

from flask import Blueprint, render_template, request

from evaluation.common.response import build_response
from evaluation.services.resume_service import analyzing_resume

resume = Blueprint('resume', __name__, url_prefix="/api/resume")

logger = logging.getLogger(__name__)


@resume.route('/abc')
def index():
	return render_template('index.html')


@resume.route('/upload', methods=['POST'])
def upload_resume():
	""" 上传简历接口 """
	resume_file = request.files.get('resume_file', None)
	if not resume_file:
		logger.error("请上传简历文件")
		return build_response(1, error_msg="请上传简历文件")
	# 调用接口解析简历，将解析后的数据存入数据库，并调用模型评价简历分数
	result = analyzing_resume(resume_file)
	# 返回简历id
	return build_response(0, data=result)


@resume.route('/evaluation/score', methods=['POST'])
def get_score():
	""" 给简历评分接口 """
	resume_id = request.form.get('resume_id', None)
	if not resume_id:
		logger.error("请传入简历id")
		return build_response(1, error_msg="请传入简历id")
	# 通过输入的简历id查询数据库中对应的数据信息，并调用模型计算分数
	result = evaluation_score_service(resume_id)