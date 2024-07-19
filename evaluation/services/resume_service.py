# encoding: utf-8
"""
@author: chenxiyue
@contact: chenxiyue@kuaishou.com
@software: PyCharm
@file: resume_service.py
@time: 2024/7/5 17:40
"""
import datetime
import io
import logging
import pandas as pd

from pdfplumber import open as pdf_open

from infer_model.inference import ModelInference

from evaluation.common.computing_method import *


def analyzing_resume(pdf_file):
    data = parse_pdf_to_key_value(pdf_file)
    logging.info(f"parsed_data: {data}")
    return True


def parse_pdf_to_key_value(pdf_file):
    data = {}
    with pdf_open(io.BytesIO(pdf_file.read())) as pdf:
        for page in pdf.pages:
            # 提取表格
            tables = page.extract_tables()
            for table in tables:
                # 假设第一行为标题行
                if len(table) > 1:
                    headers = [cell.strip() for cell in table[0]]
                    for i, row in enumerate(table[1:], start=1):
                        # 构建字典
                        row_data = dict(zip(headers, [cell.strip() for cell in row]))
                        # 将数据添加到data字典中，使用表格编号和行编号作为键
                        key = f"Table{i}_{headers[0]}"  # 假设使用第一列作为键
                        data[key] = row_data
    return data


def evaluation_score_excel_service(excel_file_path: str):
    """ 查询数据库中存储的简历信息，构造结构体传数据给模型获取评分 """
    df = pd.read_excel(excel_file_path, sheet_name='简历量化结果', engine='openpyxl')
    source_resume_json_list = df.to_dict('records')
    evaluation_result = []
    for resume_json in source_resume_json_list:
        result_json = evaluation_score_execute(resume_json)
        evaluation_result.append(result_json)
    return evaluation_result


def evaluation_score_json_service(resume_json):
    """ 传入json数据，获取评分 """
    result_json = evaluation_score_execute(resume_json)
    return result_json


def evaluation_score_execute(resume_json: dict):
    result_json = dict()
    # 调用模型获取简历评分
    model = ModelInference(r'/Users/xiyuechen/PycharmProjects/intelligent-resume-evaluation/infer_model/model/xgb_model.pkl')
    result_score = model.predict(resume_json)
    result_json['resume_match_score'] = result_score[0] if result_score else 0
    for key, value in resume_json.items():
        if key in methods_dict:
            result_json[key+"_score"] = methods_dict[key](value)
        # else:
        #     result_json[key] = value
    result_json["Q1_Q2_score"] = evaluation_Q1_Q2(resume_json['qOneCount'], resume_json['qTwoCount'])
    return result_json


def convert_to_age(birth_date_str):
    # 将字符串转换为日期格式
    birth_date = datetime.strptime(birth_date_str, "%Y%m%d").date()
    # 获取今天的日期
    today = datetime.now().date()
    # 计算年龄
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

    return age


if __name__ == '__main__':
    resume_json = {"aPaperCount":0,"academy":"4b2ecfc3dde05ba727d9a703f623e0de","averageIF":2.199999968210856,"averageRef":37,"bachelorUniversity":"fe52bfe14500ed32b94eac5e3c73e555","bachelorUniversityLevel":0,"birthmonth":"19900801","code":"B82727C0AA204E65A9C3981615D742D8","countOfCCFA":0,"doctorAfterProjectCount":0,"doctorAfterProjectFund":0,"doctorUniversity":"fd7fa6cd275f73b8d26b12467e9b2716","doctorUniversityLevel":4,"gender":"1","highestIF":3.299999952316284,"highestProjectFund":0,"highestRef":54,"lowestIF":0,"lowestRef":0,"masterUniversity":"fe52bfe14500ed32b94eac5e3c73e555","masterUniversityLevel":0,"nationalProjectCount":0,"nationalProjectTotalFund":0,"paperCount":3,"patentCount":0,"position":"3874a0aa04a727b40b9d2e63b447047a","projectCount":3,"projectFund":0,"qOneAverageRank":0,"qOneCount":0,"qOneHighestRank":0,"qOneLowestRank":58,"qTwoCount":0,"series":"f244de573c766e13515dd5dd52875b79","whetherPass":0}
    result = evaluation_score_execute(resume_json)
    print(result)