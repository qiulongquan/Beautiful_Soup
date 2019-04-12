# 按CSS搜索

# bs4说白了 就是和html进行匹配然后找到需要的值，如果找到来就对了，
# 找不到就查找文档，换其他的方法，基本上都是可以找到的。

# bs4 文档
# https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/#id66



"""
指定文档解析器
如果仅是想要解析HTML文档,只要用文档创建 BeautifulSoup 对象就可以了.
Beautiful Soup会自动选择一个解析器来解析文档.但是还可以通过参数指定使用那种解析器来解析当前文档.

BeautifulSoup 第一个参数应该是要被解析的文档字符串或是文件句柄,第二个参数用来标识怎样解析文档.
如果第二个参数为空,那么Beautiful Soup根据当前系统安装的库自动选择解析器,
解析器的优先数序: lxml, html5lib, Python标准库.在下面两种条件下解析器优先顺序会变化:

要解析的文档是什么类型: 目前支持, “html”, “xml”, 和 “html5”
指定使用哪种解析器: 目前支持, “lxml”, “html5lib”, 和 “html.parser”
安装解析器 章节介绍了可以使用哪种解析器,以及如何安装.

如果指定的解析器没有安装,Beautiful Soup会自动选择其它方案.目前只有 lxml 解析器支持XML文档的解析,在没有安装lxml库的情况下,
创建 beautifulsoup 对象时无论是否指定使用lxml,都无法得到解析后的对象
"""


import re

html_doc = """
<html><head><title>The Dormouse's story1</title></head>

<p class="title"><b>The Dormouse's story2</b></p>
<body>
<a href="http://example.com/elsie" class="sister" id="link4">Elsie444</a>
</body>
<body1>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
<a1 href="http://example.com/tillie" class="sister" id="link3">Tillie</a1>;
and they lived at the bottom of a well.</p>
</body1>
<p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, "lxml")

print("="*80)
print(soup.select("html"))
# [<title>The Dormouse's story</title>]

print("="*80)
# 找到某个tag标签下的直接子标签 [6] :
print(soup.select("body > a"))
# [<a class="sister" href="http://example.com/elsie" id="link4">Elsie444</a>]

print(soup.select("html head title"))
# [<title>The Dormouse's story</title>]

print(soup.select("body1 a"))

print("="*80)
print(soup.select("p > a1"))
# [<a1 class="sister" href="http://example.com/tillie" id="link3">Tillie</a1>]

print("="*80)
print(soup.select("p > a:nth-of-type(2)"))
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

print("="*80)
print(soup.select("p > #link1"))
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]

print("="*80)
print(soup.select(".sister"))
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

print("="*80)
# 通过属性的值来查找:
print(soup.select('a[href="http://example.com/elsie"]'))
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]

print("="*80)
print(soup.select('a[href^="http://example.com/"]'))
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

print("="*80)
print(soup.select('a[href$="tillie"]'))
# [<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

print("="*80)
print(soup.select('a[href*=".com/el"]'))
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]


# 修改文档树
# Beautiful Soup的强项是文档树的搜索,但同时也可以方便的修改文档树

print("="*80)
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', "lxml")
tag = soup.b
print(tag)
print(tag.name)
tag.name = "blockquote"
# 可以增加tag的属性
tag['class'] = 'verybold'
tag['id'] = 1
print(tag)
# <blockquote class="verybold" id="1">Extremely bold</blockquote>

# 可以删除tag的属性
del tag['class']
del tag['id']
print(tag)
# <blockquote>Extremely bold</blockquote>


# 修改 .string
print("="*80)
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup, "lxml")
print(tag)
tag = soup.a
tag.string = "New link text1."
print(tag)
# <a href="http://example.com/">New link text.</a>


# append()
print("="*80)
soup = BeautifulSoup("<a>Foo</a>", "lxml")
soup.a.append("Bar")

print(soup)
# <html><head></head><body><a>FooBar</a></body></html>
print(soup.a.contents)
# [u'Foo', u'Bar']


print("="*80)
# 这是Beautiful Soup 4.2.1 中新增的方法

# 创建一个tag最好的方法是调用工厂方法 BeautifulSoup.new_tag() :

soup = BeautifulSoup("<b></b>", "lxml")
original_tag = soup.b

new_tag = soup.new_tag("a", href="http://www.example.com")
original_tag.append(new_tag)
print(original_tag)
# <b><a href="http://www.example.com"></a></b>

new_tag.string = "Link text."
print(original_tag)
# <b><a href="http://www.example.com">Link text.</a></b>


# 格式化输出  这个很重要，可以很美观的显示html内容
# prettify() 方法将Beautiful Soup的文档树格式化后以Unicode编码输出,每个XML/HTML标签都独占一行
print("="*80)
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup, "lxml")
soup.prettify()
# '<html>\n <head>\n </head>\n <body>\n  <a href="http://example.com/">\n...'

print(soup.prettify())
# <html>
#  <head>
#  </head>
#  <body>
#   <a href="http://example.com/">
#    I linked to
#    <i>
#     example.com
#    </i>
#   </a>
#  </body>
# </html>

print("="*80)
# BeautifulSoup 对象和它的tag节点都可以调用 prettify() 方法:
print(soup.a.prettify())
# <a href="http://example.com/">
#  I linked to
#  <i>
#   example.com
#  </i>
# </a>


# get_text()
print("="*80)
markup = '<a href="http://example.com/">\nI linked to <i>example.com</i>\n</a>'
soup = BeautifulSoup(markup, "lxml")

print(soup.get_text())
# u'\nI linked to example.com\n'
print(soup.i.get_text())
# u'example.com'


# 可以通过参数指定tag的文本内容的分隔符:
print(soup.get_text(","))
# I linked to ,example.com,

# 还可以去除获得文本内容的前后空白:
print(soup.get_text("|", strip=True))
# u'I linked to|example.com'

print("="*80)
markup = u"<h1>1234abc我要吃饭</h1>"
soup = BeautifulSoup(markup, "lxml")
print(soup.h1)
# <h1>νεμω</h1>
print(soup.original_encoding)
# 'ISO-8859-7'
soup.original_encoding = "utf-8"
print(soup.h1)
print(soup.original_encoding)
