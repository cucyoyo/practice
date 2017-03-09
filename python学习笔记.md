# python学习笔记

标签（空格分隔）： 未分类

---
[参考源地址](http://python.jobbole.com/81339/)

目录

[TOC]



# 1.urllib基础

```
import urllib2
response = urllib2.urlopen("http://www.baidu.com")
print response.read()
```
运行结果是完全一样的，只不过中间多了一个request对象，推荐大家这么写，因为在构建请求时还需要加入好多内容，通过构建一个request，服务器响应请求得到应答，这样显得逻辑上清晰明确。
```
import urllib2
 
request = urllib2.Request("http://www.baidu.com")
response = urllib2.urlopen(request)
print response.read()
```

## post & get

数据传送分为POST和GET两种方式，两种方式有什么区别呢？

最重要的区别是GET方式是直接以链接形式访问，链接中包含了所有的参数，当然如果包含了密码的话是一种不安全的选择，不过你可以直观地看到自己提交了什么内容。POST则不会在网址上显示所有的参数，不过如果你想直接查看提交了什么就不太方便了，大家可以酌情选择。

### post

```
import urllib
import urllib2
 
values = {"username":"1016903103@qq.com","password":"XXXX"}
data = urllib.urlencode(values) 
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib2.Request(url,data)
response = urllib2.urlopen(request)
print response.read()
```
value字典等价写法

```
import urllib
import urllib2
 
values = {}
values['username'] = "1016903103@qq.com"
values['password'] = "XXXX"
data = urllib.urlencode(values) 
url = "http://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib2.Request(url,data)
response = urllib2.urlopen(request)
print response.read()
```

### get

```
import urllib
import urllib2
 
values={}
values['username'] = "1016903103@qq.com"
values['password']="XXXX"
data = urllib.urlencode(values) 
url = "http://passport.csdn.net/account/login"
geturl = url + "?"+data
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print response.read()
```

# 2.urllib高级

## 2.1 Headers

agent就是请求的身份，如果没有写入请求身份，那么服务器不一定会响应，所以可以在headers中设置agent

```
import urllib  
import urllib2  
 
url = 'http://www.server.com/login'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  
values = {'username' : 'cqc',  'password' : 'XXXX' }  
headers = { 'User-Agent' : user_agent }  
data = urllib.urlencode(values)  
request = urllib2.Request(url, data, headers)  
response = urllib2.urlopen(request)  
page = response.read()
```

另外，我们还有对付”反盗链”的方式，对付防盗链，服务器会识别headers中的referer是不是它自己，如果不是，有的服务器不会响应，所以我们还可以在headers中加入referer

```
headers = { 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  ,
                        'Referer':'http://www.zhihu.com/articles' }
```

## 2.2 代理服务器  Proxy

urllib2 默认会使用环境变量 http_proxy 来设置 HTTP Proxy。假如一个网站它会检测某一段时间某个IP 的访问次数，如果访问次数过多，它会禁止你的访问。所以你可以设置一些代理服务器来帮助你做工作，每隔一段时间换一个代理，网站君都不知道是谁在捣鬼了，这酸爽！

```
import urllib2
enable_proxy = True
proxy_handler = urllib2.ProxyHandler({"http" : 'http://some-proxy.com:8080'})
null_proxy_handler = urllib2.ProxyHandler({})
if enable_proxy:
    opener = urllib2.build_opener(proxy_handler)
else:
    opener = urllib2.build_opener(null_proxy_handler)
urllib2.install_opener(opener)
```
## 2.3 Timeout

```
import urllib2
response = urllib2.urlopen('http://www.baidu.com', timeout=10)
```

```
import urllib2
response = urllib2.urlopen('http://www.baidu.com',data, 10)
```

下面两种方法较少见，用到的时候具体查看源地址
## 2.4 使用 HTTP 的 PUT 和 DELETE 方法
```
import urllib2
request = urllib2.Request(uri, data=data)
request.get_method = lambda: 'PUT' # or 'DELETE'
response = urllib2.urlopen(request)
```
## 2.5使用DebugLog
```
import urllib2
httpHandler = urllib2.HTTPHandler(debuglevel=1)
httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
opener = urllib2.build_opener(httpHandler, httpsHandler)
urllib2.install_opener(opener)
response = urllib2.urlopen('http://www.baidu.com')
```
# 3.异常处理 URLError

## 3.1.URLError
```
import urllib2
 
requset = urllib2.Request('http://www.xxxxx.com')
try:
    urllib2.urlopen(requset)
except urllib2.URLError, e:
    print e.reason
```
```
[Errno 11004] getaddrinfo failed
```

## 3.2.HTTPError
HTTPError是URLError的子类，在你利用urlopen方法发出一个请求时，服务器上都会对应一个应答对象response，其中它包含一个数字”状态码”(说明见文档末尾)。举个例子，假如response是一个”重定向”，需定位到别的地址获取文档，urllib2将对此进行处理。

```
import urllib2
 
req = urllib2.Request('http://blog.csdn.net/cqcre')
try:
    urllib2.urlopen(req)
except urllib2.HTTPError, e:
    print e.code
    print e.reason
```

```
403
Forbidden
```
我们知道，**HTTPError的父类是URLError**，根据编程经验，父类的异常应当写到子类异常的后面，如果子类捕获不到，那么可以捕获父类的异常，所以上述的代码可以这么改写
```
import urllib2
 
req = urllib2.Request('http://blog.csdn.net/cqcre')
try:
    urllib2.urlopen(req)
except urllib2.HTTPError, e:
    print e.code
except urllib2.URLError, e:
    print e.reason
else:
    print "OK"
```

另外还可以加入 hasattr属性提前对属性进行判断，代码改写如下
```
import urllib2
 
req = urllib2.Request('http://blog.csdn.net/cqcre')
try:
    urllib2.urlopen(req)
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason
else:
    print "OK"
```
# 4. Cookie

## 4.1获取Cookie保存到变量

```
import urllib2
import cookielib
#声明一个CookieJar对象实例来保存cookie
cookie = cookielib.CookieJar()
#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler=urllib2.HTTPCookieProcessor(cookie)
#通过handler来构建opener
opener = urllib2.build_opener(handler)
#此处的open方法同urllib2的urlopen方法，也可以传入request
response = opener.open('http://www.baidu.com')
for item in cookie:
    print 'Name = '+item.name
    print 'Value = '+item.value
```
结果
```
Name = BAIDUID
Value = B07B663B645729F11F659C02AAE65B4C:FG=1
Name = BAIDUPSID
Value = B07B663B645729F11F659C02AAE65B4C
Name = H_PS_PSSID
Value = 12527_11076_1438_10633
Name = BDSVRTM
Value = 0
Name = BD_HOME
Value = 0
```
## 4.2 保存Cookie到文件

```
import cookielib
import urllib2
 
#设置保存cookie的文件，同级目录下的cookie.txt
filename = 'cookie.txt'
#声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = cookielib.MozillaCookieJar(filename)
#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler = urllib2.HTTPCookieProcessor(cookie)
#通过handler来构建opener
opener = urllib2.build_opener(handler)
#创建一个请求，原理同urllib2的urlopen
response = opener.open("http://www.baidu.com")
#保存cookie到文件
cookie.save(ignore_discard=True, ignore_expires=True)
```
ignore_discard的意思是即使cookies将被丢弃也将它保存下来，ignore_expires的意思是如果在该文件中 cookies已经存在，则覆盖原文件写入，在这里，我们将这两个全部设置为True。运行之后，cookies将被保存到cookie.txt文件中,[结果如图](http://qiniu.cuiqingcai.com/wp-content/uploads/2015/02/QQ%E6%88%AA%E5%9B%BE20150215215136.jpg)

## 4.3 从文件中获取Cookie并访问
已经做到把Cookie保存到文件中了，如果以后想使用，可以利用下面的方法来读取cookie并访问网站
```
import cookielib
import urllib2
 
#创建MozillaCookieJar实例对象
cookie = cookielib.MozillaCookieJar()
#从文件中读取cookie内容到变量
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
#创建请求的request
req = urllib2.Request("http://www.baidu.com")
#利用urllib2的build_opener方法创建一个opener
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open(req)
print response.read()
```
## 4.4 利用cookie模拟网站登录

学校的教育系统为例，利用cookie实现模拟登录，并将cookie信息保存到文本文件中
```
import urllib
import urllib2
import cookielib
 
filename = 'cookie.txt'
#声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata = urllib.urlencode({
			'stuid':'201200131012',
			'pwd':'23342321'
		})
#登录教务系统的URL
loginUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bks_login2.login'
#模拟登录，并把cookie保存到变量
result = opener.open(loginUrl,postdata)
#保存cookie到cookie.txt中
cookie.save(ignore_discard=True, ignore_expires=True)
#利用cookie请求访问另一个网址，此网址是成绩查询网址
gradeUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bkscjcx.curscopre'
#请求访问成绩查询网址
result = opener.open(gradeUrl)
print result.read()
```
# 5. 正则表达式
[正则表达式的语法规则](http://qiniu.cuiqingcai.com/wp-content/uploads/2015/02/20130515113723855-e1424095177180.png)
正则表达式太繁杂，并且该教程讲解有点乱，所以直接上[源网址](http://python.jobbole.com/81346/),后续需要再找更清晰简单的教程进行内容补充。
# 6. BeautifulSoup

## 6.1　创建 Beautiful Soup 对象
```
from bs4 import BeautifulSoup
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
```

```
soup = BeautifulSoup(html)
```
还可以用本地 HTML 文件来创建对象
```
soup = BeautifulSoup(open('index.html'))
```
下面我们来打印一下 soup 对象的内容，**格式化输出prettify()**
```
print soup.prettify()
```
结果：
```
&lt;html&gt;
 &lt;head&gt;
  &lt;title&gt;
   The Dormouse's story
  &lt;/title&gt;
 &lt;/head&gt;
 &lt;body&gt;
  &lt;p class="title" name="dromouse"&gt;
   &lt;b&gt;
    The Dormouse's story
   &lt;/b&gt;
  &lt;/p&gt;
  &lt;p class="story"&gt;
   Once upon a time there were three little sisters; and their names were
   &lt;a class="sister" href="http://example.com/elsie" id="link1"&gt;
    &lt;!-- Elsie --&gt;
   &lt;/a&gt;
   ,
   &lt;a class="sister" href="http://example.com/lacie" id="link2"&gt;
    Lacie
   &lt;/a&gt;
   and
   &lt;a class="sister" href="http://example.com/tillie" id="link3"&gt;
    Tillie
   &lt;/a&gt;
   ;
and they lived at the bottom of a well.
  &lt;/p&gt;
  &lt;p class="story"&gt;
   ...
  &lt;/p&gt;
 &lt;/body&gt;
&lt;/html&gt;
```
## 6.2 四大对象种类
### （1）Tag
```
print soup.title
#<title>The Dormouse's story</title>

print soup.head
#<head><title>The Dormouse's story</title></head>

print soup.a
#<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>

print soup.p
#<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
```

```
print type(soup.a)
#<class 'bs4.element.Tag'>
```
soup 对象本身比较特殊，它的 name 即为 [document]，对于其他内部标签，输出的值便为标签本身的名称。
```
print soup.name
print soup.head.name
#[document]
#head
```
在这里，我们把 p 标签的所有属性打印输出了出来，得到的类型是一个字典。
```
print soup.p.attrs
#{'class': ['title'], 'name': 'dromouse'}

```

```
print soup.p['class']
#['title']
```
```
print soup.p.get('class')
#['title']
```
我们可以对这些属性和内容等等进行修改，例如
```
soup.p['class']="newClass"
print soup.p
#<p class="newClass" name="dromouse"><b>The Dormouse's story</b></p>
```
还可以对这个属性进行删除，例如

```
del soup.p['class']
print soup.p
#<p name="dromouse"><b>The Dormouse's story</b></p>
```

### （2）NavigableString
用如下代码我们就轻松获取到了标签里面的内容，想想如果用正则表达式要多麻烦。它的类型是一个 **NavigableString**，翻译过来叫 可以遍历的字符串，不过我们最好还是称它英文名字吧:
```
print soup.p.string
#The Dormouse's story
```
来检查一下它的类型
```
print type(soup.p.string)
#<class 'bs4.element.NavigableString'>
```

### （3）BeautifulSoup
```
print type(soup.name)
#<type 'unicode'>
print soup.name 
# [document]
print soup.attrs 
#{} 空字典
```
### （4）Comment
Comment 对象是一个特殊类型的 NavigableString 对象，其实输出的内容仍然不包括注释符号，但是如果不好好处理它，可能会对我们的文本处理造成意想不到的麻烦。

```
print soup.a
print soup.a.string
print type(soup.a.string)
```
运行结果如下
```
<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>
 Elsie 
<class 'bs4.element.Comment'>
```
a 标签里的内容实际上是注释，但是如果我们利用 .string 来输出它的内容，我们发现它**已经把注释符号去掉**了，所以这可能会给我们带来不必要的麻烦。

```
if type(soup.a.string)==bs4.element.Comment:
    print soup.a.string
```
## 6.3 搜索文档树

###（1）find_all( name , attrs , recursive , text , **kwargs )

find_all() 方法搜索当前tag的所有tag子节点,并判断是否符合过滤器的条件

#### 1）name 参数

name 参数可以查找所有名字为 name 的tag,字符串对象会被自动忽略掉

A.传字符串

最简单的过滤器是字符串.在搜索方法中传入一个字符串参数,Beautiful Soup会查找与字符串完整匹配的内容,下面的例子用于查找文档中所有的<b>标签
```
soup.find_all('b')
# [<b>The Dormouse's story</b>]
```
```
print soup.find_all('a')
#[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
```
B.传正则表达式

如果传入正则表达式作为参数,Beautiful Soup会通过正则表达式的 match() 来匹配内容.下面例子中找出所有以b开头的标签,这表示<body>和<b>标签都应该被找到
```
import re
for tag in soup.find_all(re.compile("^b")):
    print(tag.name)
# body
# b
```
C.传列表

如果传入列表参数,Beautiful Soup会将与列表中任一元素匹配的内容返回.下面代码找到文档中所有<a>标签和<b>标签

```
soup.find_all(["a", "b"])
# [<b>The Dormouse's story</b>,
#  <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
```
D.传 True

True 可以匹配任何值,下面代码查找到所有的tag,但是不会返回字符串节点
```
for tag in soup.find_all(True):
    print(tag.name)
# html
# head
# title
# body
# p
# b
# p
# a
# a
```
E.传方法

如果没有合适过滤器,那么还可以定义一个方法,方法只接受一个元素参数 [4] ,如果这个方法返回 True 表示当前元素匹配并且被找到,如果不是则反回 False

下面方法校验了当前元素,如果包含 class 属性却不包含 id 属性,那么将返回 True:

```
def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')
```
将这个方法作为参数传入 find_all() 方法,将得到所有<p>标签:

```
soup.find_all(has_class_but_no_id)
# [<p class="title"><b>The Dormouse's story</b></p>,
#  <p class="story">Once upon a time there were...</p>,
#  <p class="story">...</p>]
```
#### 2）keyword 参数

注意：如果一个指定名字的参数不是搜索内置的参数名,搜索时会把该参数当作指定名字tag的属性来搜索,如果包含一个名字为 id 的参数,Beautiful Soup会搜索每个tag的”id”属性
```
soup.find_all(id='link2')
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]
```
如果传入 href 参数,Beautiful Soup会搜索每个tag的”href”属性
```
soup.find_all(href=re.compile("elsie"))
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]
```
使用多个指定名字的参数可以同时过滤tag的多个属性

```
soup.find_all(href=re.compile("elsie"), id='link1')
# [<a class="sister" href="http://example.com/elsie" id="link1">three</a>]
```
在这里我们想用 class 过滤，不过 class 是 python 的关键词，这怎么办？加个下划线就可以
```
soup.find_all("a", class_="sister")
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
```
有些tag属性在搜索不能使用,比如HTML5中的 data-* 属性

```
soup.find_all("a", class_="sister")
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
```
但是可以通过 find_all() 方法的 attrs 参数定义一个字典参数来搜索包含特殊属性的tag

```
data_soup.find_all(attrs={"data-foo": "value"})
# [<div data-foo="value">foo!</div>]
```
#### 3）text 参数

通过 text 参数可以搜搜文档中的字符串内容.与 name 参数的可选值一样, text 参数接受 字符串 , 正则表达式 , 列表, True
```
soup.find_all(text="Elsie")
# [u'Elsie']
 
soup.find_all(text=["Tillie", "Elsie", "Lacie"])
# [u'Elsie', u'Lacie', u'Tillie']
 
soup.find_all(text=re.compile("Dormouse"))
[u"The Dormouse's story", u"The Dormouse's story"]
```
#### 4）limit 参数

find_all() 方法返回全部的搜索结构,如果文档树很大那么搜索会很慢.如果我们不需要全部结果,可以使用 limit 参数限制返回结果的数量.效果与SQL中的limit关键字类似,当搜索到的结果数量达到 limit 的限制时,就停止搜索返回结果.

文档树中有3个tag符合搜索条件,但结果只返回了2个,因为我们限制了返回数量
```
soup.find_all("a", limit=2)
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]
```
#### 5）recursive 参数

调用tag的 find_all() 方法时,Beautiful Soup会检索当前tag的所有子孙节点,如果只想搜索tag的直接子节点,可以使用参数 recursive=False .

一段简单的文档:
```
<html>
 <head>
  <title>
   The Dormouse's story
  </title>
 </head>
...
```
是否使用 recursive 参数的搜索结果:

```
soup.html.find_all("title")
# [<title>The Dormouse's story</title>]
 
soup.html.find_all("title", recursive=False)
# []
```
### （2）find( name , attrs , recursive , text , **kwargs )

它与 find_all() 方法唯一的区别是 find_all() 方法的返回结果是值包含一个元素的列表,而 find() 方法直接返回结果

### （3）find_parents() find_parent()

find_all() 和 find() 只搜索当前节点的所有子节点,孙子节点等. find_parents() 和 find_parent() 用来搜索当前节点的父辈节点,搜索方法与普通tag的搜索方法相同,搜索文档搜索文档包含的内容

### （4）find_next_siblings() find_next_sibling()

这2个方法通过 .next_siblings 属性对当 tag 的所有后面解析的兄弟 tag 节点进行迭代, find_next_siblings() 方法返回所有符合条件的后面的兄弟节点,find_next_sibling() 只返回符合条件的后面的第一个tag节点

###（5）find_previous_siblings() find_previous_sibling()

这2个方法通过 .previous_siblings 属性对当前 tag 的前面解析的兄弟 tag 节点进行迭代, find_previous_siblings() 方法返回所有符合条件的前面的兄弟节点, find_previous_sibling() 方法返回第一个符合条件的前面的兄弟节点

###（6）find_all_next() find_next()

这2个方法通过 .next_elements 属性对当前 tag 的之后的 tag 和字符串进行迭代, find_all_next() 方法返回所有符合条件的节点, find_next() 方法返回第一个符合条件的节点

### （7）find_all_previous() 和 find_previous()

这2个方法通过 .previous_elements 属性对当前节点前面的 tag 和字符串进行迭代, find_all_previous() 方法返回所有符合条件的节点, find_previous()方法返回第一个符合条件的节点

注：以上（2）（3）（4）（5）（6）（7）方法参数用法与 find_all() 完全相同，原理均类似，在此不再赘述。



## 6.4.CSS选择器

我们在写 CSS 时，标签名不加任何修饰，类名前加点，id名前加 #，在这里我们也可以利用类似的方法来筛选元素，用到的方法是 soup.select()，返回类型是 list

###（1）通过标签名查找

```
print soup.select('title') 
#[<title>The Dormouse's story</title>]
```
```
print soup.select('a')
#[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
```
```
print soup.select('b')
#[<b>The Dormouse's story</b>]
```
### （2）通过类名查找

```
print soup.select('.sister')
#[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
```
### （3）通过 id 名查找

```
print soup.select('#link1')
#[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>]
```
###（4）组合查找

组合查找即和写 class 文件时，标签名与类名、id名进行的组合原理是一样的，例如查找 p 标签中，id 等于 link1的内容，二者需要用空格分开

```
print soup.select('p #link1')
#[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>]
```
直接子标签查找
```
print soup.select("head > title")
#[<title>The Dormouse's story</title>]
```
（5）属性查找

查找时还可以加入属性元素，属性需要用中括号括起来，注意属性和标签属于同一节点，所以中间不能加空格，否则会无法匹配到。

```
print soup.select("head > title")
#[<title>The Dormouse's story</title>]
```
```
print soup.select('a[href="http://example.com/elsie"]')
#[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>]
```
同样，属性仍然可以与上述查找方式组合，不在同一节点的空格隔开，同一节点的不加空格

```
print soup.select('p a[href="http://example.com/elsie"]')
#[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>]
```
好，这就是另一种与 find_all 方法有异曲同工之妙的查找方法，是不是感觉很方便？



## 6.5 遍历文档树
### （1）直接子节点 .contents .children 

tag 的 .content 属性可以将tag的子节点以列表的方式输出
```
print soup.head.contents 
#[<title>The Dormouse's story</title>]
```
```
print soup.head.contents[0]
#<title>The Dormouse's story</title>
```
.children返回的不是一个 list，不过我们可以通过遍历获取所有子节点。

我们打印输出 .children 看一下，可以发现它是一个 list 生成器对象
```
print soup.head.children
#<listiterator object at 0x7f71457f5710>
```
```
for child in  soup.body.children:
    print child
```
结果：
```
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
 
<p class="story">Once upon a time there were three little sisters; and their names were
<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>,
<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
 
<p class="story">...</p>
```
### （2）所有子孙节点　.descendants 属性

.contents 和 .children 属性仅包含tag的直接子节点，.descendants 属性可以对所有tag的子孙节点进行递归循环，和 children类似，我们也需要遍历获取其中的内容。

```
for child in soup.descendants:
    print child
```
运行结果如下，可以发现，所有的节点都被打印出来了，先生最外层的 HTML标签，其次从 head 标签一个个剥离，以此类推。
```
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>,
<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
</body></html>
<head><title>The Dormouse's story</title></head>
<title>The Dormouse's story</title>
The Dormouse's story
 
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>,
<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
</body>
 
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<b>The Dormouse's story</b>
The Dormouse's story
 
<p class="story">Once upon a time there were three little sisters; and their names were
<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>,
<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
Once upon a time there were three little sisters; and their names were
 
<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>
 Elsie 
,
 
<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
Lacie
 and
 
<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
Tillie
;
and they lived at the bottom of a well.
 
<p class="story">...</p>
...
```
### （3）节点内容.string 属性

如果一个标签里面没有标签了，那么 .string 就会返回标签里面的内容。如果标签里面只有唯一的一个标签了，那么 .string 也会返回最里面的内容。例如
```
print soup.head.string
#The Dormouse's story
print soup.title.string
#The Dormouse's story
```
如果tag包含了多个子节点,tag就无法确定，string 方法应该调用哪个子节点的内容, .string 的输出结果是 None
```
print soup.html.string
# None
```
### （4）多个内容 .strings .stripped_strings

获取多个内容，不过需要遍历获取
```
for string in soup.strings:
    print(repr(string))
    # u"The Dormouse's story"
    # u'\n\n'
    # u"The Dormouse's story"
    # u'\n\n'
    # u'Once upon a time there were three little sisters; and their names were\n'
    # u'Elsie'
    # u',\n'
    # u'Lacie'
    # u' and\n'
    # u'Tillie'
    # u';\nand they lived at the bottom of a well.'
    # u'\n\n'
    # u'...'
    # u'\n'
```
.stripped_strings

输出的字符串中可能包含了很多空格或空行,使用 .stripped_strings 可以去除多余空白内容

```
for string in soup.stripped_strings:
    print(repr(string))
    # u"The Dormouse's story"
    # u"The Dormouse's story"
    # u'Once upon a time there were three little sisters; and their names were'
    # u'Elsie'
    # u','
    # u'Lacie'
    # u'and'
    # u'Tillie'
    # u';\nand they lived at the bottom of a well.'
    # u'...'
    
```
### （5）父节点 .parent 属性

```
p = soup.p
print p.parent.name
#body
```
```
content = soup.head.title.string
print content.parent.name
#title
```
### （6）全部父节点 .parents 属性

```
content = soup.head.title.string
for parent in  content.parents:
    print parent.name
```
```
title
head
html
[document]
```
### （7）兄弟节点 .next_sibling .previous_sibling
兄弟节点可以理解为和本节点处在统一级的节点，.next_sibling 属性获取了该节点的下一个兄弟节点，.previous_sibling 则与之相反，如果节点不存在，则返回 None

注意：实际文档中的tag的 .next_sibling 和 .previous_sibling 属性通常是字符串或空白，因为空白或者换行也可以被视作一个节点，所以得到的结果可能是空白或者换行
```
print soup.p.next_sibling
#       实际该处为空白
print soup.p.prev_sibling
#None   没有前一个兄弟节点，返回 None
print soup.p.next_sibling.next_sibling
#<p class="story">Once upon a time there were three little sisters; and their names were
#<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>,
#<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
#<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
#and they lived at the bottom of a well.</p>
#下一个节点的下一个兄弟节点是我们可以看到的节点
```
### （8）全部兄弟节点 .next_siblings .previous_siblings 

通过 .next_siblings 和 .previous_siblings 属性可以对当前节点的兄弟节点迭代输出
```
for sibling in soup.a.next_siblings:
    print(repr(sibling))
    # u',\n'
    # <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
    # u' and\n'
    # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
    # u'; and they lived at the bottom of a well.'
    # None
```
###（9）前后节点 .next_element .previous_element

与 .next_sibling .previous_sibling 不同，它并不是针对于兄弟节点，而是在所有节点，不分层次

```
<head><title>The Dormouse's story</title></head>
```
那么它的下一个节点便是 title，它是不分层次关系的

```
print soup.head.next_element
#<title>The Dormouse's story</title>
```
###（10）所有前后节点 .next_elements .previous_elements

通过 .next_elements 和 .previous_elements 的迭代器就可以向前或向后访问文档的解析内容,就好像文档正在被解析一样

```
for element in last_a_tag.next_elements:
    print(repr(element))
# u'Tillie'
# u';\nand they lived at the bottom of a well.'
# u'\n\n'
# <p class="story">...</p>
# u'...'
# u'\n'
# None
```

## url编码
```
>>> import urllib  
>>> data = '杭州' 
>>> print data 
杭州
```
```
>>> data  
'\xe6\x9d\xad\xe5\xb7\x9e'  
>>> urllib.quote(data)  
'%E6%9D%AD%E5%B7%9E' 
```
那我们想转回去呢？
```
>>> urllib.unquote('%E6%9D%AD%E5%B7%9E')  
'\xe6\x9d\xad\xe5\xb7\x9e'  
>>> print urllib.unquote('%E6%9D%AD%E5%B7%9E') 
杭州
```
细心的同学会发现贴吧url中出现的是%C0%F6%BD%AD，而非'%E4%B8%BD%E6%B1%9F'，其实是编码问题。百度的是gbk，其他的一般网站比如google就是utf8的。所以可以用下列语句实现。
```
>>> import sys,urllib   
>>> s = '杭州' 
>>> urllib.quote(s.decode(sys.stdin.encoding)
.encode('gbk'))  
%BA%BC%D6%DD  
>>> urllib.quote(s.decode(sys.stdin.encoding)
.encode('utf8'))  
'%E6%9D%AD%E5%B7%9E' 
```
以上的相关内容就是对Python中文转换url编码的详细介绍。
## 去掉字符串两边的空白符
```
demoStr.lstrip() = 去除left左边的白空格  = "hello wold !    "
demoStr.rstrip() = 去除right右边的白空格 = "      hello wold !"
 
demoStr.strip() = demoStr.lstrip().rstrip()=去除left左边和right右边=去除首尾的白空格="hello wold !"
```
## 去掉字符串当中的空格
使用字符串的replace方法，第一个参数是被替换的字符，第二个参数是替换为的字符
```
s = '***a b c**'
s = s.replace(' ', '')
s = s.replace('*', '')
```


--------
# 附录：HTTPError状态码说明
> 100：继续 客户端应当继续发送请求。客户端应当继续发送请求的剩余部分，或者如果请求已经完成，忽略这个响应。

> 101： 转换协议 在发送完这个响应最后的空行后，服务器将会切换到在Upgrade 消息头中定义的那些协议。只有在切换新的协议更有好处的时候才应该采取类似措施。

> 102：继续处理 由WebDAV（RFC 2518）扩展的状态码，代表处理将被继续执行。

> 200：请求成功 处理方式：获得响应的内容，进行处理

> 201：请求完成，结果是创建了新资源。新创建资源的URI可在响应的实体中得到 处理方式：爬虫中不会遇到

> 202：请求被接受，但处理尚未完成 处理方式：阻塞等待

> 204：服务器端已经实现了请求，但是没有返回新的信 息。如果客户是用户代理，则无须为此更新自身的文档视图。 处理方式：丢弃

> 300：该状态码不被HTTP/1.0的应用程序直接使用， 只是作为3XX类型回应的默认解释。存在多个可用的被请求资源。 处理方式：若程序中能够处理，则进行进一步处理，如果程序中不能处理，则丢弃
> 301：请求到的资源都会分配一个永久的URL，这样就可以在将来通过该URL来访问此资源 处理方式：重定向到分配的URL

> 302：请求到的资源在一个不同的URL处临时保存 处理方式：重定向到临时的URL

> 304：请求的资源未更新 处理方式：丢弃

> 400：非法请求 处理方式：丢弃

> 401：未授权 处理方式：丢弃

> 403：禁止 处理方式：丢弃

> 404：没有找到 处理方式：丢弃

> 500：服务器内部错误 服务器遇到了一个未曾预料的状况，导致了它无法完成对请求的处理。一般来说，这个问题都会在服务器端的源代码出现错误时出现。

> 501：服务器无法识别 服务器不支持当前请求所需要的某个功能。当服务器无法识别请求的方法，并且无法支持其对任何资源的请求。

> 502：错误网关 作为网关或者代理工作的服务器尝试执行请求时，从上游服务器接收到无效的响应。

> 503：服务出错 由于临时的服务器维护或者过载，服务器当前无法处理请求。这个状况是临时的，并且将在一段时间以后恢复。