# -*- coding: utf-8 -*-
import re


import MySQLdb
import json

from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': '192.168.1.120', 'port': 9200}])


conn = MySQLdb.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='12345',
    db='position1',
    charset='utf8'

)
cursor = conn.cursor()


for n in range(2, 3):
    sql = 'select * from category where id = %d' % n

    cursor.execute(sql)

    data = cursor.fetchone()
    print '###########%d################' % n
    print data

    print data[5]
    low = re.search('(.*?)k-', data[5]).group(1)
    high = re.search('-(.*?)k', data[5]).group(1)
    print low
    print high

    dict = {'keyword': data[1], 'url': data[2], 'name': data[3], 'company': data[4], 'salary': data[5], 'low': low,
            'high': high, 'city': data[6], 'experience': data[7], 'education_background': data[8], 'type': data[9],
            'lure': data[10], 'publish_time': data[11], 'description': data[12], 'company_url': data[13],
            'company_official_website': data[14], 'company_field': data[15], 'company_scale': data[16],
            'company_stage_of_development': data[17], 'company_city': data[18], 'company_area': data[19],
            'company_road': data[20], 'company_address': data[21], 'resume_processing_rate': data[22],
            'resume_processing_time': data[23]}
    print dict
    json = json.dumps(dict, indent=4)
    print json

    es.index(index='yoyo', doc_type='position', id=n,
             body=json)

    a = es.get(index='yoyo', doc_type='position', id=n)

    print a

conn.close()
cursor.close()




