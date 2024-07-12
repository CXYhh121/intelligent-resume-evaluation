# encoding: utf-8
"""
@author: chenxiyue
@contact: chenxiyue@kuaishou.com
@software: PyCharm
@file: citation_papers.py
@time: 2024/7/9 22:35
"""
import random
import re
import time

import pandas as pd
import requests

Cookies = [
    "AEC=AVYB7cpRsKs59IrKRONOOH-cia2YLMZy-jNOkAYM9VgX44CKxXpdyeu5iA; NID=515=F7ZbYSanaXAgeQXeTlMLoObU9rJxPTgycSNGcMTVMtLdxXhk1SkBcnbSmGIgQl9ncrTHQh-ifRxgwLwiRXYv3oJXeHQLzixMXfhLPh2fvHWZvz1gUv1UgrOgYE7qKHZdk74j2zL8LchD3qOPUoh4pKlbhKw-5fxy5CnC5y9Cqylj4-0izC-cI0z7O270jyFYGSfVqrprUwu8uZVs8Y54; GSP=LM=1720776759:S=66eX7-7zmEnophhw",
    "GSP=LM=1720776305:S=sDtCnQX-bDrBaGSP; NID=515=PEeCFXfT9IZn2H3iF-Z7xbmJEAylXtTBHmdPrbn0uhD6HfTqXO49UV8AQQBIulxyFe7gUFjDg6HhQo2Gc-e6_vHOgq2UKJDirGDcRdJE576l0D_2QUKQbampdFiqpFuMk4FJHpqCntCpPGc8KX0bdqOCFkjnzGPNv0VJMu7h-Mcpx8K-0f473A",
    "security_session_verify=46a8b5a3a81d53499a916f544c36ceb0; security_session_mid_verify=0248f3adcb1876d901f056c6f65cc47e; _ga=GA1.1.1443868001.1720778275; __gads=ID=4bfc4077e8135966:T=1720778277:RT=1720778277:S=ALNI_MZ5bFl5RpbNF2FYV3nY1ZuS-VtDEQ; __gpi=UID=00000e8e0f513950:T=1720778277:RT=1720778277:S=ALNI_MYCYWtKgLvMOyQGqXq7VMWX6JUTiQ; __eoi=ID=a8d155a9e0644c2a:T=1720778277:RT=1720778277:S=AA-AfjbiBBvjZw70cm9YB-NY82U0; FCNEC=%5B%5B%22AKsRol8_2AYRYFLovXnG6XBis6MnWEGNn1YJPE53allGMn2wmkg2ld6qLvDgwsCg2zi9FaAD4ydCzIEHym5b4j-a92ctb1sQd1FwwifZgPwQFvVkJaqA7XBYg3wfnfoUBZAvBhk4W9DCzzBuhNfmDHqa-519jgWTnA%3D%3D%22%5D%5D; _ga_9ZN335049N=GS1.1.1720778274.1.1.1720778355.0.0.0",
    "google_verify_data=29f9a431eb55689860434fbfd561c0b2330694283377a335b71897b1; Hm_lvt_a14066940b10ee91991579cdff2b4232=1720688365,1720778239; HMACCOUNT=1AA111881D84171D; NID=515=eRIhJdWM3Al_RymHhW1K-LTcCrFXQxqisHnUH3DWSt_XxngsCIoW4IYeDmypWUM1lWeOXQth1flWiIZ1xNPfINBynKzo7RXLPvheu8h5c5HXj4FDw7NgCyeAeHZcwq4gYHsJFvRb8IS3CpX38haLl5Qk5JLFr1OgIVgti_GzyQY; GSP=LM=1720778247:S=urgOJFMoZQErJaNd; Hm_lpvt_a14066940b10ee91991579cdff2b4232=1720778404"]
User_Agent = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
]
client_data = [
    'CJa2yQEIo7bJAQipncoBCJ33ygEIlaHLAQiGoM0BCLvIzQEI6JPOAQjBlc4BCLOWzgEIxZ3OAQiyn84BCKeizgEI0qLOAQjipc4BCNunzgEY9snNARjX680BGKGdzgE=',
    "CJS2yQEIpLbJAQipncoBCOOHywEIlqHLAQj+mM0BCIagzQEIxZ3OAQipns4BCIChzgEIp6LOAQjjpc4BCOGnzgEIj6jOAQiZqM4BGKCdzgE="]

URLS = ['https://x.sci-hub.org.cn/scholar?hl=zh-TW&as_sdt=0%2C5&q={paper}&btnG=',
        'https://scholar.google.com.hk/scholar?hl=zh-CN&as_sdt=0%2C5&q={paper}&btnG=',
        'https://scholar.google.com/scholar?hl=zh-CN&as_sdt=0%2C5&q={paper}&btnG=',
        'https://www.dotaindex.com/paper_search?type=1&q={paper}&btnG=',
        'https://xueshu.aigrogu.com/scholar?hl=zh-CN&as_sdt=0%2C5&q={paper}&btnG=',
        'https://xs.fropet.com/scholar?hl=zh-CN&as_sdt=0%2C5&q={paper}&btnG=',
        'https://so.cljtscd.com/scholar?hl=zh-CN&as_sdt=0%2C5&q={paper}&btnG=',
        'https://sc.panda985.com/scholar?hl=zh-CN&as_sdt=0%2C5&q={paper}&btnG=']

URLS_COOKIE_DICT = [
    # {
    #     "url": "https://scholar.google.com.hk/scholar?hl=zh-CN&as_sdt=0%2C5&q={paper}&btnG=",
    #     "cookies": "GSP=LM=1720776305:S=sDtCnQX-bDrBaGSP; AEC=AVYB7cp2goPEyhfX8qjirrj8ZIHb9GMuqOq5V9xYBuMlFCxuqu8vyoRCb2I; NID=515=r9WKBEvkr0_EzaQzguKv-w3K16TbuujtRcE3LPdMN1PeNda6TvBhrxgKho9-ZSkoIkGtvGNccfReIuj_U60CIinyxDP4Ogh9Xta-_80zmFmzzNiHuoaXFjlOgQCsYwbbl2HmYPqf7-_tI6qyHtRUZlR20xQMcmcQxD-bCoyXruSJn2KmKsB1UeNjNthxxW0q_Ys2Lpjn1DYAXucfxNPH5lPPwno"
    # },
    {
        "url": 'https://scholar.google.com/scholar?hl=zh-CN&as_sdt=0%2C5&q={paper}&btnG=',
        "cookies": "AEC=AVYB7cpJRi6Qn-9XHyXNmk4j6HJ3a9DJl0Z3ROoHfG6zF3pSel743i8nXQ; GSP=LM=1720776307:S=A6A7ky5MnD2GKZ_Q; NID=515=ck5oE4YQeM4fj0bzO5hmRyEs-ZGiCOTmL5vUGDZFRhnu6Lzpus4T6SvILd1AhoJ1-pvsF4u1twRjIOFMPl8yEoh2qlkm5aSk59co4mLi9D6OViQy3Cy503yuj6EKP8yxMX8pkELWmA9B0MJQf1xzK5GbMbk2_eL2kiDTG2al_p6Py2Tt8YasUbbUl-80cjdNAbphIPWA"
    },
    {
        "url": 'https://www.dotaindex.com/paper_search?type=1&q={paper}&btnG=',
        "cookies": ""
    },
    {
        "url": 'https://xueshu.aigrogu.com/scholar?hl=zh-CN&as_sdt=0%2C5&q={paper}&btnG=',
        "cookies": "Hm_lvt_a14066940b10ee91991579cdff2b4232=1720688365,1720778239; HMACCOUNT=1AA111881D84171D; NID=515=eRIhJdWM3Al_RymHhW1K-LTcCrFXQxqisHnUH3DWSt_XxngsCIoW4IYeDmypWUM1lWeOXQth1flWiIZ1xNPfINBynKzo7RXLPvheu8h5c5HXj4FDw7NgCyeAeHZcwq4gYHsJFvRb8IS3CpX38haLl5Qk5JLFr1OgIVgti_GzyQY; GSP=LM=1720778247:S=urgOJFMoZQErJaNd; google_verify_data=d54755f9b8e1a2ae2e06b0e494aa6e9aa38326b274458cc9fb5bb7e9; Hm_lpvt_a14066940b10ee91991579cdff2b4232=1720779245"
    },
    # {
    #     "url": 'https://xs.fropet.com/scholar?hl=zh-CN&as_sdt=0%2C5&q={paper}&btnG=',
    #     "cookies": "security_session_verify=46a8b5a3a81d53499a916f544c36ceb0; security_session_mid_verify=0248f3adcb1876d901f056c6f65cc47e; _ga=GA1.1.1443868001.1720778275; __gads=ID=4bfc4077e8135966:T=1720778277:RT=1720778277:S=ALNI_MZ5bFl5RpbNF2FYV3nY1ZuS-VtDEQ; __gpi=UID=00000e8e0f513950:T=1720778277:RT=1720778277:S=ALNI_MYCYWtKgLvMOyQGqXq7VMWX6JUTiQ; __eoi=ID=a8d155a9e0644c2a:T=1720778277:RT=1720778277:S=AA-AfjbiBBvjZw70cm9YB-NY82U0; FCNEC=%5B%5B%22AKsRol8_2AYRYFLovXnG6XBis6MnWEGNn1YJPE53allGMn2wmkg2ld6qLvDgwsCg2zi9FaAD4ydCzIEHym5b4j-a92ctb1sQd1FwwifZgPwQFvVkJaqA7XBYg3wfnfoUBZAvBhk4W9DCzzBuhNfmDHqa-519jgWTnA%3D%3D%22%5D%5D; _ga_9ZN335049N=GS1.1.1720778274.1.1.1720778355.0.0.0"
    # },
    {
        "url": 'https://so.cljtscd.com/scholar?hl=zh-CN&as_sdt=0%2C5&q={paper}&btnG=',
        "cookies": ""
    },
    {
        "url": 'https://sc.panda985.com/scholar?hl=zh-CN&as_sdt=0%2C5&q={paper}&btnG=',
        "cookies": "_gid=GA1.2.87514695.1720778151; NID=515=EcNl7gIwmexGNNJKM8NTw-JEjHdKurzQXIWaQ8bevPRV-RFWUl4Jtn7741ZJOSlORzHpEKrJZR_gKhqWcLY3HdhJXWYMzeeHDPk0MUX9P8wYhNwIa_7-xu8BqYeHZ94bNisNZMr3aQl7O1nBbZDqdkE_eNYn0cP-tctt2gmOUzg; GSP=LM=1720778202:S=2rjyDQwbNX8Ei8tx; _gat_gtag_UA_126288799_1=1; _ga=GA1.1.1113490388.1720778151; __gads=ID=7d35214cdffe8c8e:T=1720778161:RT=1720779130:S=ALNI_MbBpGLH795FjlEg6rq8QmImppbZHg; __gpi=UID=00000e8e1052536a:T=1720778161:RT=1720779130:S=ALNI_MbUdptyw9l3Vilr5luH1KwZNOavpA; __eoi=ID=3917cc68e33ce7c1:T=1720778161:RT=1720779130:S=AA-AfjavIrc60fNuSnOCaBuv02MQ; FCNEC=%5B%5B%22AKsRol-RGgF6opguQNZCTl8MpZx6nNJr5HkzWrdv5cq4q_agWXzJQfsPAW85U7KsINudw02RQOuDMS-qIOdcgbfYQytyptrAKfXtMb4GfFV49VTJaR_uMMTKYh4xhEvEIHyFP9a12xiMhB3GF5LV6fByXCN2tHigcA%3D%3D%22%5D%5D; _ga_4F58LQ5NXK=GS1.1.1720778151.1.1.1720779132.58.0.0"
    },
    {
        "url": 'https://so3.cljtscd.com/scholar?hl=zh-CN&as_sdt=0%2C5&q={paper}&btnG=',
        "cookies": "_ga=GA1.1.1721849406.1720777988; security_session_verify=b31a60955ccba066830357965d99f8ca; security_session_mid_verify=67cb59e56ef119c6ba0fd93f44db84f9; _ga_57RHS2FH4B=GS1.1.1720777987.1.1.1720779053.0.0.0"
    }
]


def analysis_citation_excel():
    df = pd.read_excel('/Users/xiyuechen/PycharmProjects/intelligent-resume-evaluation/false_paper_data.xlsx',
                       sheet_name='论文', engine='openpyxl')
    paper_list = df['论文/作品题目'].tolist()
    return paper_list


def get_google_scholar_citation(paper_name):
    random_number = random.randint(1, 5)
    time.sleep(random_number)
    # google_url_ = URLS[random.randint(0, 6)]
    # google_url = google_url_.replace('{paper}', paper_name)
    # Cookie = Cookies[random.randint(0, 1)]
    url_cookie_dict = URLS_COOKIE_DICT[random.randint(0, len(URLS_COOKIE_DICT)-1)]
    google_url = url_cookie_dict.get('url').replace('{paper}', paper_name)
    print("google_url: ", google_url)
    headers = {
        'User-Agent': User_Agent[random.randint(0, 1)],
        'X-Client-Data': client_data[random.randint(0, 1)],
        'Cookie': url_cookie_dict.get('cookies')
    }
    session = requests.Session()
    result = session.get(google_url, headers=headers)
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
            citation = -1
        citation_list.append({"paper": paper, "citation": citation})
    if citation_list:
        output_file = f'papers_with_citations_{int(time.time())}.xlsx'
        df = pd.DataFrame(citation_list)
        df.to_excel(output_file, index=False, engine='openpyxl')
