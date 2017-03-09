#encoding=utf-8
import urllib2

from bs4 import BeautifulSoup

from lagou import url_manager,html_parser,html_downloader,html_outputer


class SpiderMian(object):

    def __init__(self):
        #self.geturl = url_downloader.UrlDownloader()
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()




    def craw(self, root_url):


        html_cont = self.downloader.download(root_url)
        # print html_cont
        #cont = 1
        print 3
        new_urls = self.parser.parser(root_url,html_cont)[0]

        print new_urls
        print 4

        self.urls.add_new_urls(new_urls)

        cont = 1
        while self.urls.has_new_url():
            try:

                new_url = self.urls.get_new_url()

                print 'craw %d : %s'%(cont, new_url)

                html_cont = self.downloader.download(new_url)

                new_data = self.parser.parser(new_url, html_cont)

                #self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                # if cont == 20:
                #     break
                cont = cont + 1
            except:
                print 'craw failed'


        self.outputer.output_html()


if __name__ == "__main__":
    root_url = "http://www.lagou.com/zhaopin/webanquan/"
    print 1
    obj_spider = SpiderMian()
    print 2
    obj_spider.craw(root_url)