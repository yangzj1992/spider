# -*- coding: utf-8 -*-
import bs4
import re
import requests

from bs4 import BeautifulSoup

def work(html):
    soup = BeautifulSoup(html,'html.parser')
    name = soup.find_all(attrs={"bgcolor":"#dedede"})
    color = soup.find_all(attrs={"bgcolor":"#c0c0c0"})
    for names in name:
      if (pattern1.search(names.contents[0])):
        print(names.contents[0])
    for colors in color:
      if pattern2.search(colors.contents[0]):
        print(colors.contents[0])

pattern1 = re.compile(r'[a-z]') 
pattern2 = re.compile(r'^#')
use_data = {}
use_data['url'] = r'http://xh.5156edu.com/page/z1015m9220j18754.html'
response = requests.get(use_data['url'])
print type(requests.get(use_data['url']).text) #查看编码
response.encoding = 'gbk'
work(response.text)




