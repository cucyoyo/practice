#-*- coding: utf-8 -*-
import pickle

from bs4 import BeautifulSoup


class PositionParser(object):


    def parser(self, url, content, name):#从职位页面（静态）提取有用信息
        res_data = {}
        soup = BeautifulSoup(content, "lxml")

        if soup == None:
            return None,0,0
        else:
            # 搜索关键字
            res_data['keyword'] = name

            # 职位url
            res_data['url'] = url

            # 职位名称
            position_node = soup.find_all('h2')[1]
            res_data['position'] = position_node.get_text().encode('utf-8')

            # 公司
            com = soup.find('dt', class_="clearfix join_tc_icon")
            if com != None:
                company_node = com.find("div")
                res_data['company'] = company_node.get_text().encode('utf-8')
            else:
                res_data['company'] = 'error'

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
            description_collect = ''
            for description in descriptions:
                m = m + 1
                description_collect = description_collect + description.get_text().encode('utf-8') + '\n'
            res_data['description'] = description_collect

            # 公司url
            res_data['company_url'] = soup.find('dl', class_="job_company").find('a')['href']

            # 公司官方主页
            res_data['company_official_website'] = soup.find('ul', class_ = "c_feature").find('a')['href']

            # 公司领域
            company_field_node = soup.find('ul', class_="c_feature").find_all('li')[0]
            res_data['company_field'] = company_field_node.get_text().encode('utf-8').strip()

            #　公司规模
            company_scale_node = soup.find('ul', class_="c_feature").find_all('li')[1]
            res_data['company_scale'] = company_scale_node.get_text().encode('utf-8').strip()

            # 公司发展阶段
            development_stage_node = soup.find_all('ul', class_="c_feature")[1].find('li')
            res_data['company_stage_of_development'] = development_stage_node.get_text().encode('utf-8').strip()

            # 公司详细地址
            company_addr_node = soup.find('div', class_ ="work_addr")
            if company_addr_node == None:
                res_data['company_city'] = ''
                res_data['company_area'] = ''
                res_data['company_road'] = ''
                res_data['company_address'] = ''
            else:
                a = company_addr_node.find_all('a')
                len_ = len(a)

                if len_ == 0:
                    res_data['company_city'] = ''
                    res_data['company_area'] = ''
                    res_data['company_road'] = ''
                elif len_ == 1:
                    res_data['company_city'] = a[0].get_text().encode('utf-8')
                    res_data['company_area'] = ''
                    res_data['company_road'] = ''

                elif len_ == 2:
                    res_data['company_city'] = a[0].get_text().encode('utf-8')
                    res_data['company_area'] = a[1].get_text().encode('utf-8')
                    res_data['company_road'] = ''

                else:
                    res_data['company_city'] = a[0].get_text().encode('utf-8')
                    res_data['company_area'] = a[1].get_text().encode('utf-8')
                    res_data['company_road'] = a[2].get_text().encode('utf-8')

                res_data['company_address'] = company_addr_node.get_text().encode('utf-8').strip().replace(' ', '').replace('\n','')

            # 简历处理
            resume_processing_node = soup.find('div', class_="publisher_data").find_all('span', class_ = "data")
            res_data['resume_processing_rate'] = resume_processing_node[0].get_text().encode('utf-8')
            res_data['resume_processing_time'] = resume_processing_node[1].get_text().encode('utf-8')



            return res_data