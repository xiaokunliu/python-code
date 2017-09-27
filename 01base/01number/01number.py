#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
python 数字类型
"""

#  整数和浮点数
import decimal
import math

from decimal import Decimal
from fractions import Fraction

"""
python3.0 只有整数，没有像2.6那样区分整数和长整数
"""
print(102929)
print(202.92929)
print(2.14e-10)

# 复数
# 通过complex创建复数
num = complex(10,-2)    # 10-2j
print(num)
print(3+5j)


# 固定精度的十进制数
# 整数转字符串
print(hex(29))      # 转16进制的字符串
print(oct(10))      # 转8进制的字符串
print(bin(20))      # 转2进制的字符串

# 字符串转整数
print(int("0x1d",base = 16))    # 16进制字符串转换为10进制表示
print(int("0o12",base = 8))     # 8进制字符串转换为10进制表示
print(int("0b10100",base = 2))  # 2进制字符串转换为10进制表示

#  python 表达式操作符
"""
yield x                 生成器函数发送协议
lambda args:expression  生成匿名函数
x if y else z           三元选择表达式
x or y                  逻辑或（只有x为假才会计算y）
x and y                 逻辑与（只有x为真，才会计算y）
not x                   逻辑非
x in y，x not in y      成员关系（可迭代对象、集合）
x is y，x is not y      对象实体测试
x // y                  floor除法
x ** y                  幂运算
x[i]                    索引
x[i:j:k]                分片
x(...)                  调用函数、方法、类以及其他可调用的
x.attr                  属性引用
(...)                   元组，表达式，生成器表达式
[...]                   列表，列表解析
{...}                   字典、集合、集合和字典解析
"""

# 混合类型自动升级
print(10 + 0.2093)      #自动转成浮点数

# 数字显示格式化
num = 1 / 3.0
print(('%e' % num))
print(('%4.2f' % num))          # 显示小数点后两位
print('{0:4.2f}'.format(num))   # 显示小数点后两位

"""
默认交互的的回显和打印的区别就相当于repr[默认交互模式]和str[打印语句]的区别
repr -- 用于额外细节
str  -- 用于一般用途
"""

"""
支持两个python版本（2.x 和 3.x）
可以在2.x中导入 __future__import 打开3.x的一些操作符计算
"""


"""
传统除法 与 Floor(截断)除法

x / y 传统除法 与 真除法

x // y Floor 除法，把结果向下截断到它的下层，即真正结果之下的最近整数
"""
print(math.floor(-2.5))     # 向下取整，显示 -3
print(math.floor(2.5))      # 向下取整，显示 2

print(math.trunc(-2.5))     # 直接截断小数，显示2
print(math.trunc(2.5))      # 直接截断小数，显示2

str1 = '{0:o},{1:x},{2:b}'.format(64,64,64)
str2 = '%o,%x,%X' % (64,255,255)
print(str1)
print(str2)


"""
使用内置的浮点数缺乏精度，需要导入模块Decimal
"""
print(Decimal(1.0) + Decimal(1.0) + Decimal(1.0) - Decimal(3.0))

# 设置全局精度
# print(Decimal(1.0) / Decimal(7.0))
#
# # 保留小数点后四位
# decimal.getcontext().prec = 4
# print(Decimal(1.0) / Decimal(7.0)) ## 四舍五入之后的结果保留4位


# 使用上下文管理器设置临时进度
with decimal.localcontext() as ctx:
	ctx.prec = 4
	print(Decimal(1.0) / Decimal(7.0))

print(Decimal(1.0) / Decimal(7.0))


#  分数类型
x = Fraction(1,3)
print(x)

y = Fraction(4,6)
print(y)

print(x+y)
print(x-y)
print(x*y)

z = Fraction('.25')
print(z)

# 转换和混合类型
print((2.5).as_integer_ratio())

f = 2.5
fz = Fraction(*f.as_integer_ratio())
print(fz)



