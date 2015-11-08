# -*- coding: utf-8 -*-
import bs4
import re
import requests

from bs4 import BeautifulSoup

def work(html):
    soup = BeautifulSoup(html,'html.parser')
    print(soup.prettify())

use_data = {}
use_data['url'] = r'http://teach.ustb.edu.cn'
# proxy = {"http":"http://72.46.135.119:21071","https":"https://72.46.135.119:21071"}
response = requests.get(use_data['url'])
# response = requests.get(use_data['url'],proxies = proxy,verify=False)
print type(requests.get(use_data['url']).text) #查看编码
response.encoding = 'gbk'
work(response.text)




