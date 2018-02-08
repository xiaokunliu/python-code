#!/usr/bin/env python
# -*- coding: UTF-8 -*-


"""
类：通过对现实事物进行抽象来描述现实事物的行为和特性，通过类来管理对象实例
元类：描述上述类的类，即可以通过元类来管理类
1. 元类
> 作用:元类简单地扩展了装饰器的代码插入模型

1）将程序中的共用模块进行封装对外提供API或者工具类的调用
2）可以增强类的行为特征，类似于代理类或者是包装类的作用，即对原有的类进行方法功能或者是信息上的增强
3）可以实现面向切面编程以及与数据库映射的ORM设计
4）新式类的内存模型将通过元类更好地形象化展现

> python工具：
1）自省属性和工具： __class__ and  __dict__
2）重载操作符：__str__ and  __add__
3）属性操作回调方法：_getattr__ ,  __setattr__ ,__delattr__ , and  __getattribute__
4）类属性，内建 property
5）类属性描述：Descriptors（提供__get__ ,  __set__ , and  __delete__）
6）函数和类装饰器
7）元类

2. 元类的模型
1)python2的新式类与python3定义的类均是type类型的实例对象
2)元类是type类型的子类
3)类语句协议，class = type(classname, superclasses, attributedict)

3. 声明元类

> py3

1）class Spam(metaclass=Meta): # 3.X version (only)
2）class Spam(Eggs, metaclass=Meta): # Normal supers OK: must list first

> py2

class Spam(object):
    # 2.X version (only), object optional?
    __metaclass__ = Meta

class Spam(Eggs, object):
    # Normal supers OK: object suggested
    __metaclass__ = Meta

> py3 & py2 metaclass dispatch

class = Meta(classname, superclasses, attributedict)
Meta.__new__(Meta, classname, superclasses, attributedict)
Meta.__init__(class, classname, superclasses, attributedict)


4. 编写元类




5. 继承和实例
6. 元类方法
7. 添加方法到类中
8. 应用装饰器到方法中
"""






















