
#encoding=utf-8

import chardet
import sys
class HtmlOutputer(object):
    typeEncode = sys.getfilesystemencoding()  ##系统默认编码

    def __init__(self):
        self.datas = []


    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html', 'w')

        fout.write("<html>")

        fout.write("<body>")
        fout.write("<table>")

        #python默认编码：ascii
        for data in self.datas:
            fout.write("<tr>")

            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['company'].encode('utf-8'))
            fout.write("<td>%s</td>" % data['position'].encode('utf-8'))

            fout.write("<td>%s</td>" % data['salary'].encode('utf-8'))
            fout.write("<td>%s</td>" % data['request'].encode('utf-8'))
            fout.write("<td>%s</td>" % data['lure'].encode('utf-8'))
            fout.write("<td>%s</td>" % data['time'].encode('utf-8'))
            fout.write("<td>%s</td>" % data['description'].encode('utf-8'))
            # infoencode = chardet.detect(data['title']).get('encoding', 'utf-8')  ##通过第3方模块来自动提取网页的编码
            # html = data['title'].decode(infoencode, 'ignore').encode(self.typeEncode)  ##先转换成unicode编码，然后转换系统编码
            # fout.write("<td>%s</td>" % html)
            # infoencode1 = chardet.detect(data['summary']).get('encoding', 'utf-8')  ##通过第3方模块来自动提取网页的编码
            # html1 = data['summary'].decode(infoencode, 'ignore').encode(self.typeEncode)  ##先转换成unicode编码，然后转换系统编码
            # fout.write("<td>%s</td>" % html1)

            fout.write("</tr>")


        fout.write("</table>")
        fout.write("</body>")

        fout.write("</html>")

        fout.close()




# req = urllib2.Request("http://www.163.com/")##这里可以换成http://www.baidu.com,http://www.sohu.com
# content = urllib2.urlopen(req).read()
# typeEncode = sys.getfilesystemencoding()##系统默认编码
# infoencode = chardet.detect(content).get('encoding','utf-8')##通过第3方模块来自动提取网页的编码
# html = content.decode(infoencode,'ignore').encode(typeEncode)##先转换成unicode编码，然后转换系统编码输出
# print html