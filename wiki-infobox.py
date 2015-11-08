# coding=utf-8
import urllib
import time
import re

#第一步 获取维基百科内容
#http://zh.wikipedia.org/wiki/程序设计语言列表
keyname="程序设计语言列表"
temp='http://zh.wikipedia.org/wiki/'+str(keyname)
content = urllib.urlopen(temp).read()
open('wikipedia.html','w+').write(content)
print 'Start Crawling pages!!!'

#第二步 获取网页中的所有URL
#从原文中"0-9"到"参看"之间是A-Z各个语言的URL
start=content.find(r'0-9')
end=content.find(r'参看')
cutcontent=content[start:end]
link_list = re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')", cutcontent)
fileurl=open('test.txt','w')
for url in link_list:
    #字符串包含wiki或/w/index.php则正确url 否则A-Z
    if url.find('wiki')>=0 or url.find('index.php')>=0:     
        fileurl.write(url+'\n')
        #print url
        num=num+1
fileurl.close()
print 'URL Successed! ',num,' urls.'

#第三步 下载每个程序URL静态文件并获取Infobox对应table信息
#国家：http://zh.wikipedia.org/wiki/阿布哈茲
#语言：http://zh.wikipedia.org/wiki/ActionScript
info=open('infobox.txt','w')
info.write('****************获取程序语言信息*************\n\n')
j=1
for url in link_list:
    if url.find('wiki')>=0 or url.find('index.php')>=0:
        #下载静态html
        wikiurl='http://zh.wikipedia.org'+str(url)
        print wikiurl
        language = urllib.urlopen(wikiurl).read()
        name=str(j)+' language.html'
        #注意 需要创建一个country的文件夹 否则总报错No such file or directory
        open(r'language/'+name,'w+').write(language) #写方式打开+没有即创建
        #获取title信息
        title_pat=r'(?<=<title>).*?(?=</title>)'
        title_ex=re.compile(title_pat,re.M|re.S)
        title_obj=re.search(title_ex, language) #language对应当前语言HTML所有内容
        title=title_obj.group()
        #获取内容'C语言 - 维基百科，自由的百科全书' 仅获取语言名
        middle=title.find(r'-')
        info.write('【程序语言  '+title[:middle]+'】\n')
        print title[:middle]

        #第四步 获取Infobox的内容
        #标准方法是通过<table>匹配</table>确认其内容，找与它最近的一个结束符号
        #但此处分析源码后取巧<p><b>实现
        start=language.find(r'<table class="infobox vevent"') #起点记录查询位置
        end=language.find(r'<p><b>'+title[:middle-1])    #减去1个空格
        infobox=language[start:end]
        #print infobox

        #第五步 获取table中属性-属性值
        if "infobox vevent" in language: #防止无Infobox输出多余换行
            #获取table中tr值
            res_tr = r'<tr>(.*?)</tr>'
            m_tr =  re.findall(res_tr,infobox,re.S|re.M)
            for line in m_tr:
                #print unicode(line,'utf-8')
            
                #获取表格第一列th 属性
                res_th = r'<th scope=.*?>(.*?)</th>'
                m_th = re.findall(res_th,line,re.S|re.M)
                for mm in m_th:
                    #如果获取加粗的th中含超链接则处理
                    if "href" in mm:
                        restr = r'<a href=.*?>(.*?)</a>'
                        h = re.findall(restr,mm,re.S|re.M)
                        print unicode(h[0],'utf-8')
                        info.write(h[0]+'\n')
                    else:
                        #报错用str()不行 针对两个类型相同的变量
                        #TypeError: coercing to Unicode: need string or buffer, list found
                        print unicode(mm,'utf-8') #unicode防止乱
                        info.write(mm+'\n')

                #获取表格第二列td 属性值
                res_td = r'<td .*?>(.*?)</td>'
                m_td = re.findall(res_td,line,re.S|re.M)
                for nn in m_td:
                    if "href" in nn:
                        #处理超链接<a href=../rel=..></a>
                        res_value = r'<a .*?>(.*?)</a>'
                        m_value = re.findall(res_value,nn,re.S|re.M) #m_td会出现TypeError: expected string or buffer
                        for value in m_value:
                            print unicode(value,'utf-8'),
                            info.write(value+' ')
                        print ' ' #换行
                        info.write('\n')
                    else:
                        print unicode(nn,'utf-8')
                        info.write(nn+'\n')
            print '\n'
            info.write('\n\n')
        else:
            print 'No Infobox\n'
            info.write('No Infobox\n\n\n')

        #设置下载数量
        j=j+1
        time.sleep(1)
        if j==40:
            break;
    else:
        print 'Error url!!!'
else:
    print 'Download over!!!'