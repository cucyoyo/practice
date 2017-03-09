#-*- coding: utf-8 -*-
import re

class CompanyParser(object):
    # 传入进来的company_ids本身就是非空的，这里相当于一个局部的全局变量，这样就能防止每次执行这个函数的时候company_id被覆盖
    def get_company_ids(self, content,company_ids):
        ids = re.findall('"companyId":(.*?),"', content, re.S)
        for company_id in ids:
            company_ids.add(company_id)
        return company_ids

    def get_url(self,id):
        url = 'http://www.lagou.com/gongsi/searchPosition.json'
        data = 'companyId=%s&positionFirstType=全部&pageNo=1&pageSize=10'%id
        return url, data

    def get_new_data(self,id,n):
        data = 'companyId=%s&positionFirstType=全部&pageNo=%d&pageSize=10'%(id,n)
        return data


