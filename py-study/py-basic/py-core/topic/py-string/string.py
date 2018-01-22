#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Unicode与字节字符串
1. py3.x string的变化
2. 字符串的基础
3. 编写基本的字符串
4. 编写unicode字符串
5. 使用3.x的字节对象
6. 使用3.x、2.6字节数组对象
7. 使用文本和字节文件
8. 使用unicode文件
9. 3.x中的字符串工具
"""


"""
3.x的字符串变化
1）If you deal with non-ASCII Unicode text—for instance, in the context of internationalized domains like the Web,
or the results of some XML and JSON parsers and databases you will find support for text encodings to be different in 3.X, but also probably more direct, accessible, and seamless than in 2.X

2）If you deal with binary data—for example, in the form of image or audio files or packed data processed with the struct module you will need to understand 3.X’s new bytes object
and 3.X’s different and sharper distinction between text and bi- nary data and files

3）If you fall into neither of the prior two categories, you can generally use strings in 3.X much as you would in 2.X,
with the general str string type, text files, and all the familiar string operations we studied earlier.
Your strings will be encoded and decoded by 3.X using your platform’s default encoding
(e.g., ASCII, or UTF-8 on Windows in the U.S.—sys.getdefaultencoding gives your default if you care to check),
but you probably won’t notice
"""


"""
字符串的基础
1.
"""