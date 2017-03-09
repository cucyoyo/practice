#-*- coding: utf-8 -*-
import json
import re
from bs4 import BeautifulSoup

from lagou import url_manager,html_downloader,position_parser,html_downloader,outputer

class Storage(object):

    def __init__(self):#初始化

        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()

        self.position_parser = position_parser.PositionParser()
        self.outputer = outputer.Outputer()

    def store(self,name):#此函数得出root_url的页码并根据页数开始循环抓取
        print 1
        url = 'http://www.lagou.com/jobs/list_%s?px=default&city=全国'%name#root_url（total_page信息从root_url中提取）
        content = self.downloader.get_content(url,data = None)
        print 2
        if content == None:
            print '%s爬取失败'%url
        else:
            soup = BeautifulSoup(content, "lxml")
            # print soup
            # print type(soup.find('span', class_="span totalNum"))

            if soup.find('span', class_ = "span totalNum") == None:
                print '%s爬取失败'%url
            else:
                page = soup.find('span', class_ = "span totalNum").get_text()#提取页码信息

                # 由于职位信息是动态加载的，直接从上面url无法得到我们所需的职位url，下面root_url是经过分析以后得到的动态加载时的ｕｒｌ
                # 分析结果：url:'http://www.lagou.com/jobs/positionAjax.json?px=default&needAddtionalResult=false'
                # --data 'first=true&pn=1&kd=web安全'
                root_url = 'http://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
                print 'is storing : %s'%name
                fopen = open('%s.txt'%name, 'w')

                for n in range(1,int(page)+1):
                # for n in range(1, 2):

                    data = 'first=true&pn=%d&kd=%s'%(n,name)#获取动态信息对应url的data
                    content = self.downloader.get_content(root_url,data)

                    if content == None:
                        print 'url:%s,data:%s爬取失败' % (root_url, data)
                    else:

                        fopen.write('%s'%content)
                        fopen.write('\n')
                fopen.close()
                print 'is stored:%s' % root_url

                self.store_position(name)

    def store_position(self, name):

        fopen = open('%s.txt' % name, 'r')
        content = fopen.read()
        fopen.close()

        position_ids = re.findall('"positionId":(.*?),"', content, re.S)
        print '正在存储%s的所有职位'%name
        for position_id in position_ids:
            print position_id
            # http://www.lagou.com/jobs/709515.html
            url = "http://www.lagou.com/jobs/%s.html" % position_id
            content = self.downloader.get_content(url, data=None)
            f_positon = open('%s-%s.txt'%(name,position_id),'w')
            f_positon.write(content)
            f_positon.close()
        print '%s的所有职位存储成功'%name

if __name__ == '__main__':#程序入口
    ob_main = Storage()
    with open('configuration.txt', 'r') as f:
        for line in f:
            name = map(str, line.split(','))  # 将配置文件内的信息输入到list结构中

    for n in range(0, len(name)):
    # for n in range(0, 1):
        print name[n]
        ob_main.store(name[n])






