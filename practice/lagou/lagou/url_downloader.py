import re
import urllib2

from bs4 import BeautifulSoup
#encoding=utf-8


class UrlDownloader(object):

    def _get_new_urls(self, root_url):

        # html_cont = self.downloader.download(new_url)
        if root_url is None:
            return None
        response = urllib2.urlopen(root_url)

        if response.getcode() != 200:
            return None

        html_cont = response.read()
        if html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        print soup


        new_urls = set()



        # atry = soup.find('span',class_="format-time")
        # print atry

        #< div class ="s_position_list " id="s_position_list" >
        #<ul class="item_con_list" style="display: block;">
        # <a class="position_link" href="http://www.lagou.com/jobs/1940670.html" target="_blank" data-index="1" data-lg-tj-id="8E00" data-lg-tj-no="...</a>

        a = soup.findAll("a",{"class":"position_link"})
        print links
        for link in links:
            new_url = link['href']
            print new_url
            new_urls.add(new_url)
        return new_urls