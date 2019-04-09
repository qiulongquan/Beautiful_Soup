# 安装解析器
# html5lib
# lxml
# html.parser
# 上面3种常用，各有各自的优缺点，html.parser是在Python标准库中自带的，不需要安装。
# 推荐使用lxml作为解析器,因为效率更高.
# 在Python2.7.3之前的版本和Python3中3.2.2之前的版本,必须安装lxml或html5lib,
# 因为那些Python版本的标准库中内置的HTML解析方法不够稳定.
#
# 提示: 如果一段HTML或XML文档格式不正确的话,
# 那么在不同的解析器中返回的结果可能是不一样的,查看
# 解析器之间的区别 了解更多细节

from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc,"lxml")

# 将一段文档传入BeautifulSoup 的构造方法,
# 就能得到一个文档的对象, 可以传入一段字符串或一个文件句柄.
# soup = BeautifulSoup(open("index.html"))
# soup = BeautifulSoup("<html>data</html>")

print(soup.title)
# <title>The Dormouse's story</title>

print(soup.title.name)
# u'title'

print(soup.title.string)
# u'The Dormouse's story'

print(soup.title.parent.name)
# u'head'

print(soup.p)
# <p class="title"><b>The Dormouse's story</b></p>

print(soup.p['class'])
# u'title'

print(soup.a)
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

print(soup.a['class'])
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

print(soup.a['href'])
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

print(soup.a['id'])
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

a = soup.find_all('a')
for i in a:
    print(i)
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

print("="*80)
print(soup.find(id="link3"))
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

print("="*80)
for link in soup.find_all('a'):
    print(link.get('href'))
    # http://example.com/elsie
    # http://example.com/lacie
    # http://example.com/tillie

print("="*80)
# 从文档中获取所有文字内容:
print(soup.get_text())
# The Dormouse's story
#
# The Dormouse's story
#
# Once upon a time there were three little sisters; and their names were
# Elsie,
# Lacie and
# Tillie;
# and they lived at the bottom of a well.
#
# ...