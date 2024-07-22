# encoding: utf-8
"""
@author: chenxiyue
@contact: chenxiyue@126.com
@software: PyCharm
@file: model.py
@time: 2024/7/2 15:53
"""
from datetime import datetime

from evaluation.models.dbs import mysql as db


class ResumeProfile(db.Model):
    __tablename__ = 'resume_profile'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    code = db.Column(db.String(64), nullable=False, comment='编号')
    whetherPass = db.Column(db.String(1), default='0', comment='是否通过')
    series = db.Column(db.String(64), comment='系列')
    position = db.Column(db.String(64), comment='申报岗位')
    academy = db.Column(db.String(64), comment='应聘单位')
    gender = db.Column(db.SmallInteger, default=0, comment='性别')
    birthmonth = db.Column(db.String(32), comment='出生年月')
    bachelorUniversity = db.Column(db.String(64), comment='本科学校')
    bachelorUniversityLevel = db.Column(db.Integer, default=0, comment='硕士学校级别')
    masterUniversity = db.Column(db.String(64), comment='硕士学校')
    masterUniversityLevel = db.Column(db.Integer, default=0, comment='硕士学校类别')
    doctorUniversity = db.Column(db.String(64), comment='博士学校')
    doctorUniversityLevel = db.Column(db.Integer, default=0, comment='博士学校级别')
    projectCount = db.Column(db.Integer, default=0, comment='项目数')
    nationalProjectCount = db.Column(db.Integer, default=0, comment='国家级项目数')
    projectFund = db.Column(db.Numeric(10, 2), default=0.00, comment='项目经费')
    highestProjectFund = db.Column(db.Numeric(10, 2), default=0.00, comment='最高项目经费')
    nationalProjectTotalFund = db.Column(db.Numeric(10, 2), default=0.00, comment='国家级项目总经费')
    doctorAfterProjectFund = db.Column(db.Numeric(10, 2), default=0.00, comment='博士后项目经费')
    doctorAfterProjectCount = db.Column(db.Integer, default=0, comment='博士后项目')
    highestIF = db.Column(db.Numeric(10, 6), default=0.000000, comment='最高IF')
    lowestIF = db.Column(db.Numeric(10, 6), default=0.000000, comment='最低IF')
    averageIF = db.Column(db.Numeric(10, 6), default=0.000000, comment='平均IF')
    qOneCount = db.Column(db.Integer, default=0, comment='Q1区数')
    qOneHighestRank = db.Column(db.Integer, default=0, comment='Q1区最高排名')
    qOneLowestRank = db.Column(db.Integer, default=0, comment='Q1最低排名')
    qOneAverageRank = db.Column(db.Numeric(10, 6), default=0.000000, comment='Q1平均排名')
    qTwoCount = db.Column(db.Integer, default=0, comment='Q2区数量')
    paperCount = db.Column(db.Integer, default=0, comment='论文数')
    countOfCCFA = db.Column(db.Integer, default=0, comment='CCFA数')
    highestRef = db.Column(db.Integer, default=0, comment='最高引用')
    averageRef = db.Column(db.Integer, default=0, comment='平均引用')
    lowestRef = db.Column(db.Integer, default=0, comment='最低引用')
    aPaperCount = db.Column(db.Integer, default=0, comment='A类目录')
    patentCount = db.Column(db.Integer, default=0, comment='专利数')
    
    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}


class ResumeIndexDataInfo(db.Model):
    __tablename__ = 'ResumeIndexDataInfo'
    id = db.Column(db.BigInteger(), nullable=False, primary_key=True)
    index_name = db.Column(db.String(64), nullable=False, comment='指标名称')
    index_upper_limit = db.Column(db.Float(), nullable=False, comment='指标上限值')
    index_lower_limit = db.Column(db.Float(), nullable=False, comment='指标下限值')



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
    recruitment_id = db.Column(db.BigInteger(), nullable=False, comment='招聘岗位id')
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


class Education(db.Model):
    """ 教育经历 """
    __tablename__ = 'Education'
    id = db.Column(db.BigInteger(), nullable=False, primary_key=True)
    person_id = db.Column(db.BigInteger(), nullable=False, comment='个人简历id')
    school_name = db.Column(db.String(128), nullable=False, comment='学校名称')
    background = db.Column(db.String(64), nullable=False, comment='学历阶段：本科，硕士，博士')
    school_rank = db.Column(db.BigInteger(), comment='学校排名')
    category = db.Column(db.String(128), comment='学校类别：985/211')


class WorkExperience(db.Model):
    """ 工作经历 """
    __tablename__ = 'WorkExperience'
    id = db.Column(db.BigInteger(), nullable=False, primary_key=True)
    person_id = db.Column(db.BigInteger(), nullable=False, comment='个人简历id')
    work_unit = db.Column(db.String(128), nullable=False, comment='工作单位')
    work_time = db.Column(db.String(64), nullable=False, comment='工作起止时间')
    research_direction = db.Column(db.String(128), comment='研究方向')
    technical_title = db.Column(db.String(128), comment='职位职称')


class TeachSituation(db.Model):
    """ 教育学生情况 """
    __tablename__ = 'TeachSituation'
    id = db.Column(db.BigInteger(), nullable=False, primary_key=True)
    person_id = db.Column(db.BigInteger(), nullable=False, comment='个人简历id')
    teach_class = db.Column(db.Text, comment='教育班级')
    teach_student = db.Column(db.Text, comment='教育学生')
    teach_result = db.Column(db.Text, comment='教学成果')


class Dissertation(db.Model):
    """ 论文情况 """
    __tablename__ = 'Dissertation'
    id = db.Column(db.BigInteger(), nullable=False, primary_key=True)
    person_id = db.Column(db.BigInteger(), nullable=False, comment='个人简历id')
    name = db.Column(db.String(128), nullable=False, comment='论文名称')
    DOI = db.Column(db.String(128), nullable=False, comment='论文DOI')
    journal_title = db.Column(db.String(64), comment='期刊名称')
    publish_time = db.Column(db.String(64),  comment='发表时间')
    rank = db.Column(db.Integer(), comment='排名')
    result = db.Column(db.String(64), comment='成果简介')
    original_show = db.Column(db.Text, comment='原创性说明')


class Project(db.Model):
    """ 项目情况 """
    __tablename__ = 'Project'
    id = db.Column(db.BigInteger(), nullable=False, primary_key=True)
    person_id = db.Column(db.BigInteger(), nullable=False, comment='个人简历id')
    name = db.Column(db.String(128), nullable=False, comment='项目名称')
    source = db.Column(db.String(64), comment='项目来源')
    rank_in_all = db.Column(db.String(64), comment='排名/总人数')
    amount_money = db.Column(db.String(64), comment='到款金额/总金额')


class EvaluationResult(db.Model):
    """ 评价结果 """
    __tablename__ = 'EvaluationResult'
    id = db.Column(db.BigInteger(), nullable=False, primary_key=True)
    person_id = db.Column(db.BigInteger(), nullable=False, comment='个人简历id')
    recruitment_id = db.Column(db.BigInteger(), nullable=False, comment='招聘岗位id')
    match = db.Column(db.Float, comment='岗位匹配度得分')
    match_detail = db.Column(db.Text, comment='岗位匹配度得分详情')
    score = db.Column(db.Float, comment='得分')
    score_detail = db.Column(db.Text, comment='得分详情')
    created_time = db.Column(db.DateTime, default=datetime.now, comment='创建时间')
    update_time = db.Column(db.DateTime, comment='更新时间')