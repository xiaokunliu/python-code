#### python字符串
*  Python 3.X provides an alternative string type for binary data, and supports Uni-
code text (including ASCII) in its normal string type.

*  Python 2.X provides an alternative string type for non-ASCII Unicode text, and
supports both simple text and binary data in its normal string type

> python3.x字符串处理的事情

* deal with non-ASCII Unicode text
* deal with binary data
* 定义的字符串能够根据操作系统默认的编码格式对字符串进行编解码运算

> 字符编码方案

* 字符集：是一种将整数代码分配给单个字符并能够在计算机内存中表示的一种标准
* ASCII标准：类似于字符串文本的概念，其定义了0-127的字符代码，并且允许每个字符都能够存储在一个8bit的大小空间，尽管实际是占用7bit
* 特殊字符，为了能够容纳特殊字符,一些标准尽可能使用8bit(0-255)来定义一个字符的存储(1个字节),分配128-255的值来定义特殊的字符
* Unicode被定义为"宽字符",这是由于一个字符可能占用多字节,Unicode编码字符主要应用于国际化的程序，代表着那些占用超过8bit的欧亚地区以及其他非英语字符集

> 字符串存储

在计算机中存储字符串文本数据，可以说字符通过编码encoding转换为原始字节(raw string)形式(使用r的时候是不会存在转移特殊字符),
原始字节(raw string)将通过解码decode的方式转换为字符文本数据

* 编码encoding：是一个将字符文本翻译成为原始的字节形式
* 解码decoding：是将一个原始的字节形式翻译成为字符文本数据

That is, we encode from string to raw bytes, and decode from raw bytes to string. To
scripts, decoded strings are just characters in memory, but may be encoded into a
variety of byte string representations when stored on files, transferred over networks,
embedded in documents and databases, and so on.

> py3.x的字符处理工具

* 文本工具：使用内置的ord函数返回一个Unicode对应的数值，并不要求是ASCII文本数据
* 文本大小：每个字符使用一个简单的7位字节ASCII文本数据存储，UTF-16使用一个字符用多字节存储的方式

> py的字符串类型

* str:代表8位字节存储的文本和二进制数据
* Unicode代表是一个解码后的Unicode文本数据

> py3.x的字符串类型

* str：代表着一个解码的文本数据，包括ASCII文本
* bytes：代表着一个二进制数据，包括编码后的文本数据
* bytearray：字节类型的可变风格

> 文本类型

* 二进制文件：图片数据，视频数据
* 文本文件：html文本，csv文本等

> 编写基本的字符串

* py3.x与py2.x的字符串

```python
b = b'binary_data'  # 二进制数据,py2x是属于字符串类型，py3x是二进制类型
s = 'string_data'   # 字符串数据

print b  # 打印将以字符串的形式打印

print b[0],s[0] # 字符串类型仍以字符串切片方式输出，b[0]则是以int类型的序列存储，输出的时候是输出整数

# bytes prefix works on single, double, triple quotes, raw
b_text = b"""
xxxxx xxxx
"""
```

> 字符串类型转换

* str.encode() and  bytes(S, encoding) :转为字节数据，分别将字符串数据转换为raw data数据、从一个解码的字符串创建一个字节对象
* bytes.decode() and  str(B, encoding) ：转为字符串数据，分别将一个raw字节转换为字符串、创建一个解码后的字符串

> 编写Unicode数据

* 编写ASCII文本

```python
> ord('X')  # 转换为整数数据

> chr(88)  # 转换为字符数据

> S = 'XYZ'
> S.encode('ascii') # 依次将字符串转换为ASCII对应的字节数据
```

> 编写非ASCII文本

```python
> chr(0xc4)       # 16进制数据转换为字符
> chr(0xe8)       # 16进制数据转换为字符
> S = '\xc4\xe8'    # 简单16进制转换，输出字符串
```

> 编码的文本

* py3.x允许使用十六进制和Unicode的方式编写特殊的字符
* 16进制方式编写的字符串将会被转移为字节字符串，而Unicode字符串则不会被转义

> 编码和解码非ASCII文本

```python
>>> S = '\u00c4\u00e8'   # Non-ASCII文本字符串，长度为2
>>> S.encode('ascii')   
UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1:
ordinal not in range(128)

>>> S.encode('latin-1')     # 能够正常被编码，长度为2
>>> S.encode('utf-8')       # 能够正常被编码，长度为4
```

> 字节字符形式：编码的文本数据

* py3.x允许使用特殊的字符通过hex和Unicode来对字符串进行转义
* hex表示的16进制字符将被转义为字节字符串，而Unicode声明的字符将以字节为单位保存字符，不做转义

> 编码转换

```python
>>> S.encode(character_set)
>>> S.decode(character_set)
```

> py3.x与py2.x编写Unicode字符串

* py2.x混合字符串类型

```python
# str + unicode,自动转换为unicode字符串,前提条件是均为ASCII文本
str = "abc" + u"xxx"
print type(str)     # unicode 类型

# 非ASCII文本不能进行混合操作
>>> S = "中文"
>>> U = u"中文"
>>> S+U
UnicodeDecodeError: 'ascii' codec can't decode byte 0xc4 in position 1: ordinal
not in range(128)
```

* py3.x

```python
# py3.x要求必须手动进行转换
# 字符串转Unicode字符串
>>> str(u"spam")
>>> unicode("spam")
```

> 声明py文件对应的字符串编码

```python
# -*- coding: UTF-8 -*-
```

> 使用py3.x字节对象

* 使用`__mod__ and  __rmod__` 内置操作符回调实现字符串的格式化

```python
>>> '%s' % 99
>>> b'%s' % 99   # 报错

>>> '{0}'.format(99)
>>> b'{0}'.format(99)      # 报错
```

* 字节与字符串转换

```python
# str.encode() or bytes()
>>> B = 'spam'.encode()     # bytes(str)  
>>> S = B.decode()          # str(B)
```

* 使用bytearray

```python
>>> bytearray('spam', 'UTF-8')
```

> py3.x使用总结

* Use  str for textual data.
* Use  bytes for binary data.
* Use  bytearray for binary data you wish to change in place.

> 使用文本和二进制文件

* 文本模式的文件接口内容将根据Unicode编码来定，要不就是默认的系统平台，或者指定一个编码名称传递进去
* 二进制文件将返回原始的字节数据值

> py2.x的文本和字节模式

```python
>>> open('temp', 'w').write('abd\n') # Write in text mode: adds \r
>>> open('temp', 'r').read() # Read in text mode: drops \r
'abd\n'
>>> open('temp', 'rb').read() # Read in binary mode: verbatim
'abd\r\n'
>>> open('temp', 'wb').write('abc\n') # Write in binary mode
>>> open('temp', 'r').read() # \n not expanded to \r\n
'abc\n'
>>> open('temp', 'rb').read()
'abc\n'
```

> py3.x的文本和字节模式

```python
>>> open('temp', 'w').write('abc\n') # Text mode makes and requires str
4
>>> open('temp', 'w').write(b'abc\n')
TypeError: must be str, not bytes
>>> open('temp', 'wb').write(b'abc\n') # Binary mode makes and requires bytes
4
>>> open('temp', 'wb').write('abc\n')
TypeError: 'str' does not support the buffer interface
```

> py3.x中读写Unicode数据

* 手动编码

```python
U = "str".encode("UTF-8")
```

* 文件读取与写入时进行编码

```python
# r表示默认以字符串的形式读取
# rb表示以二进制数据的形式读取出来
with open("test.txt","w","UTF-8") as writer, with open("read.txt","r","UTF-8") as reader:
    reader.read()
    writer.write("xxx")
```

* 解码不匹配

```python
>>> file = open(r'C:\Python33\python.exe', 'r')
>>> text = file.read()
UnicodeDecodeError: 'charmap' codec can't decode byte 0x90 in position 2: ...

>>> file = open(r'C:\Python33\python.exe', 'rb')
>>> data = file.read()
>>> data[:20]
b'MZ\x90\x00\x03\x00\x00\x00\x04\x00\x00\x00\xff\xff\x00\x00\xb8\x00\x00\x00'
```

> py3.x处理BOM

* In UTF-16, the BOM is always processed for “utf-16,” and the more specific encoding name “utf-16-le” denotes little-endian format.
* In UTF-8, the more specific encoding “utf-8-sig” forces Python to both skip and write a BOM on input and output, respectively, but the general “utf-8” does not

> 字符串处理工具

* 使用正则模块
* 使用结构化的二进制模块

```python
## py3.x
>>> from struct import pack
>>> pack('>i4sh', 7, b'spam', 8) # bytes in 3.X (8-bit strings)

## py2.x
C:\code> C:\python27\python
>>> from struct import pack
>>> pack('>i4sh', 7, 'spam', 8) # str in 2.X (8-bit strings)
'\x00\x00\x00\x07spam\x00\x08'
```

* 使用pickle模块将对象序列化

```python
import pickle
>>> pickle.dumps([1, 2, 3]) # Python 3.X default protocol=3=binary
b'\x80\x03]q\x00(K\x01K\x02K\x03e.'
>>> pickle.dumps([1, 2, 3], protocol=0) # ASCII protocol 0, but still bytes!
b'(lp0\nL1L\naL2L\naL3L\na.'
```

* 使用xml解析工具

```python
import re
text = open('mybooks.xml').read()
found = re.findall('<title>(.*)</title>', text)
for title in found: print(title)

from xml.dom.minidom import parse, Node
xmltree = parse('mybooks.xml')
for node1 in xmltree.getElementsByTagName('title'):
for node2 in node1.childNodes:
if node2.nodeType == Node.TEXT_NODE:
print(node2.data)

import xml.sax.handler
class BookHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        self.inTitle = False
    
    def startElement(self, name, attributes):
        if name == 'title':
            self.inTitle = True
    
    def characters(self, data):
        if self.inTitle:
            print(data)

    def endElement(self, name):
        if name == 'title':
            self.inTitle = False
            
import xml.sax
parser = xml.sax.make_parser()
handler = BookHandler()
parser.setContentHandler(handler)
parser.parse('mybooks.xml')
```
