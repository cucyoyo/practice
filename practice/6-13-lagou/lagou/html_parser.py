#encoding=utf-8

import re
import urlparse

from bs4 import BeautifulSoup


class HtmlParser(object):

    def parser(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        #print soup

        #new_urls = self._get_new_urls(page_url, soup)

        new_data = self._get_new_data(page_url, soup)
        new_urls = self._get_new_urls(page_url, soup)


        return  new_urls,new_data

    def _get_new_urls(self, root_url, soup):


        new_urls = set()

        links = soup.find_all('a', class_="position_link")
        print links
        for link in links:
            new_url = link['href']
            print new_url
            new_urls.add(new_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}


        #url
        res_data['url'] = page_url
        print res_data['url']

        #公司
        company_node = soup.find('dt',class_ = "clearfix join_tc_icon").find("h1").find("div")
        res_data['company'] = company_node.get_text()

        #职位
        position_node = soup.find('dt', class_="clearfix join_tc_icon").find("h1")
        res_data['position'] = company_node.get_text()


        #薪资
        salary_node = soup.find('span', class_="red")
        res_data['salary'] = salary_node.get_text()

        #要求
        ###不确定
        request_node = soup.find('span', class_="")
        res_data['request'] = request_node.get_text()

        #职位诱惑

        lure_node = soup.find('dd', class_="job_request").find("p")[1]#不确定
        res_data['lure'] = lure_node.get_text()

        # 发布时间

        time_node = soup.find('p', class_="publish_time")
        res_data['time'] = time_node.get_text()

        # 职位描述

        description_node = soup.find('h3', class_="description").find("p")
        res_data['description'] = description_node.get_text()

        # #<div class="lemma-summary" label-module="lemmaSummary">
        # summary_node = soup.find('div', class_="lemma-summary")
        # res_data['summary'] = summary_node.get_text()
        # #print res_data['summary']


        return res_data

#         < dt
#
#         class ="clearfix join_tc_icon" >
#
#         < h1
#         title = "超级手机/电视--WEB安全专家" >
#
#     < em > < / em >
#     < div > 乐视智能云平台招聘 < / div >
#     超级手机 / 电视 - -WEB安全专家
#
# < / h1 >

#
# ####
# < dd
#
#
# class ="job_request" >
#
# < p >
# < span
#
#
# class ="red" > 15k-30k < / span >
#
# < span > 北京 < / span >
# < span > 经验不限 < / span >
# < span > 大专及以上 < / span >
# < span > 全职 < / span >
# < / p >
# < p > 职位诱惑: 期权激励；智能设备云端安全挑战 < / p >
# < p
#
#
# class ="publish_time" > 2016-05-05 & nbsp; 发布于拉勾网 < / p >
#
# < / dd >
#
# ###
# < dd
#
#
# class ="job_bt" >
#
# < h3
#
#
# class ="description" > 职位描述 < / h3 >
#
# < p > < strong > 公司背景： < / strong > < / p >
# < p > 我们是乐视集团控股子公司乐视致新，超级手机、超级电视是我们的旗舰产品。 < / p >
# < p > & nbsp; < / p >
# < p > < strong > 团队背景： < / strong > < / p >
# < p > 我们是智能云平台团队，负责为所有智能终端设备提供云端服务。我们是公司的核心团队，团队核心成员来自百度、小米、360、新浪，参与公司的所有核心业务和产品。压力大、挑战大、机遇更大。 < / p >
# < p > 未来10年是智能终端的时代，我们的目标是打造一个服务智能终端的云平台。 < / p >
# < p > & nbsp; < / p >
# < p > < strong > 团队文化： < / strong > < / p >
# < p > 态度第一，积极主动，人人参与； < / p >
# < p > 做事而不是写代码： 需要你参与到项目的全流程中； < / p >
# < p > 技术至上，用技术来改变生活 < / p >
# < p > < br > < / p >
# < p > < strong > 岗位职责： < / strong > < / p >
# < ol
#
#
# class =" list-paddingleft-2" >
#
# < li > < p > 负责智能云平台的安全规划、安全架构设计和实现 < / p > < / li >
# < li > < p > 负责跟踪业界领先的网络安全技术和解决方案，并结合产品需求推动落地 < / p > < / li >
# < li > < p > 负责云平台的安全测试方案的设计和评定 < / p > < / li >
# < li > < p > 负责云平台产品的安全审核、安全风险评估分析和加固 < / p > < / li >
# < li > < p > 研究各种安全技术，编写和维护用于安全测试的攻击工具、防御工具和分析工具 < / p > < / li >
# < li > < p > 为部门员工提供网络安全意识教育及培训，帮助研发人员提高程序代码的安全性、健壮性 < / p > < p > < br > < / p > < / li >
# < / ol >
# < p > < strong > 岗位要求： < / strong > < / p >
# < ol
#
#
# class =" list-paddingleft-2" >
#
# < li > < p > 深刻理解攻防技术，对最新攻防技术保持关注 < / p > < / li >
# < li > < p > 精通常见云计算平台、系统、网络、WEB应用攻击技术、防御加固 < / p > < / li >
# < li > < p > 有丰富的安全运维、对抗实践经验，有大型WEB系统安全设计、防护实战经验 < / p > < / li >
# < li > < p > 精通攻击的各类技术及方法，对各类WEB应用的弱点有较深入的理解 < / p > < / li >
# < li > < p > 有安全、网络、系统国际认证证书者有限 < br > < / p > < / li >
# < / ol >
# < / dd >