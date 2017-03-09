#-*- coding: utf-8 -*-


import re
import urllib2
from bs4 import BeautifulSoup

url = "http://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false"
data = 'first=true&pn=1&kd=web%E5%AE%89%E5%85%A8/'

response0 = urllib2.urlopen(url,data)#打开目标页面，存入变量up
content0 = response0.read()#从up中读入该HTML文件


position_ids = re.findall('"positionId":(.*?),"',content0,re.S)
res_data = {}
cont = 1
fopen = open('output.txt','w')
for position_id in position_ids:

    fopen.write('%d. ' % cont)

    #http://www.lagou.com/jobs/709515.html
    url = "http://www.lagou.com/jobs/%s.html"%position_id
    response = urllib2.urlopen(url)  # 打开目标页面，存入变量up
    content = response.read()
    soup = BeautifulSoup(content,"lxml")
    #print soup
    # url
    res_data['url'] = url
    print 'url',res_data['url']
    fopen.write('%s' % res_data['url'])
    fopen.write('\n')

    # 公司
    company_node = soup.find('dt', class_="clearfix join_tc_icon").find("div")
    res_data['company'] = company_node.get_text().encode('utf-8')
    fopen.write('%s' % res_data['company'])
    fopen.write('\n')
    print 'company',res_data['company']

    # 职位
    # position_node = soup.find('dt', class_="clearfix join_tc_icon").find("h1")
    # position_node = soup.find('h2')
    # res_data['position'] = company_node.get_text().encode('utf-8')
    res_data['position'] = re.findall('<h1 title="(.*?)">', content,re.S)
    print 'position',res_data['position']
    fopen.write('%s' % res_data['position'])
    fopen.write('\n')

    # 薪资
    salary_node = soup.find('span', class_="red")
    res_data['salary'] = salary_node.get_text()
    print 'salary',res_data['salary']
    fopen.write('%s' % res_data['salary'])
    fopen.write('\n')

    # 要求
    ###不确定
    request_node = soup.find('span', class_="")
    res_data['request'] = request_node.get_text().encode('utf-8')
    print 'request',res_data['request']
    fopen.write('%s' % res_data['request'])
    fopen.write('\n')



    # 职位诱惑
    lure_node = soup.find('dd', class_="job_request").find_all("p")[1]  # 不确定
    res_data['lure'] = lure_node.get_text().encode('utf-8')
    print 'lure',res_data['lure']
    fopen.write('%s' % res_data['lure'])
    fopen.write('\n')



    # 发布时间
    time_node = soup.find('p', class_="publish_time")
    res_data['time'] = time_node.get_text().encode('utf-8')
    print 'time',res_data['time']
    fopen.write('%s' % res_data['time'])
    fopen.write('\n')


    # 职位描述
    description_set = set()
    description_node = soup.find('h3', class_="description").find_all("p")
    for description in description_node:
        description_in = description.get_text().encode('utf-8')
        description_set.add(description_in)

    res_data['description'] = description_set
    print 'description',res_data['description']
    fopen.write('%s' % res_data['description'])
    fopen.write('\n')
    fopen.write('\n')

    cont = cont + 1

fopen.close()

