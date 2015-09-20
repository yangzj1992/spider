#coding=utf-8

import re
import urllib2
import socket
import urllib

def user_agent(url):
    req_header = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    req_timeout = 20
    try:
        response = urllib2.urlopen(url)
        html = response.read()
    except urllib2.URLError as e:
        print e.message
    except socket.timeout as e:
        user_agent(url)
    return html

def getImg(html):
    reg = r'src="(.*?\.jpg)" pic_ext=' #此处为正则表达式，用于匹配页面中的图片链接，不同的网页图片链接的格式有所不用，此处需按需调整
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    print imglist
    # x = 1
    # for imgurl in imglist:
    #     urllib.urlretrieve(imgurl,'%s.jpg' % x )
    #     print "第",x,"张下载完成！"
    #     x+=1

#将图片所在网页链接放入此处，大部分在WINDOWS下使用，所以不采用变量传入的方式        
html = user_agent("http://www.baidu.com")

getImg(html)