# encoding: utf-8
"""
@author: chenxiyue
@contact: chenxiyue@kuaishou.com
@software: PyCharm
@file: model.py
@time: 2024/7/2 15:53
"""
import datetime

from evaluation.models.dbs import mysql as db


class Recruitment(db.Model):
    __tablename__ = 'Recruitment'
    id = db.Column(db.BigInteger(), nullable=False, primary_key=True)
    job_name = db.Column(db.String(64), nullable=False, comment='岗位名称')
    job_number = db.Column(db.BigInteger(), comment='岗位编号')
    require_person = db.Column(db.BigInteger(), comment='招聘人数')
    require_edu = db.Column(db.String(64), comment='学历要求')
    require_age = db.Column(db.BigInteger(), comment='年龄要求')
    job_grade = db.Column(db.String(128), comment='岗位级别')
    applicant_first_level = db.Column(db.String(128), comment='应聘者一级学科')
    job_level = db.Column(db.String(128), comment='岗位学科方向')
    qualification = db.Column(db.Text, comment='任职条件')
    other_requirement = db.Column(db.Text, comment='岗位其他要求')


class PersonBaseData(db.Model):
    """ 个人简历的基本信息 """
    __tablename__ = 'PersonBaseData'
    id = db.Column(db.BigInteger(), nullable=False, primary_key=True)
    unit = db.Column(db.String(64), nullable=False, comment='应聘单位')
    series = db.Column(db.String(64), nullable=False, comment='申报系列')
    post_job = db.Column(db.String(128), comment='申报岗位')
    job_number = db.Column(db.BigInteger(), comment='岗位编号')
    now_title = db.Column(db.String(64), comment='现有职称')
    apply_title = db.Column(db.String(64), comment='申报职称')
    source_title = db.Column(db.String(64), comment='来源和职称')
    person_type = db.Column(db.String(64), comment='来源和职称')
    review_status = db.Column(db.String(64), comment='来源和职称')
    patent_situation = db.Column(db.Text, comment='专利情况')
    honor_situation = db.Column(db.Text, comment='奖励情况')
    copyright_situation = db.Column(db.Text, comment='著作情况')
    working_assumption = db.Column(db.Text, comment='工作设想')
    first_person_thesis = db.Column(db.Text, comment='第一人称发布论文数')
    lead_project = db.Column(db.Text, comment='主持项目')
    lead_project = db.Column(db.Text, comment='主持项目')
    created_time = db.Column(db.DateTime, default=datetime.now, comment='创建时间')
    update_time = db.Column(db.DateTime, comment='更新时间')


