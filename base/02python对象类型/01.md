#### 数字类型
* 基本数字类型操作
> 十进制转16进制、8进制、2进制
```
num = 29  ## 10进制
## 转16进制
hex(num)   ## 0x1d

## 转8进制
oct(num)   ## 0o35

## 转2进制
bin(num)   ## 0b11101
```

> 16进制、8进制、2进制转十进制
```
## 16进制转10进制
str_hex = r'0x1d'
int(str_hex,base = 16)

## 8进制转10进制
str_oct = r'0o35'
int(str_oct,base = 8)

## 2进制转10进制
str_bin = r'0b11101'
int(str_bin,base = 2)
```

> 定义复数
```
## 1 way
b = 3 + 3j

## 2 way
a = complex(2,10)       ## 使用内置函数定义复数
```

> 数字格式化显示
```
### python3.5
>>> num = 1 / 3.0
>>> print(num)
0.3333333333333333

## 使用科学基数法计算
>>> '%e' % num
'3.333333e-01'  ## 输出是字符串类型

## 保留两位小数并格式化为字符串显示
>>> '%4.2f' % num
'0.33'

## 使用format方法格式化(一般使用这种方式格式化)
>>> '{0:4.2f}'.format(num)
'0.33'
```

> python2.7与python3.5的"/"与"//"
```
python2.7中"/"，对于整数会保持结果为整数，对于浮点数会保持小数部分
python3.x中"/". 始终返回带有小数部分

python2.7和python3.x中"//".不考虑操作对象的类型，总会省略掉结果的小数部分，剩下最小的能整除的整数部分
```

> Floor与Truncation区别
```
## 导入math模块
## floor是获取最靠近整数的下限，truncation是直接获取数据的整数部分
>>> import math
>>> math.floor(2.5) 
2
>>> math.floor(-2.5) 
-3
>>> math.trunc(2.5) 
2
>>> math.trunc(-2.5) 
-2
```

* 其他数字类型 
> 数字精度
```code 
## 将数字字符串转换为浮点数据
#### python3.x,python2.7 之前只能使用字符串
>>> from decimal import Decimal
>>> Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3') 
Decimal('0.0')

#### python3.x，python2.7之后不仅支持字符串也可以支持小数点转换，并且产生更多的位数
>>> Decimal(0.1) + Decimal(0.1) + Decimal(0.1) - Decimal(0.3) 
Decimal('2.775557561565156540423631668E-17')

#### 设置全局精度
>>> decimal.getcontext().prec = 4
>>> decimal.Decimal(1) / decimal.Decimal(7) 
Decimal('0.1429')

#### Decimal context manager
>>> import decimal
>>> decimal.Decimal('1.00') / decimal.Decimal('3.00') 
Decimal('0.3333333333333333333333333333')
>>> with decimal.localcontext() as ctx:
... ctx.prec = 2
... decimal.Decimal('1.00') / decimal.Decimal('3.00') 
...
Decimal('0.33')
>>>
>>> decimal.Decimal('1.00') / decimal.Decimal('3.00')
Decimal('0.3333333333333333333333333333')
```

> 定义分数
```code 
>>> from fractions import Fraction 
>>> x = Fraction(1, 3)
>>> y = Fraction(4, 6)
>>> x Fraction(1, 3) >>> y Fraction(2, 3) >>> print(y) 2/3
```





