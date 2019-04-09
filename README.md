```

Beautiful Soup 是一个可以从HTML或XML文件中提取数据的Python库.
它能够通过你喜欢的转换器实现惯用的文档导航,查找,修改文档的方式.
BeautifulSoup4 说明文档
https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/

安装解析器
html5lib
lxml
html.parser
上面3种常用，各有各自的优缺点，
html.parser是在Python标准库中自带的，不需要安装。
推荐使用lxml作为解析器,因为效率更高.
在Python2.7.3之前的版本和Python3中3.2.2之前的版本,
必须安装lxml或html5lib,
因为那些Python版本的标准库中内置的HTML解析方法不够稳定.

提示: 如果一段HTML或XML文档格式不正确的话,
那么在不同的解析器中返回的结果可能是不一样的,
查看解析器之间的区别 了解更多细节

```