#-*- coding: utf-8 -*-
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class Outputer(object):

    def outputer(self, res_data, cont, conn, cursor):
        print '###########%d##############' % cont
        # print res_data['url'],res_data['position'],res_data['company_url'],res_data['company'],res_data['salary'],res_data['request2'],res_data['request3'],res_data['request4'],res_data['request5'],res_data['lure'],res_data['time'],res_data['description']
        # print cont, res_data['keyword'], res_data['url'], res_data['position'], res_data['company'], res_data['salary'], \
        # res_data['request2'], res_data['request3'], res_data['request4'], res_data['request5'], res_data['lure'], \
        # res_data['time'], res_data['description'], res_data['company_url'], res_data['company_official_website'], \
        # res_data['company_field'], res_data['company_scale'], res_data['company_stage_of_development'], res_data[
        #     'company_city'], res_data['company_area'], res_data['company_road'], res_data['company_address'], res_data[
        #     'resume_processing_rate'], res_data['resume_processing_time']

        # sql = "INSERT INTO category(id,position_url,position_name, company_url,company_name,salary,city,experience,education_background,type,lure,publish_time,description) VALUES('%s', '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (cont, res_data['url'], res_data['position'], res_data['company_url'], res_data['company'], res_data['salary'], res_data['request2'],res_data['request3'], res_data['request4'], res_data['request5'], res_data['lure'], res_data['time'],res_data['description'])
        # 24
        sql = "INSERT INTO category(id,keyword,position_url,position_name, company_name,salary,city,experience,education_background,type,lure,publish_time,description,company_url,company_official_website,company_field, company_scale, company_stage_of_development, company_city, company_area, company_road, company_address,resume_processing_rate,resume_processing_time) VALUES('%s', '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (cont, res_data['keyword'], res_data['url'], res_data['position'], res_data['company'], res_data['salary'],res_data['request2'], res_data['request3'], res_data['request4'], res_data['request5'], res_data['lure'],res_data['time'], res_data['description'], res_data['company_url'], res_data['company_official_website'],res_data['company_field'], res_data['company_scale'], res_data['company_stage_of_development'],res_data['company_city'], res_data['company_area'], res_data['company_road'], res_data['company_address'],res_data['resume_processing_rate'], res_data['resume_processing_time'])
        try:
            cursor.execute(sql)
            conn.commit()
        except Exception as e:
            print e
            conn.rollback()


