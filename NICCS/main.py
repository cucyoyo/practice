
#-*- coding: utf-8 -*-
import MySQLdb
from bs4 import BeautifulSoup


class Spider(object):

    def cut(self,content):# 去掉字段中多余的空格和回车
        content = content.strip(' ').strip('\n').strip(' ').strip('\t').strip('\r')
        return content

    def manager(self,url):

        # 链接数据库
        f = open('password.txt', 'r')
        password = f.read()
        f.close()
        conn = MySQLdb.connect(
            host='127.0.0.1',
            user='root',
            passwd='%s' % password,
            port=3306,
            db='NICCS',
            charset='utf8'
        )
        cursor = conn.cursor()
        ca_id = 0
        sp_id = 0
        job_id = 0
        task_id = 0
        ksa_id = 0
        course_id = 0
        method_id = 0

        f_category = open('category.txt','r')
        category_content = f_category.read()
        f_category.close()

        ca_soup = BeautifulSoup(category_content, "lxml")
        categories = ca_soup.find_all('div', class_="category-item clearfix clearfix")

        for category in categories:

            ca_id = ca_id + 1

            category_url_half = category.find_all('a')[1]['href']  # category页面里的前往specialty areas的url
            category_url = url + category_url_half
            category_name = str(category.find_all('a')[1].get_text())
            category_des = str(category.find('div', class_ = "field-content").find('p').get_text()).replace("'","''")#将描述里面的单引号变成两个单引号，否则存入过程将会出错
            print u'正将category(%s)条目的信息存入数据库...' % category_name
            sql = "INSERT INTO tb_categories(id, name, url, des) VALUES('%d', '%s', '%s', '%s')" % (ca_id, category_name, category_url, category_des)

            try:
                cursor.execute(sql)
                conn.commit()
                print u'存储成功：category(%s)条目的信息存入数据库...' % category_name
            except Exception as e:
                print u'category(%s)条目的信息存储失败：%s,接下来回滚' % (category_name,e)
                conn.rollback()

            f_sp = open('sp_content(%s).txt'%category_name,'r')
            sp_content = f_sp.read()
            f_sp.close()

            sp_soup = BeautifulSoup(sp_content, "lxml")
            sps = sp_soup.find_all('div',
                                class_="specialty-item clearfix clearfix")  # 从sp_content的页面里取出的是specialty area的条目
            for sp in sps:
                sp_id = sp_id + 1

                sp_url_half = sp.find('a')['href']  # specialty areas页面的里的前往related jobs页面的url
                sp_url = url + sp_url_half
                sp_name = sp.find('a').get_text()
                sp_des = sp.find('div', class_ = "field-content").find('p').get_text().replace("'","''")
                # sp_des = sp_des.replace('\n','')
                # sp_des = sp_des.replace(' ','')
                sp_des = self.cut(sp_des)

                print u'正将category.sp(%s.%s)条目的信息存入数据库...' % (category_name,sp_name)
                sql = "INSERT INTO tb_sp(id, ca_id, name, url, des) VALUES('%d', '%d', '%s', '%s', '%s')"%(sp_id, ca_id, sp_name, sp_url, sp_des)
                try:
                    cursor.execute(sql)
                    conn.commit()
                    print u'存储成功：category.sp(%s.%s)条目的信息存入数据库...' % (category_name,sp_name)
                except Exception as e:
                    print u'存储失败category.sp(%s.%s)条目的信息：%s,接下来回滚' % (category_name,sp_name, e)
                    conn.rollback()

                f_job = open('job_content(%s).txt' % sp_name, 'r')
                job_content = f_job.read()
                f_job.close()

                job_soup = BeautifulSoup(job_content, "lxml")

                #Related Jobs Titles

                if job_soup.find_all('div', class_="item-list"):# 存在没有工作名称的情况
                    jobs = job_soup.find_all('div', class_="item-list")[1].find('ul').find_all('li')
                    for job in jobs:
                        job_id = job_id +1
                        job_name = job.get_text().replace("'","''")

                        print u'正将category.sp.job(%s.%s.%s)条目的信息存入数据库...' % (category_name, sp_name, job_name)
                        sql = "INSERT INTO tb_jobs(id, sp_id, job) VALUES('%d', '%d', '%s')"%(job_id, sp_id, job_name)
                        try:
                            cursor.execute(sql)
                            conn.commit()
                            print u'存储成功：category.sp.job(%s.%s.%s)条目的信息存入数据库...' % (category_name, sp_name, job_name)
                        except Exception as e:
                            print u'存储失败:category.sp.job(%s.%s.%s)条目的信息：%s,接下来回滚' % (category_name, sp_name,job_name, e)
                            conn.rollback()

                    #Tasks
                    tasks = job_soup.find_all('div', class_="item-list")[2].find('ul').find_all('li')
                    # tasks = soup.find('div', class_ = "view view-explore-the-framework view-id-explore_the_framework view-display-id-sa_detail_task view-dom-id-7312af63c50d6f22fac5c092198f5f0c").find('div', class_ = "view-content").find('div', class_ = "item-list").find('ul').find_all('li')
                    for task in tasks:
                        task_id = task_id + 1
                        task_name = task.get_text().replace("'","''")
                        task_name = self.cut(task_name)
                        # task_name = task_name.strip('\n')
                        # task_name = task_name.strip(' ')
                        # task_name = task_name.strip('\t')

                        print u'正将category.sp.task(%s.%s.%s)条目的信息存入数据库...' % (category_name, sp_name, task_name)
                        sql = "INSERT INTO tb_tasks(id, sp_id, task) VALUES('%d', '%d', '%s')" % (task_id, sp_id, task_name)
                        try:
                            cursor.execute(sql)
                            conn.commit()
                            print u'存储成功：category.sp.task(%s.%s.%s)条目的信息存入数据库...' % (category_name, sp_name, task_name)
                        except Exception as e:
                            print u'存储失败:category.sp.task(%s.%s.%s)条目的信息：%s,接下来回滚' % (category_name, sp_name, task_name, e)
                            conn.rollback()

                    #KSAs
                    ksas = job_soup.find_all('div', class_="item-list")[3].find('ul').find_all('li')
                    for ksa in ksas:
                        ksa_id = ksa_id + 1

                        ksa_content = ksa.get_text().replace("'","''")
                        ksa_content = self.cut(ksa_content)
                        # ksa_content = ksa_content.strip('\n')
                        # ksa_content = ksa_content.strip(' ')
                        # ksa_content = ksa_content.strip('\t')

                        print u'正将category.sp.ksa(%s.%s.%s)条目的信息存入数据库...' % (category_name, sp_name, ksa_content)
                        sql = "INSERT INTO tb_ksas(id, sp_id, ksa) VALUES('%d', '%d', '%s')" % (ksa_id, sp_id, ksa_content)
                        try:
                            cursor.execute(sql)
                            conn.commit()
                            print u'存储成功：category.sp.ksa(%s.%s.%s)条目的信息存入数据库...' % (category_name, sp_name, ksa_content)
                        except Exception as e:
                            print u'存储失败:category.sp.ksa(%s.%s.%s)条目的信息：%s,接下来回滚' % (category_name, sp_name, ksa_content, e)
                            conn.rollback()

                    ############

                f_course = open('course_content(%s).txt' % sp_name, 'r')
                course_content = f_course.read()
                f_course.close()

                course_soup = BeautifulSoup(course_content, "lxml")

                tbodies = course_soup.find_all('tbody')
                for tbody in tbodies:
                    trs = tbody.find_all('tr')
                    for tr in trs:
                        course_id = course_id +1
                        course_name = tr.find('td', class_ = "views-field views-field-title").find('a').get_text()
                        name_url = url + tr.find('td', class_ = "views-field views-field-title").find('a')['href']
                        course_provider = tr.find('td', class_ = "views-field views-field-field-tc-provider-name").find('a').get_text()
                        provider_url = url + tr.find('td', class_ = "views-field views-field-field-tc-provider-name").find('a')['href']
                        location = tr.find('td', class_ = "views-field views-field-field-tc-locations").get_text()
                        # location = location.strip(' ')
                        # location = location.strip('\n')
                        # location = location.strip('\t')
                        location = self.cut(location)

                        print u'正将category.sp.course(%s.%s.%s)条目的信息存入数据库...' % (category_name, sp_name, course_name)
                        sql = "INSERT INTO tb_courses(id, sp_id, name, name_url, provider, provider_url, location) VALUES('%d', '%d', '%s', '%s', '%s', '%s', '%s')"%(course_id, sp_id, course_name, name_url, course_provider, provider_url, location)
                        try:
                            cursor.execute(sql)
                            conn.commit()
                            print u'存储成功：category.sp.course(%s.%s.%s)条目的信息存入数据库...' % (category_name, sp_name, course_name)
                        except Exception as e:
                            print u'存储失败:category.sp.course(%s.%s.%s)条目的信息：%s,接下来回滚' % (
                            category_name, sp_name, course_name, e)
                            conn.rollback()

                        methods = tr.find('td', class_ = "views-field views-field-field-tc-delivery-method").get_text()# 取出的是带逗号的str类型
                        methods = methods.replace(' ','')# 去掉字符串中的空格

                        # methods = methods.strip('\n')
                        # methods = methods.strip('\t')
                        methods = methods.split(',')#将str类型转化为list类型
                        new_methods = []# 去重
                        for method in methods:
                            if method not in new_methods:
                                new_methods.append(method)
                        for method in new_methods:#实现了分词
                            method_id = method_id + 1
                            method = self.cut(method)

                            print u'正将category.sp.course.method(%s.%s.%s.%s)条目的信息存入数据库...' % (category_name, sp_name, course_name, method)
                            sql = "INSERT INTO tb_course_dm(id, course_id, method) VALUES('%d', '%d', '%s')" % (method_id, course_id, method)
                            try:
                                cursor.execute(sql)
                                conn.commit()
                                print u'存储成功：category.sp.course.method(%s.%s.%s.%s)条目的信息存入数据库...' % (
                                category_name, sp_name, course_name, method)
                            except Exception as e:
                                print u'存储失败:category.sp.course.method(%s.%s.%s.%s)条目的信息：%s,接下来回滚' % (
                                    category_name, sp_name, course_name, method, e)
                                conn.rollback()

        cursor.close()
        conn.close()


if __name__ == '__main__':
    url = 'https://niccs.us-cert.gov'
    ob_main = Spider()
    ob_main.manager(url)