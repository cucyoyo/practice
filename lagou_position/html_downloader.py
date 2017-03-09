
#-*- coding: utf-8 -*-
import urllib2
import urllib
from cookielib import CookieJar
import httplib
from socket import error as SocketError
import errno

class HtmlDownloader(object):



    def get_content(self, root_url, data):


        httplib.HTTPConnection._http_vsn = 10
        httplib.HTTPConnection._http_vsn_str = 'HTTP/1.0'
        #代理服务器，解决频繁访问、要求输入验证码的问题
        proxy_handler = urllib2.ProxyHandler({"http": '27.46.37.74:9797'})
        # cookie登陆信息
        cj = CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        #,proxy_handler

        try:
            response = opener.open(root_url, data, timeout=60)

        except urllib2.HTTPError, e:
            print e.code
            return None
        except urllib2.URLError, e:
            print e.reason
            return None
        except SocketError as e:
            if e.errno != errno.ECONNRESET:
                raise  # Not error we are looking for
            pass  # Handle error here.
            return None

        else:
            print "OK"
            return response.read()



