#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
__call__
"""
class CallClass:
	def __call__(self, *args, **kwargs):
		print("Call class call")
		if args is not None:
			for item in args:
				print(item)

		if kwargs is not None:
			for k,v in kwargs.items():
				print(k,v)


def test_call():
	c = CallClass()
	c(1, 2, 3)  # 调用类实例进行赋值，会回调CallClass的__call__方法

# print(c)

# __call__应用： Function Interfaces and Callback-Based Code


class CallBack:
	def __init__(self,color):
		self.color = color

	def __call__(self):
		print("call callback color[%s]" % self.color)


class EventCall:
	def __init__(self,callback = None):
		self.c = callback

	def press(self):
		self.c()


def test_call_back():
	c1 = CallBack("red")
	c2 = CallBack("green")
	e1 = EventCall(callback = c1)
	e2 = EventCall(callback = c2)

	e1.press()      # when press then trigger callback
	e2.press()


# 使用函数进行回调
def callback_fn(color):
	def oncall():
		print("select the color[%s]" % color)
	return oncall


def test_callback_fn():
	fn = callback_fn("green")
	fn()


# def test_lamaba_callback():
# 	cs4 = (lambda color='red': print('turn ' + color))
# 	cs4()

# if __name__ == '__main__':
#     # test_call()
#     test_call_back()
#     # test_callback_fn()
#     # test_lamaba_callback()


"""
比较运算符
1. 比较运算符不存在像 __add__ 或 __iadd__的边界运算
2. 比较运算符没有隐式关系
3. py2.x在没有特殊定义下都是通过__cmp__的方法来进行比较,py3.x已经删除__cmp__以及cmp方法，用特定的方法来代替
"""


class C:
	"""
	方式一
	"""
	data = 'spam'

	def __gt__(self, other): return self.data > other

	def __lt__(self, other): return self.data < other


class S:
	data = "spam"
	"""
	python3.x将不可用
	"""
	def __cmp__(self, other):
		return cmp(self.data,other)


class D:
	"""
	方式三,改变cmp的方法,3.x仍然报错
	"""
	data = "d"

	def __cmp__(self, other):
		return (self.data > other) - (self.data < other)


def test_c():
	c = C()
	print(c > 'ham')
	print(c < 'ham')


def test_S():
	s = S()
	print(s > 'ham')


def test_d():
	d = D()
	print(d > 'ham')
	print(d < 'ham')

if __name__ == '__main__':
	# test_c()
	# test_d()
	test_S()
	# pass


"""
bool 测试:__bool__ & __len__
"""


class Truth:
	def __bool__(self):
		print("call bool method ...")
		return True

	"""
	3.x:如果没有__bool__就会执行__len__,也就是两个都存在的时候，__bool__的优先级比__len__高
	2.x如果没有__bool__就会执行__len__,也就是两个都存在的时候，__len__的优先级比__bool__高
	"""
	def __len__(self):
		print("call len method ....")
		return 0

	"""
	__nonzero__:仅在python2.x使用，用于返回一个布尔值,并且优先级大于上面的__len__方法
	"""
	# def __nonzero__(self):
	# 	print "call zero for python2.x"
	# 	return False

def test_truth():
	X = Truth()
	if X:   # 调用__bool__方法
		print("i'm truth ....")


# if __name__ == '__main__':
#     test_truth()


# 对象析构 __del__
class Life:
	def __init__(self, name='unknown'):
		print('Hello ' + name)
		self.name = name

	def live(self):
		print(self.name)

	def __del__(self):
		print('Goodbye ' + self.name)

"""
__del__使用笔记：
Need:python会自动回收内存空间，析构器并非是空间管理的一项必需工具
Predictability:python退出解释器的时候，并不能保证会调用仍然存在的对象的析构函数来进行回收操作
Exceptions:由于存在异常情况并且不知道异常发生的时刻，析构器很难确定什么时候调用来进行回收操作
Cycles:对象的循环引用可以防止垃圾回收器发生一些如我们所期望的错误或者异常
"""


def test_del():
	l = Life("keithl")
	l.live()

# if __name__ == '__main__':
#     test_del()