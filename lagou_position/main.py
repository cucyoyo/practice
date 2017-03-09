#-*- coding: utf-8 -*-
import json
import re
import MySQLdb


from lagou import url_manager,html_downloader,position_parser,html_downloader,outputer

class Lagou(object):

    def __init__(self):#初始化

        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.position_parser = position_parser.PositionParser()
        self.outputer = outputer.Outputer()

    def manage(self,name):

        # 直接从文件中读取网页源码
        fopen = open('/home/sj/PycharmProjects/lagou/lagou/%s.txt'%name,'r')
        content = fopen.read()
        fopen.close()

        # 这里尝试将json数据转换为python的数据结构然后结构化抓取，如下。但是鉴于同样在这个场景下，用一句正则表达式即可代替下面这些，所以选择了正则表达式，实质上这两种方法都没有问题。
        # data = json.loads(content)
        # pagesize = data["content"]["pageSize"]
        # for n in range(0, int(pagesize)):
        #     position_ids.append(data["content"]["positionResult"]["result"][n]["positionId"])

        position_ids = re.findall('"positionId":(.*?),"', content, re.S)

        cont = 1
        for position_id in position_ids:

            url = "http://www.lagou.com/jobs/%s.html" % position_id
            print position_id
            # 从文件中读取相应职位的网页源码
            f_positon = open('/home/sj/PycharmProjects/lagou/lagou/%s-%s.txt' % (name, position_id), 'r')
            content = f_positon.read()
            f_positon.close()

            if content == None:
                print '职位信息读取失败！url:%s'%url
            else:
                data = self.position_parser.parser(url, content, name)# 解析，返回解析好的数据data
                if data == None:
                    print '职位解析失败！url:%s'%url
                else:
                    # 链接数据库，进行数据存储
                    conn = MySQLdb.connect(
                        host='127.0.0.1',
                        user='root',
                        passwd='12345',
                        port=3306,
                        db='position1',
                        charset='utf8'
                    )
                    cursor = conn.cursor()

                    self.outputer.outputer(data, cont, conn, cursor)

                    cont = cont + 1
                    cursor.close()
                    conn.close()

if __name__ == '__main__':#程序入口

    ob_main = Lagou()

    with open('configuration.txt', 'r') as f:
        for line in f:
            name = map(str, line.split(','))#将配置文件内的信息输入到list结构中

    for n in range(0,len(name)):
        print name[n]
        ob_main.manage(name[n])





