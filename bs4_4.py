# 按CSS搜索
# bs4说白了 就是和html进行匹配然后找到需要的值，如果找到来就对了，
# 找不到就查找文档，换其他的方法，基本上都是可以找到的。

# bs4 文档
# https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/#id66

import re

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
soup = BeautifulSoup(html_doc, "lxml")

print(soup.find_all("a"), "sister")
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

print("="*80)
print(soup.find_all(class_=re.compile("title")))
# [<p class="title"><b>The Dormouse's story2</b></p>]
print(soup.find_all(re.compile("title")))
# [<title>The Dormouse's story1</title>]

print("="*80)
def has_six_characters(css_class):
    if css_class is not None and len(css_class) == 6:
        print(css_class)
        return css_class

print(soup.find_all(class_=has_six_characters))
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

print("="*80)
css_soup = BeautifulSoup('<p class="body strikeout"></p>', "lxml")
print(css_soup.find_all("p", class_="strikeout"))
# [<p class="body strikeout"></p>]

print(css_soup.find_all("p", class_="body"))
# [<p class="body strikeout"></p>]

print(css_soup.find_all(class_=re.compile("body")))
# [<p class="body strikeout"></p>]

print(soup.find_all("a", attrs={"class": "sister"}))
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]


# text 参数

html_doc = """
<html><head><title>The Dormouse's story1</title></head>

<p class="title"><b>The Dormouse's story2</b></p>
<body>
<p class="story">Once upon a time there were three little sisters; and their names were</p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
</body>
</html>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, "lxml")

print("="*80)
print(soup.find_all(text="Elsie"))
# [u'Elsie']

print(soup.find_all(text=["Tillie", "Elsie", "Lacie"]))
# [u'Elsie', u'Lacie', u'Tillie']

print(soup.find_all(text=re.compile("Dormouse")))
# [u"The Dormouse's story", u"The Dormouse's story"]

print(soup.find_all(text=re.compile("Els")))
# ['Elsie']

print("="*80)
def is_the_only_string_within_a_tag(s):
    # ""Return True if this string is the only child of its parent tag.""
    print('\n'+"---------")
    print(s)
    print(s.parent.string)
    print("---------"+'\n')
    return (s == s.parent.string)

print(soup.find_all(text=is_the_only_string_within_a_tag))
# ["The Dormouse's story1", "The Dormouse's story2",
# 'Once upon a time there were three little sisters; and their names were',
# 'Elsie', 'Lacie', 'Tillie', '...']


# limit 参数
# find_all() 方法返回全部的搜索结构,如果文档树很大那么搜索会很慢.如果我们不需要全部结果,
# # 可以使用 limit 参数限制返回结果的数量.效果与SQL中的limit关键字类似,
# # 当搜索到的结果数量达到 limit 的限制时,就停止搜索返回结果.
print("="*80)
print(soup.find_all("a", limit=2))
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

print("="*80)
html_doc = """
<html>
 <head>
  <title>
   The Dormouse's story
  </title>
 </head>
...
"""
soup = BeautifulSoup(html_doc, "lxml")
print(soup.find_all("title", recursive=False))


print(soup.html.find_all("title"))
# [<title>The Dormouse's story</title>]

print(soup.html.find_all("title", recursive=False))
# []

print("="*80)
# 增加html和不增加html效果是一样的
print(soup.html.find_all("title"))
# [<title>The Dormouse's story</title>]

print(soup.find_all("title"))
# [<title>The Dormouse's story</title>]

print("="*80)
# 唯一的区别是 find_all() 方法的返回结果是值包含一个元素的列表,而 find() 方法直接返回结果.
# find_all() 方法没有找到目标是返回空列表, find() 方法找不到目标时,返回 None .
print(soup.find_all('title', limit=1))
# [<title>The Dormouse's story</title>]

print(soup.find('title'))
# <title>The Dormouse's story</title>

print(soup.find("nosuchtag"))
# None

print("="*80)

html_doc = """
<html><head><title>The Dormouse's story1</title></head>

<p class="title"><b>The Dormouse's story2</b></p>
<body>
<p class="story">Once upon a time there were three little sisters; and their names were</p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
</body>
</html>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, "lxml")

a_string = soup.find(text="Lacie")
print(a_string)
# u'Lacie'

# find_parents() 用来搜索当前节点的父辈节点
print(a_string.find_parents("a"))
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]
print(a_string.find_parents("p"))
print(a_string.find_parents("p", class_="story"))


print("="*80)

first_link = soup.a
print(first_link)
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

print("="*80)
print(first_link.find_next_siblings("a"))
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

# find_next_siblings() 方法返回所有符合条件的后面的兄弟节点, find_next_sibling() 只返回符合条件的后面的第一个tag节点.
print("="*80)
first_story_paragraph = soup.find("p", "story")
print(first_story_paragraph)
print(first_story_paragraph.find_next_sibling("p"))
# <p class="story">...</p>


# find_previous_siblings() 方法返回所有符合条件的前面的兄弟节点,
# find_previous_sibling() 方法返回第一个符合条件的前面的兄弟节点:
print("="*80)
last_link = soup.find("a", id="link3")
print(last_link)
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

print(last_link.find_previous_siblings("a"))
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]

first_story_paragraph = soup.find("p", "story")
print(first_story_paragraph)
print(first_story_paragraph.find_previous_sibling("p"))
# <p class="title"><b>The Dormouse's story</b></p>


# find_all_next() 方法返回所有符合条件的节点, find_next() 方法返回第一个符合条件的节点:
print("="*80)
first_link = soup.find("a", id="link3")
print(first_link)
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

print(first_link.find_all_next(text=True))
# [u'Elsie', u',\n', u'Lacie', u' and\n', u'Tillie',
#  u';\nand they lived at the bottom of a well.', u'\n\n', u'...', u'\n']

print(first_link.find_next("p"))
# <p class="story">...</p>


# find_all_previous() 方法返回所有符合条件的节点, find_previous() 方法返回第一个符合条件的节点.
print("="*80)
first_link = soup.a
print(first_link)
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

print(first_link.find_all_previous("p"))
# [<p class="story">Once upon a time there were three little sisters; ...</p>,
#  <p class="title"><b>The Dormouse's story</b></p>]

print(first_link.find_previous("title"))
# <title>The Dormouse's story</title>