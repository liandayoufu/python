#!/usr/bin/env python
# coding=utf-8
# 面向对象编程 OOP
from types import MethodType
class Student(object): # 表示该类是从哪个类继承下来的，（object)则表示继承所有的类
    def __init__(self,name,score):  # __init__以两个划线开头的是private method 私有方法，不可以被外部调用，__init__方法的第一个参数永远是self表示创建的实例本身
        self.name = name
        self.score = score

    def print_score(self):
        print '%s: %s' % (self.name, self.score)


bob = Student("bob",100)
bob.name
bob.score
bob.print_score()

# 访问限制
class Stu(object):
    def __init__(self,name,score):
        self.__name = name      # __name 私有变量，不可外部直接访问，Bob._Stu__name()也是可以访问到的，
        self.__score = score
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def print_score(self):
        return self.__name,self.__score
# 如果变量名为_name 一个下划线，这样的变量实际外部是可以直接访问的，但是按照约定成俗的规定，看到这样的变量意思就是：虽然可以被访问，但是请当成私有变量不要随意访问
Bob = Stu("Bob",100)
print Bob.get_name()
print Bob.get_score()
print Bob.print_score()

# 获取对象信息
# dir() 获取对象所有方法和属性 getattr() setattr() hasattr() 分别获取、设置属性，判断对象是否有该属性
getattr(Bob,"get_name") # 也可以获取对象的方法
getattr(Bob,'a',404) # 如果获取属性失败就返回一个默认值404

class Animal(object):
    pass

a = Animal()
a.name = "Dog"  # 动态给实例绑定一个属性
print a.name

# 也可以给实例动态绑定方法
def set_type(self,type):
    self.type = type

# from types import MethodType
a.set_type = MethodType(set_type,a,Animal) # 给实例a绑定方法，
a.set_type = "沙皮"

b = Animal()    # 只给实例绑定方法，新建实例不可用，
b.set_type = "牛头梗"

Animal.set_type = MethodType(set_type,None,Animal) # 给class绑定方法，后新建的实例都可以直接调用方法

### `__slots__` 变量限制类可以给class添加的属性
class Book(object):
    __slots__ =  ('name','category')

bshell = Book
bshell.name = "Bash Shell scripting"
bshell.category = "Linux script programming"
bshell.author = "linus" # 会报错Book没有author这个属性

## @property Python的内置装饰器(decorator),负责把方法变成属性来调用

class Student(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError("Score must be a integer")
        if value < 0 or value > 100:
            raise ValueError("must between 0 ~ 100")
        self._score = value

Lidia = Student()
Lidia.score = 101

## __str__() 返回用户看到的字串  __repr__() 返回开发看到的字串

class Myobject(object):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return "Myobject object (name: %s)" % self.name
    __repr__ = __str__

# __iter__ 让一个可迭代的类可以用于for ... in ...循环

# 斐波列那数列
class Fib(object):
    def __init__(self):
        self.a,self.b = 0,1
    def __iter__(self):
        return self
    def next(self):
        self.a,self.b = self.b,self.a + self.b
        if self.a > 1000:
            raise StopIteration()
        return self.a

for n in Fib():
    print n,

class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                    a, b = b, a + b
            return L








