# encoding: utf-8
"""
@author: chenxiyue
@contact: chenxiyue@kuaishou.com
@software: PyCharm
@file: resume_service.py
@time: 2024/7/5 17:40
"""
import io
import logging

from pdfplumber import open as pdf_open


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


# 示例使用
# 假设 resume_file 是一个包含PDF文件的 FileStorage 对象
# parsed_data = parse_pdf_to_key_value(resume_file)
# print(parsed_data)
# def analyzing_resume(resume_file):
# 	""" 解析简历信息 """
# 	# 使用上下文管理器读取文件到内存
# 	with io.BytesIO(resume_file.read()) as bio:
# 		# 使用PdfReader代替PdfFileReader
# 		pdf = PdfReader(bio)
#
# 		# 初始化文本列表
# 		text_parts = []
# 		for page in pdf.pages:
# 			# 使用extract_text()方法获取文本
# 			text_parts.append(page.extract_text())
#
# 		# 连接文本部分
# 		text = '\n'.join(filter(None, text_parts))
# 		return text


def evaluation_score_service(resume_id: int):
    """ 查询数据库中存储的简历信息，构造结构体传数据给模型获取评分 """
    # TODO：查询简历信息
    