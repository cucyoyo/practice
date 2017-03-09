#-*- coding: utf-8 -*-
import urllib2

class Downloader(object):
    def get_content(self, url):


        # user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36'

        # headers = {'User-Agent': user_agent}

        try:

            request = urllib2.Request(url)
            request.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36')
            request.add_header('Cookie',
                               'SSESSe0bb5b196cac32397be7eedf6428aadb=L7Cb4_G2RP4gTuJjOTGkmB8UhuJNeMyJAMYGxnuCfOg; has_js=1; _ga=GA1.2.16513484.1469613813')
            response = urllib2.urlopen(request)
        except urllib2.HTTPError, e:
            print e.code
            return None
        except urllib2.URLError, e:
            print e.reason
            return None
        else:

            content = response.read()
            return content
