#-*- coding: utf-8 -*-
import json
import re
from bs4 import BeautifulSoup

from NICCS import downloader

class Storage(object):

    def __init__(self):#初始化
        self.downloader = downloader.Downloader()




    def store(self,url):#此函数得出root_url的页码并根据页数开始循环抓取
        start_url = url + '/training/framework/categories'#初始界面：category的界面，里面是category条目
        category_content = self.downloader.get_content(start_url)

        print 'storing category_content.......'

        f_category = open('category.txt','w')
        f_category.write(category_content)
        f_category.close()

        print 'done:category_content stored!'

        soup = BeautifulSoup(category_content, "lxml")
        categories = soup.find_all('div', class_ = "category-item clearfix clearfix")
        a = 1
        for each in categories:
            if a <= 3:
                a = a + 1
                continue
            else:
                category_url_half = each.find_all('a')[1]['href'] #category页面里的前往specialty areas的url
                category_url = url + category_url_half
                category_name = each.find_all('a')[1].get_text()
                sp_content = self.downloader.get_content(category_url)# 从category条目的url进入的是specialty areas的页面，得到的是sp_content

                print 'storing %s :sp_content........'%category_name

                f_sp = open('sp_content(%s).txt'%category_name, 'w')
                f_sp.write(sp_content)
                f_sp.close()
                print 'done: %s :sp_content is stored!' % category_name

                soup = BeautifulSoup(sp_content, "lxml")
                sps = soup.find_all('div', class_ = "specialty-item clearfix clearfix")# 从sp_content的页面里取出的是specialty area的条目
                for each in sps:
                    sp_url_half = each.find('a')['href'] #specialty areas页面的里的前往related jobs页面的url
                    sp_url = url + sp_url_half
                    sp_name = each.find('a').get_text()
                    job_content = self.downloader.get_content(sp_url)#sp_url指向的是job的页面，这里得到的是job页面的内容

                    print 'storing %s :job_content: ......'%sp_name

                    f_job = open('job_content(%s).txt' % sp_name, 'w')
                    f_job.write(job_content)
                    f_job.close()

                    print 'done: %s :job_content is stored!' % sp_name

                    soup = BeautifulSoup(job_content, "lxml")
                    course_url_half = soup.find('a', class_ = "courses-btn")['href']  # 在job_content里取出课程的url
                    course_url = url + course_url_half

                    course_content = self.downloader.get_content(course_url)#课程页面的内容

                    soup = BeautifulSoup(course_content,"lxml")

                    print 'storing specialty area :%s :course_content.......' % sp_name
                    f_course = open('course_content(%s).txt' % sp_name, 'a')  # 用追加存储的方式打开文件
                    f_course.write(course_content)  # 写入第一页

                    last_tag = soup.find('li', class_="pager-last last")

                    if last_tag == None:#可能只有一页
                        print '只有一页'
                    else:

                        last_page = str(last_tag.find('a'))  # 取出跳转到最后一页的按钮的a标签,这里面可以提取出最后一页的页码
                        page = int(re.findall(';page=(.*?)"> Last', last_page)[0])# 总的页数

                        for n in range(1, page + 1):#追加写入后面的页，即该specialty area的所有页面的课程都存在这一个文件里
                            mid_url = course_url + '&specialty[0]=11810&&&&items_per_page=20&page=%d'%n
                            print mid_url

                            mid_content = self.downloader.get_content(mid_url)
                            print mid_content
                            f_course.write(mid_content)

                        f_course.close()

                        print 'done: specialty area :%s :course_content is stored!' % sp_name




        # print content


if __name__ == '__main__':#程序入口

    url = 'https://niccs.us-cert.gov'
    ob_main = Storage()
    ob_main.store(url)






