from bs4 import BeautifulSoup

soup = BeautifulSoup('<b class="boldest">Extremely bold</b>',"lxml")
tag = soup.b
print(type(tag))
# <class 'bs4.element.Tag'>

print("="*80)
print(tag.name)
# u'b'

print("="*80)
# 如果改变了tag的name,那将影响所有通过当前Beautiful Soup对象生成的HTML文档:
tag.name = "blockquote"
print(tag)
# <blockquote class="boldest">Extremely bold</blockquote>

print("="*80)
# 一个tag可能有很多个属性. tag <b class="boldest"> 有一个 “class” 的属性,
# 值为 “boldest” . tag的属性的操作方法与字典相同:
print(tag['class'])
# u'boldest'

print("="*80)
print(tag.attrs)
# {u'class': u'boldest'}

print("="*80)
# tag的属性可以被添加,删除或修改. 再说一次, tag的属性操作方法与字典一样
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>',"lxml")
tag = soup.b
tag['class'] = 'verybold'
tag['id'] = 1
print(tag)
# <blockquote class="verybold" id="1">Extremely bold</blockquote>

del tag['class']
del tag['id']
print(tag)
# <blockquote>Extremely bold</blockquote>

# print(tag['class'])
# KeyError: 'class'
print(tag.get('class'))
# None

print("="*80)
# 在Beautiful Soup中多值属性的返回类型是list:
css_soup = BeautifulSoup('<p class="body strikeout"></p>',"lxml")
css_soup.p['class']
# ["body", "strikeout"]

css_soup = BeautifulSoup('<p class="body"></p>',"lxml")
css_soup.p['class']
# ["body"]

print("="*80)
id_soup = BeautifulSoup('<p id="my id"></p>',"lxml")
print(id_soup.p['id'])
# 'my id'

print("="*80)
rel_soup = BeautifulSoup('<p>Back to the <a rel="index">homepage</a></p>',"lxml")
print(rel_soup.a['rel'])
# ['index']
rel_soup.a['rel'] = ['index', 'contents']
print(rel_soup.p)
# <p>Back to the <a rel="index contents">homepage</a></p>

print("="*80)
xml_soup = BeautifulSoup('<p class="body strikeout"></p>', 'xml')
print("unique code = "+xml_soup.p['class'])
# u'body strikeout'

# 可以遍历的字符串

print("="*80)
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>',"lxml")
tag = soup.b
tag.string
# u'Extremely bold'
print(type(tag.string))
# <class 'bs4.element.NavigableString'>


print("="*80)
html_doc = """
<html><head><title>The Dormouse's story1</title></head>

<p class="title"><b>The Dormouse's story2</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc,"lxml")

print(soup.find_all('a'))
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

print("="*80)
head_tag = soup.head
print(head_tag)
# <head><title>The Dormouse's story</title></head>

print(head_tag.contents)
# [<title>The Dormouse's story</title>]

title_tag = head_tag.contents[0]
print(title_tag)
# <title>The Dormouse's story</title>
print(title_tag.contents)
# [u'The Dormouse's story']

print(len(soup.contents))
# 1
# 把全部html内容打印
print(soup.contents)

print("="*80)
print(soup.contents[0].name)
# u'html'

print("="*80)
for child in head_tag.descendants:
    print(child)
    # <title>The Dormouse's story</title>
    # The Dormouse's story

print("="*80)
print(len(list(soup.children)))
# 1

print(list(soup.descendants))
# 25

print("="*80)
html_doc = """
<html><head><title>The Dormouse's story1</title></head>

<p class="title"><b>The Dormouse's story2</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc,"lxml")

last_a_tag = soup.find("a", id="link2")
print(last_a_tag)
# <a class="sister" href="http://example.com/tillie" id="link1">Tillie</a>

print(last_a_tag.next_sibling)

print(last_a_tag.next_sibling.next_sibling)

print(last_a_tag.previous_element.previous_element)

# 搜索文档树

html_doc = """
<html><head><title>The Dormouse's story</title></head>

<p class="title"><b>The Dormouse's story</b></p>

<p class="story1">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="title">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, "lxml")

# 如果传入字节码参数,Beautiful Soup会当作UTF-8编码,可以传入一段Unicode 编码来避免Beautiful Soup解析编码出错

# 正则表达式

print("="*80)
# 把P开头到结尾的所有值都取回来了。<p  ....  </p>
print(soup.find_all("p", "title"))
# [<p class="title"><b>The Dormouse's story</b></p>, <p class="title">...</p>]

print("="*80)
import re
print(soup.find_all(href=re.compile("example"), id="link1"))
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]

print("="*80)
data_soup = BeautifulSoup('<div data1-foo="value">foo!</div>', "lxml")
# 特殊的符号data1-foo 不能用普通方式获取 需要用attrs方式来获取值
# print(data_soup.find_all(data1-foo="value"))
# SyntaxError: keyword can't be an expression

print(data_soup.find_all(attrs={"data1-foo":"value"}))
# [<div data-foo="value">foo!</div>]