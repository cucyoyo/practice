#-*- coding: utf-8 -*-
import csv
import re
import urllib2
from bs4 import BeautifulSoup

#curl 'http://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false' --data 'first=true&pn=1&kd=web%E5%AE%89%E5%85%A8'



def get_position_ids(root_url,data):
    response0 = urllib2.urlopen(root_url,data)#打开目标页面，存入变量up
    content0 = response0.read()#从up中读入该HTML文件

    position_ids = re.findall('"positionId":(.*?),"',content0,re.S)
    return position_ids


def parser(url):
    res_data = {}
    response = urllib2.urlopen(url)  # 打开目标页面，存入变量up
    content = response.read()
    soup = BeautifulSoup(content, "lxml")
    # print soup
    # url
    res_data['url'] = url

    # 公司
    company_node = soup.find('dt', class_="clearfix join_tc_icon").find("div")
    res_data['company'] = company_node.get_text().encode('utf-8')

    # 职位
    #position_node = soup.find('dt', class_="clearfix join_tc_icon").find("h1")
    position_node = soup.find_all('h2')[1]
    res_data['position'] = position_node.get_text().encode('utf-8')
    # res_data['position'] = re.findall('<h1 title="(.*?)">', content, re.S)

    # 薪资
    salary_node = soup.find('span', class_="red")
    res_data['salary'] = salary_node.get_text()


    # 要求
    requests = soup.find('dd',class_="job_request").find_all('span')
    n = 0
    for request in requests:
        n = n+1
        res_data['request%d'%n] = request.get_text().encode('utf-8')

    # 职位诱惑
    lure_node = soup.find('dd', class_="job_request").find_all("p")[1]  # 不确定
    res_data['lure'] = lure_node.get_text().encode('utf-8')

    # 发布时间
    time_node = soup.find('p', class_="publish_time")
    res_data['time'] = time_node.get_text().encode('utf-8')

    # 职位描述
    descriptions = soup.find('dd', class_="job_bt").find_all("p")
    m = 0
    for description in descriptions:
        m = m + 1
        res_data['description%d'%m] = description.get_text().encode('utf-8')


    return res_data, n, m


def outputer(res_data,cont,fopen,n,m):

    #data_set = set()

    fopen.write('%d. ' % cont)
    #data_set.add(cont)

    print 'url', res_data['url']
    fopen.write('%s' % res_data['url'])
    fopen.write('\n')
    #data_set.add(res_data['url'])

    fopen.write('%s' % res_data['company'])
    fopen.write('\n')
    print 'company', res_data['company']
    #data_set.add(res_data['company'])

    print 'position', res_data['position']
    fopen.write('%s' % res_data['position'])
    fopen.write('\n')
    #data_set.add(res_data['position'])

    print 'salary', res_data['salary']
    fopen.write('%s' % res_data['salary'])
    fopen.write('\n')
    #data_set.add(res_data['salary'])

    for each in range(2, n + 1):
        print '%d'%each, res_data['request%d'%each]
        fopen.write('%s' % res_data['request%d'%each])
        fopen.write('\n')
        #data_set.add(res_data['request%d'%each])

    print 'lure', res_data['lure']
    fopen.write('%s' % res_data['lure'])
    fopen.write('\n')
    #data_set.add(res_data['lure'])

    print 'time', res_data['time']
    fopen.write('%s' % res_data['time'])
    fopen.write('\n')
    #data_set.add(res_data['time'])

    for each in range(1, m+1):
        print '%d' % each, res_data['description%d' % each]
        fopen.write('%s' % res_data['description%d' % each])
        fopen.write('\n')
        fopen.write('\n')
        #data_set.add(res_data['description%d' % each])


    # 尝试使用csv格式输出，暂未成功
    # filename+='.csv'
    # writer = csv.writer(file(filename, 'wb'))#创建一个名为sessdefaults的csv文件
    # writer.writerow([key, value])#指出字段名
    # myIter = dictname.iteritems()
    # while True :
    #     try :
    #         item_list = list(myIter.next())#将键值对元组转换为列表
    #         writer.writerow(item_list)#分行写入
    #         #print repr(item_list)
    #     except StopIteration :
    #         break
    # print data_set
    #
    # csvFile = open("test.csv",'w+')
    # try:
    #     writer = csv.writer(csvFile)
    #     writer.writerow(data_set)
    # finally:
    #     csvFile.close()

def manager(root_url,data):
    position_ids = get_position_ids(root_url, data)

    cont = 1
    fopen = open('output.txt', 'w')

    for position_id in position_ids:

        # http://www.lagou.com/jobs/709515.html
        url = "http://www.lagou.com/jobs/%s.html" % position_id
        data, n, m = parser(url)
        outputer(data,cont,fopen, n, m)
        cont = cont + 1

    fopen.close()

if __name__ == '__main__':
    root_url = "http://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false"
    data = 'first=true&pn=1&kd=web%E5%AE%89%E5%85%A8/'
    manager(root_url,data)
