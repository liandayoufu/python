__author__ = 'Bob Xu'
# coding=utf-8
#!/bin/env python

L=[]
i = 1
while i < 100:
    L.append(i)
    i += 2
print L

print "切片，从下标为0开始，0可以省略不写，到下标为5结束，但不显示5，"
print L[:5],L[5:10]
print L[-1:],L[-1],L[-9:-1]

print "第三位表步进"
L = range(100)
print L[10:21],L[::5],L[1:11:2]
print L[:]
print (1,2,3,4,5,6,7)[:4]
T = range(10)
print T

print "迭代"
for i,v in enumerate(['a','b','c']):
    print i,v

L=[]
for x in  range(1,11):
    L.append(x*x)
print
print L
print [x*x for x in range(1,11) if x%2==0]

print "for循环其实可以同时使用两个甚至多个变量，比如dict的iteritems()可以同时迭代key和value："
dic = {'Gege':'Huanhuan','an':'aini'}
for k,v in dic.iteritems():
    print k,'=',v

print "列表生成式也可以使用两个变量来生成list"
print [v + '=' + k for k,v in dic.iteritems()]

print "把一个list中所有的字符串变成小写"
L = ['apple','ibm','intel','google']
print [ s.upper() for s in L]

print [m + n for m in 'ABC' for n in 'XYZ']

print "高阶函数"
def add(x,y,f):
    return f(x) + f(y)
print add(2,-5,abs)

print "计算一个List内所有数乘积"
def prod(x,y):
    return x * y
print "reduce函数：reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)"
print "求1到5乘积:",reduce(prod,range(1,6))

print "把一个list中的字母都变成首字母大写，其他小写"
def format(s):
    return s[0].upper() + s[1:].lower()
print "首字母大写其他小写：",map(format,L)

#L1 = []
#name = raw_input('Pl input your name:')
#while name != 'quit':
#    L1.append(name)
#    name = raw_input('Pl input your name:')
#print map(format,L1)

print  "filter函数 内置的过滤函数，Ture则保留"
def is_odd(n):
    return n % 2 == 1
print filter(is_odd,[1,2,3,4,5,6,7,8,9,0])
print "筛选奇数：",filter(is_odd,range(1,100))

# 找出素数
def is_prime(n):
    for i in range(2,n-1):
        if n % i != 0:
            i+=1
        else:
            return 0
            exit
    return 1
print is_prime(5)
print "筛选素数：",filter(is_prime,range(1,100))

# 排序 倒序
def reverse_cmp(x,y):
    if x < y:
        return 1
    if x > y:
        return -1
    return 0
print sorted([1,2,3,4,5,7456,2334,10],reverse_cmp)
L0 = ['Alice','Bob','bob','cat','David','nani']
print "直接排序：",sorted(L0)
print "逆序排序：",sorted(L0,reverse_cmp)

# 忽略大小写
def ignore_case_cmp(s1,s2):
    t1 = s1.upper()
    t2 = s2.upper()
    if t1 < t2:
        return -1
    if t1 > t2:
        return 1
    return 0
print "忽略大小写排序：",sorted(L0,ignore_case_cmp)

print "返回函数"
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

def calc_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f = calc_sum(1,3,5,7,9)
print "f",f
print "f()",f()
