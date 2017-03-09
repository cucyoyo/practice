#-*- coding: utf-8 -*-

import csv
import re
from bs4 import BeautifulSoup

from lagou import url_manager,html_downloader,company_parser,position_parser,html_downloader,outputer

fopen = open('output.txt', 'w')

class Lagou(object):

    def __init__(self):#初始化

        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.company_parser = company_parser.CompanyParser()
        self.position_parser = position_parser.PositionParser()
        self.outputer = outputer.Outputer()

    def collect_ids(self, root_url,data,position_ids,company_ids):

        content = self.downloader.get_content(root_url,data)

        if content == None:
            print 'url:%s,data:%s爬取失败'%(root_url,data)
        else:
            position_ids = self.position_parser.get_position_ids(content,position_ids)
            company_ids = self.company_parser.get_company_ids(content,company_ids)
        return position_ids,company_ids

    def manager(self, position_ids,company_ids):

        self.position_manager(position_ids)#根据position_id得到职位对应的url，接下来进行爬源码、解析和输出
        self.urls.add_new_ids(company_ids)
        # print '有没有ｃｏｍｐａｎｙ　ｉｄ??? ',self.urls.has_new_id()
        while self.urls.has_new_id():


            new_id = self.urls.get_new_id()
            # print '新ｉｄ是？？？　',new_id
            # self.company_parser.parser(new_id)

            company_url, company_data = self.company_parser.get_url(new_id)

            # print '公司ｕｒｌ和ｄａｔａ？？？', company_url,company_data
            content = self.downloader.get_content(company_url, company_data)
            # print content
            #"pageSize":10 "totalCount":"410","
            totalCount = re.findall('"totalCount":"(.*?)","', content, re.S)[0]
            # print totalCount
            pageSize = re.findall('"pageSize":(.*?),"', content, re.S)[0]
            # print pageSize
            page = int(totalCount) / int(pageSize) + 1
            # print page
            position_ids1 = set()
            company_ids1 = set()
            for n in range(1,page+1):
                new_data = self.company_parser.get_new_data(new_id,n)
                self.collect_ids(company_url, new_data, position_ids1, company_ids1)

            # position_ids = self.position_parser.get_position_ids(content)
            self.position_manager(position_ids1)
            #company_position_ids =

            # conpany_data, n, m = self.position_parser.parser(company_url)
            # self.outputer.outputer(data, cont, fopen, n, m)
            # cont = cont + 1


    def position_manager(self,position_ids):
        cont = 1
        for position_id in position_ids:
            # http://www.lagou.com/jobs/709515.html
            url = "http://www.lagou.com/jobs/%s.html" % position_id
            content = self.downloader.get_content(url, data=None)
            if content == None:
                print '爬取失败！url:%s'%url
            else:
                data, n, m = self.position_parser.parser(url, content)
                if data == None:
                    print '爬取失败！url:%s'%url
                else:
                    self.outputer.outputer(data, cont, fopen, n, m)
                    cont = cont + 1



    def start(self,name):#此函数得出root_url的页码并根据页数开始循环抓取

        # http://www.lagou.com/jobs/list_web安全?px=default&city=全国

        url = 'http://www.lagou.com/jobs/list_%s?px=default&city=全国'%name#root_url（total_page信息从root_url中提取）
        content = self.downloader.get_content(url,data = None)
        if content == None:
            print '%s爬取失败'%url
        else:
            soup = BeautifulSoup(content, "lxml")
            # < span class ="span totalNum" > 3 < / span >
            page = soup.find('span', class_ = "span totalNum").get_text()#提取页码信息
            #由于职位信息是动态加载的，直接从上面url无法得到我们所需的职位url，下面root_url是经过分析以后得到的动态加载时的ｕｒｌ
            # 分析结果：url:'http://www.lagou.com/jobs/positionAjax.json?px=default&needAddtionalResult=false'
            # --data 'first=true&pn=1&kd=web安全'
            root_url = 'http://www.lagou.com/jobs/positionAjax.json?px=default&needAddtionalResult=false'
            #这里初始化定义职位和公司id的原因是：这里相当于定义了一个全局变量变量，防止收集的两种id在每次循环中被覆盖。如果在每次循环结束后直接执行manager函数，则公司id的判重操作会出现问题
            position_ids = set()
            company_ids = set()
            for n in range(1,int(page)+1):

                data = 'first=true&pn=%d&kd=%s'%(n,name)#获取动态信息对应url的data

                position_ids, company_ids = self.collect_ids(root_url,data,position_ids,company_ids)
             #for循环执行完毕后的结果是：爬取了web安全，全国范围内，所有职位的，position_id和company_id并分别保存在position_ids, company_ids中。（这里的web安全只是举例，还有信息安全、渗透测试等）

            self.manager(position_ids,company_ids)

if __name__ == '__main__':#程序入口


    ob_main = Lagou()
    name1 = 'web安全'
    name2 = '网络安全'
    name3 = '系统安全'
    name4 = '信息安全'
    name5 = '渗透测试'
    name6 = '病毒分析'
    name7 = '安全工程师'
    name8 = '逆向'
    name9 = '安全专家'

    ob_main.start(name1)
    ob_main.start(name2)
    ob_main.start(name3)
    ob_main.start(name4)
    ob_main.start(name5)
    ob_main.start(name6)
    ob_main.start(name7)
    ob_main.start(name8)
    ob_main.start(name9)


    fopen.close()



















