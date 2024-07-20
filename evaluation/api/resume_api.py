# encoding: utf-8
"""
@author: chenxiyue
@contact: chenxiyue@126.com
@software: PyCharm
@file: resume_api.py
@time: 2024/7/4 19:32
"""
import logging

from flask import Blueprint, render_template, request

from evaluation.common.response import build_response
from evaluation.services.resume_service import analyzing_resume, evaluation_score_excel_service, \
    evaluation_score_json_service

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


@resume.route('/evaluation/score/excel', methods=['POST'])
def evaluation_score_excel():
    """ 量化数据简历评分接口 """
    excel_file = request.files.get('excel_file', None)
    if not excel_file:
        logger.error("请上传excel文件")
        return build_response(1, error_msg="请上传excel文件")
    # 调用接口解析excel，将解析后的数据存入数据库，并调用模型计算分数
    result = evaluation_score_excel_service(excel_file)
    return build_response(0, data=result)
    # 返回简历id


@resume.route('/evaluation/score/json', methods=['POST'])
def get_score():
    """ 给简历评分接口 """
    resume_json = request.get_json()
    if not resume_json:
        logger.error("请传入简历数据")
        return build_response(1, error_msg="请传入简历数据")
    # 通过输入的简历id查询数据库中对应的数据信息，并调用模型计算分数
    result = evaluation_score_json_service(resume_json)
    return build_response(0, data=result)
