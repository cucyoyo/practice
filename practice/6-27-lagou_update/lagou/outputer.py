#-*- coding: utf-8 -*-
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class Outputer(object):

    def outputer(self, res_data, cont, fopen, n, m):


        fopen.write('###############%d.#################\n ' % cont)

        print 'url', res_data['url']
        fopen.write('%s' % res_data['url'])
        fopen.write('\n')

        # print 'company', res_data['company']
        fopen.write('%s' % res_data['company'])
        fopen.write('\n')

        # print 'position', res_data['position']
        fopen.write('%s' % res_data['position'])
        fopen.write('\n')

        print 'salary', res_data['salary']
        fopen.write('%s' % res_data['salary'])
        fopen.write('\n')
        #data_set.add(res_data['salary'])

        for each in range(2, n + 1):
            print '%d'%each, res_data['request%d'%each]
            fopen.write('%s' % res_data['request%d'%each])
            fopen.write('\n')
            #data_set.add(res_data['request%d'%each])

        print 'lure', res_data['lure']
        fopen.write('%s' % res_data['lure'])
        fopen.write('\n')
        #data_set.add(res_data['lure'])

        print 'time', res_data['time']
        fopen.write('%s' % res_data['time'])
        fopen.write('\n')
        #data_set.add(res_data['time'])

        for each in range(1, m+1):
            print '%d' % each, res_data['description%d' % each]
            fopen.write('%s' % res_data['description%d' % each])
            fopen.write('\n')
            fopen.write('\n')
            #data_set.add(res_data['description%d' % each])


        # 尝试使用csv格式输出，暂未成功
        # filename+='.csv'
        # writer = csv.writer(file(filename, 'wb'))#创建一个名为sessdefaults的csv文件
        # writer.writerow([key, value])#指出字段名
        # myIter = dictname.iteritems()
        # while True :
        #     try :
        #         item_list = list(myIter.next())#将键值对元组转换为列表
        #         writer.writerow(item_list)#分行写入
        #         #print repr(item_list)
        #     except StopIteration :
        #         break
        # print data_set
        #
        # csvFile = open("test.csv",'w+')
        # try:
        #     writer = csv.writer(csvFile)
        #     writer.writerow(data_set)
        # finally:
        #     csvFile.close()