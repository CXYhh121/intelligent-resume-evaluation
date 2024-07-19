# encoding: utf-8
"""
@author: chenxiyue
@contact: chenxiyue@126.com
@software: PyCharm
@file: selenium_chrome.py
@time: 2024/7/11 15:08
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

if __name__ == '__main__':
    # 设置Chrome选项，例如无头模式
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # 无界面模式
    
    # 设置WebDriver路径
    service = Service('/Users/xiyuechen/usr/local/bin')  # 替换为你的chromedriver的实际路径
    
    # 初始化WebDriver
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # 访问目标网站
    driver.get('https://scholar.google.com/scholar?q=%E9%97%AE%E9%A2%98%E5%88%86%E6%9E%90%E6%A8%A1%E5%9E%8B&hl=zh-CN&as_sdt=0,5')
    
    # 等待页面加载完成，可以使用time.sleep()或更高级的等待条件
    time.sleep(5)  # 假设页面需要5秒来加载
    
    # 获取页面源代码
    page_source = driver.page_source
    
    # 打印页面源代码
    print(page_source)
    
    # 不忘关闭浏览器
    driver.quit()