
#-*- coding: utf-8 -*-
import urllib2
import urllib
from cookielib import CookieJar
import httplib


class HtmlDownloader(object):

    def get_content(self, root_url,data):

        httplib.HTTPConnection._http_vsn = 10
        httplib.HTTPConnection._http_vsn_str = 'HTTP/1.0'

        cj = CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

        # req = urllib2.Request(root_url)
        try:
            response = opener.open(root_url, data, timeout=60)

        except urllib2.HTTPError, e:
            print e.code
            return None
        except urllib2.URLError, e:
            print e.reason
            return None
        else:
            print "OK"
            return response.read()



