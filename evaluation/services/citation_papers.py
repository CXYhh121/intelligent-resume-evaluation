# encoding: utf-8
"""
@author: chenxiyue
@contact: chenxiyue@kuaishou.com
@software: PyCharm
@file: citation_papers.py
@time: 2024/7/9 22:35
"""
import re
import time

import pandas as pd
import requests

Cookie = "HSID=AM540tKgJbyIzyY3H; SSID=Aw7-o73vAhldY4G89; APISID=AcbiRg6b2UHcAPLp/A3Mk9mNmcbgeXxtYp; SAPISID=bPTkTA1NMGgX7dH-/ArC7RtZkY7FnrV_oA; __Secure-1PAPISID=bPTkTA1NMGgX7dH-/ArC7RtZkY7FnrV_oA; __Secure-3PAPISID=bPTkTA1NMGgX7dH-/ArC7RtZkY7FnrV_oA; SID=g.a000kwjrDVrrDEkly9ilR8nwJdAtFIi_YArxdPADpBiy2Zvg3wOjwFXEYSElyLIKKfGneXEMcgACgYKAdUSARASFQHGX2Mi1pZ2SWhIKRF9L9MK_rpxHhoVAUF8yKpCmxRwMgMKhg2ULbcJB5mF0076; __Secure-1PSID=g.a000kwjrDVrrDEkly9ilR8nwJdAtFIi_YArxdPADpBiy2Zvg3wOjS5eVMLTjnfgS4PEHarOxQwACgYKAWISARASFQHGX2MiO5zR-BsKFBiEuTLIZxWVqBoVAUF8yKr7mAFLY_G4N0a3Gt68OGNB0076; __Secure-3PSID=g.a000kwjrDVrrDEkly9ilR8nwJdAtFIi_YArxdPADpBiy2Zvg3wOjJvkYYIaPMzPPpPgimd2ldAACgYKARMSARASFQHGX2MiIoKjxn2VKJj42e5gSWndIxoVAUF8yKp3-7dr0h5UTWAXVybRQ_Ei0076; SEARCH_SAMESITE=CgQIwZsB; AEC=AVYB7crUFD1LDWC3vm7tgGLHKg5qCNua-kn7bDk0_IvTbbRsuJMsCW0EwA; NID=515=f0u-qG_3P0Uzv2lgM2_OukTjlmnxAh-7yUtpc6Wd5o_hpUkWgdCQphlqUKzHWpUKvjrKNVN6yeABSC1yp_-mOdMrAA6fjoNhiGPb1B5z-eOFSJkKMudNrUQs4uNMwJtHDW22gngW1kh-hT8leXsElZ7kS71xkI6NauBTplz1ZKGEKrlGTrIcX-SuBrd7NtpKBIvA7M4qTy_t92GoVQK_oDA-0Fz4CGK5OPsaaRYN8njxlHEAxvEzPwuMzBm9mruHaSK1P_N9-d2AbEaK5LjC8_GT5s8QwOJ7XdqEQarsAtlsf1B_ppFv7NKMdXJbY_YtS79iXNXEd7s0x9Mi9EfO-Xkdsdtsip5_TdstjvNuWrQ_6Om6xNe350j6du8Cizc3fGW_NvNyVdCvQCOVU0tObdeRSmBCBR-H0F8oGd9lQum3zE0; GSP=A=1SZJBQ:CPTS=1720582551:LM=1720582551:S=-xnNsxGBJ_CsI9dY"

proxies = {
    'https': 'http://202.101.213.188:22786',
}


def analysis_citation_excel():
    df = pd.read_excel('/Users/xiyuechen/PycharmProjects/intelligent-resume-evaluation/false_paper_data.xlsx',
                       sheet_name='论文', engine='openpyxl')
    paper_list = df['论文/作品题目'].tolist()
    return paper_list


def get_google_scholar_citation(paper):
    time.sleep(2)
    google_url = f"https://scholar.google.com.hk/scholar?hl=zh-CN&as_sdt=0%2C5&q={paper}&btnG="
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'X-Client-Data': 'CJa2yQEIo7bJAQipncoBCJ33ygEIlaHLAQiGoM0BCLvIzQEI6JPOAQjBlc4BCLOWzgEIxZ3OAQiyn84BCKeizgEI0qLOAQjipc4BCNunzgEY9snNARjX680BGKGdzgE=',
        'Cookie': Cookie
    }
    result = requests.get(google_url, headers=headers, proxies=proxies)
    return result.text
    


def extract_number_after_keyword(text):
    pattern = r'被引用次数：(\d+)'
    matches = re.findall(pattern, text)
    if matches:
        citation_count = int(matches[0])
        return citation_count
    else:
        print("未找到匹配的引用次数")


if __name__ == '__main__':
    paper_list = analysis_citation_excel()
    citation_list = []
    for paper in paper_list:
        result = get_google_scholar_citation(paper)
        citation = extract_number_after_keyword(result)
        if not citation:
            # 如果未找到匹配的引用次数，则跳出循环，将已爬取的数据存储
            break
        citation_list.append({"paper": paper, "citation": citation})
    print(citation_list)
    df = pd.DataFrame(citation_list)
    df.to_excel('papers_with_citations.xlsx', index=False, engine='openpyxl')

    
    
