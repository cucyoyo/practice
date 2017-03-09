#-*- coding: utf-8 -*-
import re

from bs4 import BeautifulSoup


class PositionParser(object):
    # 传入进来的position_ids本身就是非空的，这里相当于一个局部的全局变量，这样就能防止每次执行这个函数的时候position_id被覆盖
    def get_position_ids(self, content,position_ids):

        ids = re.findall('"positionId":(.*?),"', content, re.S)

        for position_id in ids:
            position_ids.add(position_id)

        return position_ids

    def parser(self, url,content):#从职位页面（静态）提取有用信息
        res_data = {}
        soup = BeautifulSoup(content, "lxml")

        if soup == None:
            return None,0,0
        else:

            res_data['url'] = url

            # 公司
            company_node = soup.find('dt', class_="clearfix join_tc_icon").find("div")
            res_data['company'] = company_node.get_text().encode('utf-8')

            # 职位
            position_node = soup.find_all('h2')[1]
            res_data['position'] = position_node.get_text().encode('utf-8')

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