#!/usr/bin/env python
#  -*- coding: utf-8 -*-

import urllib2
import cookielib
from bs4 import BeautifulSoup

import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

url = 'http://www.qiushibaike.com/hot/page/1'
cookie = cookielib.CookieJar()
handler=urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)

user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36'
header = {'User-Agent':user_agent}

re = urllib2.Request(url,headers=header)
response = opener.open(re)



soup = BeautifulSoup(response,"lxml")
words = soup.find_all('div',class_ = "content")

fo = open("wenzi.txt",'w')
#print type(words)
n = 1
for word in words:
    fo.write('%d.'%n)
    fo.write(word.get_text().encode('utf-8'))
    n = n+1

fo.close()