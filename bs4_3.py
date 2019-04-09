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