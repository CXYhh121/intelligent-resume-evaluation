# encoding: utf-8
"""
@author: chenxiyue
@contact: chenxiyue@kuaishou.com
@software: PyCharm
@file: db_handler.py
@time: 2024/7/5 20:04
"""
import logging

from flask_sqlalchemy import BaseQuery

from evaluation.models import app, sqlalchemy_context
from evaluation.models.model import PersonBaseData

TimeFormat = 'YYYY-MM-DD HH:mm:ss'

logger = logging.getLogger()


class DbHandler(BaseQuery):
    def __init__(self):
        pass
    
    @staticmethod
    @sqlalchemy_context(app)
    def query_test(limit=None, offset=None):
        """
        查询PersonBaseData表的部分记录，使用分页。
        :param limit: 每页记录数
        :param offset: 跳过的记录数
        :return: 查询结果
        """
        return PersonBaseData.query.limit(limit).offset(offset).all()
    
    @staticmethod
    @sqlalchemy_context(app)
    def query_person_base_data(query_filter: dict):
        """
        查询简历基础信息，根据query_filter中的条件进行查询。
        :param query_filter: 查询条件
        :return: 查询结果, list类型
        """
        result_obj = PersonBaseData.query.filter_by(**query_filter).all()
        if result_obj is None:
            return []
        return [obj.to_dict() for obj in result_obj]
    
    @staticmethod
    @sqlalchemy_context(app)
    def query_person_base_data_by_id(person_id: int):
        """
        通过id查询简历基础信息
        :param person_id: 简历id
        :return: 查询结果, dict类型
        """
        return PersonBaseData.query.filter_by(id=person_id).first().to_dict()
    
    @staticmethod
    @sqlalchemy_context(app)
    def query_resume_key_factors(resume_id: int):
        """
        通过简历id查询简历评价的关键因子返回
        :param resume_id: 简历id
        :return: 查询结果, dict类型
        """
        
        
