# encoding: utf-8
"""
@author: chenxiyue
@contact: chenxiyue@126.com
@software: PyCharm
@file: computing_method.py
@time: 2024/7/19 17:23
"""
from datetime import datetime


# def processor(key):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             return func(*args, **kwargs)
#         processors[key] = wrapper
#         return wrapper
#     return decorator



#### 综合评分

# birthmonth
def evaluation_age(birth_date_str):
    higest_age = 53
    lowest_age = 24
    # 将字符串转换为日期格式
    birth_date = datetime.strptime(str(birth_date_str), "%Y%m%d").date()
    # 获取今天的日期
    today = datetime.now().date()
    # 计算年龄
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    age_score = 0
    if age > higest_age:
        age_score = 10
    if age < lowest_age:
        age_score = 100
    if lowest_age <= age <= higest_age:
        age_score = ((age - lowest_age) / (higest_age - lowest_age) + 2 / 8) * 80
    return age_score


# bachelorUniversity、masterUniversity、doctorUniversity
def evaluation_university(university_level):
    eval_dict = {
        "5": 100,
        "4": 80,
        "3": 60,
        "2": 40,
        "1": 20,
        "0": 0
    }
    return eval_dict.get(str(int(university_level)), 0)


# patent 专利
def evaluation_patent(patent_num):
    patent_dict = {
        "3": 100,
        "2": 67,
        "1": 33,
        "0": 0
    }
    return patent_dict.get(str(int(patent_num)), 0)


### 项目评分
# project_num 项目数量
def evaluation_project_number(project_num):
    project_dict = {
        "5": 100,
        "4": 80,
        "3": 60,
        "2": 40,
        "1": 20,
        "0": 0
    }
    return project_dict.get(str(int(project_num)), 0)


# project_money 项目金额
def evaluation_project_money(project_money):
    project_highest_money = 8982
    project_lowest_money = 0
    
    return (project_money/project_highest_money) * 100


# project_highest_money 最高项目金额
def evaluation_project_highest_money(project_highest_money):
    project_highest_money_high = 7500
    project_lowest_money = 0
    
    return (project_highest_money/project_highest_money_high) * 100


# 国家级项目数量
def evaluation_national_project_number(national_project_num):
    national_project_dict = {
        "3": 100,
        "2": 67,
        "1": 33,
        "0": 0
    }
    return national_project_dict.get(str(int(national_project_num)), 0)


# 国家级项目经费
def evaluation_national_project_money(national_project_money):
    national_highest_project_money = 822
    national_lowest_project_money = 0
    
    return (national_project_money/national_highest_project_money) * 100


# 博士后项目数量
def evaluation_postdoc_project_number(postdoc_project_num):
    postdoc_project_dict = {
        "3": 100,
        "2": 67,
        "1": 33,
        "0": 0
    }
    return postdoc_project_dict.get(str(int(postdoc_project_num)), 0)


# 博士后项目经费
def evaluation_postdoc_project_money(postdoc_project_money):
    postdoc_highest_project_money = 100
    postdoc_lowest_project_money = 0
    return (postdoc_project_money/postdoc_highest_project_money) * 100


### 论文评价
# paper_num 论文数量
def evaluation_paper_number(paper_num):
    paper_highest_num = 15
    paper_lowest_num = 0
    return (paper_num/paper_highest_num) * 100


# IF 论文影响因子
def evaluation_paper_IF(paper_IF):
    paper_highest_IF = 51.4000015258789
    paper_lowest_IF = 0
    return (paper_IF/paper_highest_IF) * 100


# 高被引论文数量
def evaluation_high_citation_paper_number(high_citation_paper_num):
    high_citation_paper_highest_num = 3448
    high_citation_paper_lowest_num = 0
    return (high_citation_paper_num/high_citation_paper_highest_num) * 100


# Q1 Q2指数
def evaluation_Q1_Q2(Q1, Q2):
    Q1_highest = 15
    Q2_highest = 9
    Q1_lowest = 0
    Q2_lowest = 0
    
    return (Q1*1.5+Q2) / (Q1_highest*1.5+Q2_highest) * 100


# A类论文数
def evaluation_A_paper_number(A_paper_num):
    A_paper_dict= {
        "4": 100,
        "3": 75,
        "2": 50,
        "1": 25,
        "0": 0
    }
    return A_paper_dict.get(str(int(A_paper_num)), 0)


# 项目综合评分
def evaluation_project_score(project_num, project_money, project_highest_money, national_project_num,
                             national_project_money, postdoc_project_num, postdoc_project_money):
    return (evaluation_project_number(project_num) * 0.1 +
            evaluation_project_money(project_money) * 0.1 +
            evaluation_project_highest_money(project_highest_money) * 0.1 +
            evaluation_national_project_number(national_project_num) * 0.15 +
            evaluation_national_project_money(national_project_money) * 0.15 +
            evaluation_postdoc_project_number(postdoc_project_num) * 0.2 +
            evaluation_postdoc_project_money(postdoc_project_money) * 0.2)


# 论文综合得分
def evaluation_paper_score(paper_num, paper_IF, high_citation_paper_num, Q1, Q2, A_paper_num):
    return (evaluation_paper_number(paper_num) * 0.15 +
            evaluation_paper_IF(paper_IF) * 0.15 +
            evaluation_high_citation_paper_number(high_citation_paper_num) * 0.2 +
            evaluation_Q1_Q2(Q1, Q2) * 0.2 +
            evaluation_A_paper_number(A_paper_num) * 0.3)


methods_dict = {
    "projectCount": evaluation_project_number,
    "highestIF": evaluation_paper_IF,
    "highestProjectFund": evaluation_project_highest_money,
    "nationalProjectTotalFund": evaluation_national_project_money,
    "projectFund": evaluation_project_money,
    "countOfCCFA": evaluation_A_paper_number,
    "birthmonth": evaluation_age,
    "masterUniversityLevel": evaluation_university,
    "doctorAfterProjectCount": evaluation_postdoc_project_number,
    "bachelorUniversityLevel": evaluation_university,
    "doctorAfterProjectFund": evaluation_postdoc_project_money,
    "highestRef": evaluation_high_citation_paper_number,
    "aPaperCount": evaluation_A_paper_number,
    "doctorUniversityLevel": evaluation_university,
    "paperCount": evaluation_paper_number,
    "nationalProjectCount": evaluation_national_project_number
}