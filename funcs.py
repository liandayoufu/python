#!/bin/env python
# coding=utf-8
# function  study notes

def power(x,n=2):
    s=1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print power(5)
print power(2,10)
print

# 函数定义时设定默认值
def register(name,gender,City='Shanghai'):
    print 'name:',name
    print 'gender:',gender
    print 'City:',City
register('Bob','M')
register('Huan','F',City='徐州')
print

def add_end(L=None):
    if L is None:
        L = []
    L.append('end')
    return L
print add_end([1,2,3])
print add_end()
print add_end()

def add_end(L=[]):
    L.append('end')
    return L
print add_end([1,2,3])
print add_end()
print add_end()

# 函数接收list或tuple作为参数
def calc(nums):
    sum = 0
    for n in nums:
        sum = sum + n * n
    return sum
print calc([1,2,3,4])
print calc((1,2,3,4,5))
print

# 可变参数 *
def calc1(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print '*numbers作为可变参数：'
print calc1(1,2,3,4)
print calc1(2,3,4,5,6)
print '分别传入list 或*list传入所有：'
numbers=[1,3,5,7]
print calc1(numbers[0],numbers[1],numbers[2])
print calc1(*numbers)

# 关键字参数 **
def person(name,age,**kw):
    print 'Name:',name
    print 'Age:',age
    print 'Addition:',kw
person('Bob','28')
person('Bob','28',City='Shanghai',Xifuer='Huanhuan')

# 参数组合
def func(a,b,c=0,*args,**kw):
    print 'a=',a,'b=',b,'c=',c,'args=',args,'opts=',kw
func('Bob','is','a','good','nice',attr1='Man',attr2='Xman')
func(1,2)
args = (1,2,3)
kw = {'xfer':'Huanhuan','gg':'dalian'}
func(*args,**kw)

# 递归函数
def fact(n):
    if n == 1:
        return 1
    return  n * fact(n-1)
print
print fact(1)
print fact(2)
print fact(5)
#print '100!=', fact(100)
print '999!=', fact(999)

# 尾递归
def fact(n):
    return fact_iter(1,1,n)

def fact_iter(product,count,max):
    if count > max:
        return product
    return fact_iter(product*count,count+1,max)
print '10!=',fact(10)

