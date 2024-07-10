# encoding: utf-8
"""
@author: chenxiyue
@contact: chenxiyue@kuaishou.com
@software: PyCharm
@file: __init__.py.py
@time: 2024/7/2 15:35
"""
import requests


if __name__ == '__main__':
    url = 'https://scholar.google.com.hk/scholar?hl=zh-CN&as_sdt=0%2C5&q=Effects+of+initial++++condition+and+fuel+composition+on+laminar+burning++velocities+of+blast+furnace+gas+with+low++++heat+value&btnG='
    result = requests.get(url)
    print(result.text)
    pass
