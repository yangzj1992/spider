# -*- coding: utf-8 -*-
import bs4
import urllib
import re

from bs4 import BeautifulSoup

def user_agent(url):
    req_header = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    req_timeout = 10
    try:
        response = urllib.urlopen(url)
        html = response.read()
    except urllib.URLError as e:
        print e.message
    except socket.timeout as e:
        user_agent(url)
    return html

def work(url):
    print(url)
    soup = BeautifulSoup(url,'html.parser')
    print(soup.prettify())

url = r'https://zh.wikipedia.org/zh/\%E9\%A2\%9C\%E8\%89\%B2\%E5\%88\%97\%E8\%A1\%A8' 
print(url)
html = user_agent(url)
work(html)




