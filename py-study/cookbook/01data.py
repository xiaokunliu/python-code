#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import logging

_logger = logging.getLogger(__name__)


u"""
现在有一个包含 N 个元素的元组或者是序列，怎样将它里面的值解压后同时赋值给 N 个变量
解压赋值可以用在任何可迭代对象上面,而不仅仅是列表或者元组,包括字符串，文件对象，迭代器和生成器
只想解压一部分,丢弃其他的值,对于这种情况 Python 并没有提供特殊的语法,但是你可以使用任意变量名去占位,到时候丢掉这些变量就行了
"""
data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data

u"""
解压一部分，丢弃其他的值
"""

data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
_, shares, price, _ = data


# ===

u"""
解压可迭代对象赋值给多个变量
解压出来的数据结构永远是list类型,因此也不需要去做任何关于list的类型检查
1.扩展的迭代解压语法是专门为解压不确定个数或任意个数元素的可迭代对象而设计的
2.星号表达式在迭代元素为可变长元组的序列时是很有用的
3.星号解压语法在字符串操作的时候也会很有用，比如字符串的分割
4.解压一些元素后丢弃它们，你不能简单就使用 * ,
但是你可以使用一个普通的废弃名称，比如 _ 或者 ign （ignore）
"""
# py3.x 可用,py2.x 不可用
*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]


u"""
保留最后N个元素
在迭代操作或者其他操作的时候，怎样只保留最后有限几个元素的历史记录
解决方案：
保留有限历史记录正是 collections.deque 大显身手的时候
比如,下面的代码在多行上面做简单的文本匹配,并返回匹配所在行的最后N行
"""


def search(lines, pattern, history=5):
    from collections import deque
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


u"""
怎样从一个集合中获得最大或者最小的N个元素列表(N>1)
heapq 模块有两个函数：nlargest() 和 nsmallest() 可以完美解决这个问题
如果是要获取最大或者是最小的一个，可以使用min 或者是 max方法
"""

# 从存储单个元素的集合列表中获取
import heapq
# 底层是使用堆排序实现的
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums)) # Prints [42, 37, 23]
print(heapq.nsmallest(3, nums)) # Prints [-4, 1, 2]


# 从存储的字典列表中获取
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])


u"""
实现一个优先级排序队列,并且在这个队列上面每次 pop 操作总是返回优先级最高的那个元素
"""


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        u"""
        这里使用三个元素作为元组，python可以利用三个元素组成的元组进行比较
        元组比较将会从根据元素的起始位置进行纵横比较,使优先级用负数保证优先级最高的先出队列
        使用堆排序的数据结构添加数据
        :param item:
        :param priority:
        :return:
        """
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


u"""
 字典中的键映射多个值,使用collections 模块中的 defaultdict
 defaultdict 的一个特征是它会自动初始化每个 key 刚开始对应的值，所以你只需要关注添加元素操作
"""



