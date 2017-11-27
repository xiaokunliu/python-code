1.class 语句

> 定义class statement

```python 
"""
    分配类名称,超类的连接通过括号内从左至右列出类而生成的
"""
class className(superclass1,superclass2,...):       
    '''
        定义类属性,属于所有实例的共享数据,通过类语句下进行定义和创建
    '''
    class_attr = value 
    
    
    '''
        定义实例方法以及实例属性，创建类的实例对象，每个实例对象都拥有属于自己的命名空间
    '''
    def method(self,data):      ## 定义实例方法
        self.attr = data        ## 设置实例属性,通过带有self的方法来分配属性信息
```

> 类基础概念

* python执行（非调用）类的时候，将会从头到尾执行class内定义的statement语句

```python
## person.py
## python执行的时候将会从头至尾执行一次,即会以下class的所有语句
1 class Person:
2    def __init__(self,name):
3         self.name = name
```

* 与函数类似,class语句是一个本地作用域,在class语句下定义的变量名称就属于这个本地作用域

图片

* 与模块中的变量名类似，分配在class statement下的变量名是属于类对象的属性

图片

2.方法

> python实例方法与类方法之间的映射

```
## person.py 
class Person:
    def __init__(self,name):
        self.name = name 
    
    def displayName(self):
        print(self.name)
## 创建实例并实例调用方法
>>> p = Person("person name")
>>> p.display()
person name

## 通过类调用具体实例的方法
>>> Person.display(p)
person name

## 总结：实例对象调用实例方法等价于类调用实例方法并传递实例对象
instance.method(arg1,...) <==> class.method(instance,arg1,...)
```

> 调用父类构造器,可以定制化子类拥有的属性和行为

```python
## person.py
class Person:
    def __init__(self,name,age):
        print("person init ...")
        self.name = name
        self.age = age
        
class Engineer(Person):
    def __init__(self,name,age=30)
        """
            调用父类构造器
        """
        print("Engineer init ...")
        Person.__init__(self,name,age)

## 测试
>>> Person("keithl",27)
person init ...

>>> Engineer("keithl")
Engineer init ...
person init ...
```

###### python命名空间总结

1. 命名空间定义
    * 是一种定义名称的工具，比如属性
    * 哪些名称，即向客户端暴露数据和处理逻辑的名称

2. 命名空间作用
    * 变量是通过命名空间存储的方式来查找最近的命名空间中的属性名称
    * 模块命名空间通过内置属性`__dict__`暴露属性信息
    * 类和对象命名空间通过类似字典的方式连接并将属性暴露出来
    * 类实例对象通过`__class__`属性来链接定义的类
    * 类通过`__bases__`属性来链接更高级的超类

3. 定义简单变量名称，即根据命名空间查询变量名称,遵循函数LEGB法则（local、enclosing、global、builtin）
    * 分配值,即X = value
    * 引用值,即引用X变量名称

```python
## LEGB法则应用
## legb.py
X = "glboal var x"          ## 模块的命名空间

def enclosing_fn():
    X = "enclosing var x"   ## 函数中嵌套函数的名字空间
    def call_fn():
        X = "local var x"   ## 函数内部命名空间
        print(X)
    call_fn()
    print(X)

# 还有一个python内置模块的命名空间，builtin
enclosing_fn()
print(X)

## 测试
>>> python legb.py
local var x
enclosing var x
glboal var x

## 注释 local X
>>> python legb.py
enclosing var x
enclosing var x
glboal var x

## 注释 local X 和 enclosing X
>>> python legb.py
glboal var x
glboal var x
glboal var x
```

3. 定义属性名称：对象命名空间
    * 属性值分配(object.X = value),只能根据对象命名空间下定义的属性名称来创建或者修改属性X
    * 引用属性名称(object.X),根据继承搜索树来查找
    
```python 
## object.py
## 对象命名空间赋值
class Person:
    data = "person class data"                  ## 直接在所在的对象中创建属性data，这里是指类对象
    def __init__(self,name,age):
        self.name = name            
        self.age = age
        self.data = "person instance data"      ## 直接在属性对象实例中创建属性name，这里是指类实例对象
    
## 测试对象命名空间
>>> p = Person()
>>> p.data                                      ## 根据继承搜索查询实例对象中属性data，搜索起点是对象实例p

>>> Person.data                                 ## 同上，但是搜索起点是类Person
```

4. 嵌套函数中定义的class，快速定位变量所属作用域

```python
## 嵌套类的函数值的引用
X = 20
def nested_fn():
    print(X)                
    class NestedClass:      
        print(X)            
    
        def m1(self):
            print(X)
            
        def m2(self):
            X = 30
            print(X)
    
    nested = NestedClass()  ## 20，全局变量
    nested.m1()             ## 20
    nested.m2()             ## 30,本地变量隐藏全局变量
print(X)                    ## 20

## 嵌套类的函数赋值操作
X = 20                      ## 创建全局变量X
def nested_fn():
    X = 30                  ## 创建嵌套函数下的本地变量X，隐藏全局变量X
    print(X)
    class NestedClass:
        X = 40              ## 创建类变量X，必须通过[类.属性]来显示调用,否则其他位置的变量X都是用简单命名空间规则来查找
        print(X)            ## 40，执行类本身定义的变量
    
        def m1(self):
            print(X)        ## 30，执行嵌套函数下定义的变量X
            
        def m2(self):
            X = 60          ## 覆盖嵌套函数的变量X
            print(X)        ## 执行当前函数下定义的变量X
    
    nested = NestedClass()  ## 20,是属于外部函数
    nested.m1()             ## 20
    nested.m2()             ## 30,本地变量隐藏全局变量
print(X) 
```



