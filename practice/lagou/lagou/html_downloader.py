import cookielib
import urllib2


class HtmlDownloader(object):

    def download(self, url):



        if url is None:
            return None
        # cookie = {"Cookie": "#your cookie"}
        #
        # html = requests.get(url, cookies=cookie).content
        # selector = etree.HTML(html)
        # pageNum = (int)(selector.xpath('//input[@name="mp"]')[0].attrib['value'])
        #



        # cj = cookielib.CookieJar()
        # opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        # urllib2.install_opener(opener)
        # response = urllib2.urlopen(url)
        # print response.read()

        #url = 'http://www.lagou.com/zhaopin/webanquan/'
        user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36s'
        headers = {'User-Agent': user_agent}
        try:
            request = urllib2.Request(url, headers=headers)
            response = urllib2.urlopen(request)
            content = response.read().decode('utf-8')
            print content
        except urllib2.URLError, e:
            if hasattr(e, "code"):
                print e.code
            if hasattr(e, "reason"):
                print e.reason

        # if response.getcode() != 200:
        #         return  None

        return  content