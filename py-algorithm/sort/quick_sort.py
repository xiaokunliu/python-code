#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
快速排序:是基于交换排序的一个变形，核心算法如下
将数组S排序的基本算法由下列简单的四步组成：
1）如果S中元素个数是0或者1，则返回
2）取S中任一元素v，称之为枢纽元
3）将S-{v}划分为两个不想交的集合，S1 = {x 属于 S-{v}} 且 x <= v,和S2 = {x 属于 S - {v}} 且 x > v
4) 返回quicksort(S1) + v + quicksort(S2)
"""


def quick_sort(numbers=[]):
    if len(numbers) <= 1:
        return numbers
    left_numbers = []
    right_numbers = []
    same = []
    point = numbers[int(len(numbers) / 2)]
    for num in numbers:
        if num > point:
            right_numbers.append(num)
        elif num < point:
            left_numbers.append(num)
        else:
            same.append(num)
    new_left = quick_sort(left_numbers)
    new_right = quick_sort(right_numbers)
    return new_left + same + new_right


#  算法优化：上述算法增加了空间存储，每次递归都会创建一个列表的空间内存，现在要消除每次递归创建列表空间内存

def my_quick_sort(numbers):
    if not numbers or len(numbers) <= 1:
        return numbers
    # 	以第一个数作为基准数
    point = numbers[0]
    left, right = 1, len(numbers) - 1
    while left < right:
        # 		从右边开始遍历，直到找到比point小对应的索引
        while numbers[right] > point and left < right:
            right -= 1
        # 		表示从最右边找到比point小的索引

        # 		开始从最左边查找比point大的索引
        while numbers[left] < point and left < right:
            left += 1
        # 		表示从最左边（除了point的索引）找到比point小的索引

        if left < right:
            numbers[left], numbers[right] = numbers[right], numbers[left]
    numbers[0], numbers[left] = numbers[left], numbers[0]
    return my_quick_sort(numbers[0:left]) + [point] + my_quick_sort(
        numbers[left + 1:])


numbers = [12, 3, 7, 9, 6, 23, 10, 11, 24, 25, 17, 4, 8, 19]
new_number = my_quick_sort(numbers)
print(new_number)
