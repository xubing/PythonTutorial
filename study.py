#! /usr/bin/env Python
#-*- coding:utf-8-*-
import sys
import os
import math
import pickle

print dir(os)

# test if statements   if ... elif ... elif ...
x= 2 #int(raw_input("enter a raw_int"))
if x==0:
	print 'x==0'
elif x==1:
	print 'x==1'
elif x==2:
	print 'x==2'
else:
	print 'more'

# for Statements 
a = ['cat', 'window', 'defenestrate']
for x in a:
	print x,len(a)

for x in a[:]: #进行获取整体
	if len(x)>6:
		a.insert(0, x)
print a

# The range() Function It generates lists containing arithmetic progressions:生成等差级数的链表
a =range(10)
print a
a= range(5,10)
print a
a = range(0,10,3)
print a

# 循环中带break ，contniu ，else。其中else是执行条件伟false的时候执行。
for n in range(2, 10):
	for x in range(2,n):
		if n%x==0:
			print n,'equals ',x,'*',n/x
			break
	else:
		print n ,'is a prime number'

# pass Statements  .pass 语句什么也不做。

#3.5 Defining Functions 。Keyword def，It must be followed by the function name and the parenthesized list of formal parameters.
#从函数体开始，必须进行锁进。
def fib(n):
	""" print a Fibonacci series up to n"""
	a,b=0,1
	while b<n:
		print b,
		a,b=b,a+b
f=fib #This serves as a general renaming mechanism。重名机制
f(2000)
#3.6  DefiningFunctions
#The return statement returns with a value from a function..不带表达式的return 返回None
#The statement result.append(b) calls a method of the list object result.
#3.7 More on Defining Functions 
#3.7.1 Default Argument Values 参数默认值

def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
         while True:
             ok = raw_input(prompt)
             if ok in ('y', 'ye', 'yes'): return True
             if ok in ('n', 'no', 'nop', 'nope'): return False
             retries = retries - 1
             if retries < 0: raise IOError, 'refusenik user'
             print complaint
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

#3.7.2 Keyword Arguments 
# 函数可以通过关键字参数的形式来调用。如 ‘keyword = value’ 这个不再区分参数的顺序
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
         print "-- This parrot wouldn’t", action,
         print "if you put", voltage, "volts through it."
         print "-- Lovely plumage, the", type
         print "-- It’s", state, "!"
#可以如下调用
parrot(1000)
parrot(action = 'VOOOOOM', voltage = 1000000)
parrot('a thousand', state = 'pushing up the daisies')
parrot('a million', 'bereft of life', 'jump')
#3.7.4 Unpacking Argument Lists  参数列表的分拆
#可以在调用函数时添加一个*操作符来自动把参数列表拆开。
#通用也可以用＊＊分拆关键参数为字典
range(3, 6)
#[3, 4, 5] # normal call with separate arguments
args = [3, 6]
range(*args)
#[3, 4, 5] # call with arguments unpacked from a list

# Lambda Forms 
#With the lambda keyword, small anonymous functions can be created.
def make_incrementor(n):
	return lambda x:x+n
f =make_incrementor(42)
print f;
print f(0)
print f(1)

#4 Data Structures
#4.1 More on x==2
#常用函数 append(x) extend(L) insert(i, x) remove(x) pop([i ]) index(x)
# reverse() sort() count(x)
a = [66.25, 333, 333, 1, 1234.5]
print a.count(333)
a.append(44)
a.index(333)
a.pop() #Using Lists as Stacks
a.reverse()
print a
a.pop(0) #Using Lists as Queues
print a
#4.1.3 Functional Programming Tools
#very useful when used with lists: filter(), map(), and reduce().

#4.2 The del statement
#The del statement can also be used to remove slices from a list or clear the entire list
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0] #equals pop()
del a[2:4]
print a
del a[:]
del a #del can also be used to delete entire variables:
#4.3 Tuples and Sequences 元组和序列
t = 12345, 54321, 'hello!'
print t[0],t[2]
#一个空的括号可以创建一个空元组，一个单元素的元组，可以在值后面跟一个逗号
empty = ()
singleton = 'hello',
print singleton
# 4.4 Sets
#A set is an unordered collection with no duplicate elements. 
#operations like union, intersection, difference, and symmetric difference
basket = ['apple','sss']
fruit = set(basket) 
print fruit  #set(['apple', 'sss'])
print 'sss' in fruit #True

#4.5 Dictionaries
tel = {'jack': 4098, 'sape': 4139}
print tel.has_key('guido') #has_key进行检测
a =dict([('sape', 4139),('jack', 4098)])
print a #{'sape': 4139, 'jack': 4098}
#When the keys are simple strings, it is sometimes easier to specify pairs using keyword arguments:
dict(sape=4139, guido=4127, jack=4098)
#4.6 Looping Techniques
#在字典中循环时，key value可以同时读出
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.iteritems():
	print k,v
#在序列中循环，可以读出索引位置和值

#同时循环两个或更多序列，可以用zip进行整体解读

# 5 module . 参见 study2.py
# A module is a file containing Python definitions and statements. 
# The file name is the module name with the suffix ‘.py’ appended.

#dir(var) lists all types of names: variables, modules, functions, etc.liec 
#dir() does not list the names of built-in functions and variables. If you want a list of those, they are defined in the standard module __builtin__:
#eg: 
#import __builtin__
#print dir(__builtin__)

#5.4 Packages
#The ‘__init__.py’ files are required to make Python treat the directories as containing packages; 


#6 Input and Output 
#repr() 或str()将会转化为字符
s = 'Hello, world.'
print str(s),str(0.1)
print repr(s),repr(0.1)
#格式化
#it always adds spaces between its arguments.
print 'PI is %.3f' % (math.pi),'ok，参数之间是空格，不能用逗号'
#如果超过一个字符串，需要用元组
for x in range(1,11):
    print '%2d %3d %4d' % (x, x*x, x*x*x)
#6.2   Reading and Writing Files
#open()returnsafileobject,andismostcommonlyusedwithtwoarguments:‘open(filename, mode)’
#f=open('./html.py','r')
#常用操作 read(), readline()
#print f.read()
#print f.readline()
#print f.readlines()
#for line in f:
#    print line
#python 提供pickle标准模块进行对象的类型转换
#pickle.dump(s,f)
#x =pickle.loads('123')
#print x
# 7 Errors and Exceptions
# 7.3 Handling Exceptions try except
while True:
    try:
        x = int(raw_input('input int'))
        break
    except ValueError:
        print "OOOOPS try again"
#可以多个except进行存在,每一个对应不同的类型:
#8 Classes
#类是C++和Modula－3的混合体。 允许多继承，派生类可以覆盖基类中的任何方法。方法可以调用基类中同名方法。对象可以包含任意数量的私有成员
#属性可以是只读或者写的。后一种情况下，可以对属性赋值，modname.the_answer = 42。可写的属性，也可以用del语句删除del modname.the_answer，会从modname对象中删除the_answer属性。
#8.3.1 Class Definition Syntax
class MyClass:
    "A simple example class" #这个是——doc__属性
    i = 1234
    def f(self):
        return 'hello world'

#实例化操作，倾向于将对象创建为有初始状态的.因此类会定义一个名为__init__（）的特殊方法
#def __init__(self): 
#    self.data=[]
x=MyClass()
x.i=100
print x.i
del x.i
print x.i

#8.5 Inheritance 继承
class DerivedClassName(MyClass):
    a='hello'
# 覆盖方法。如果派生类中只是想扩充而不是简单的替代基类中的重名方法，可以直接调用基类方法，Baseclass DerivedClassName(BaseClassName)
# 8.5.1 Multiple Inheritance 多继承。class DerivedClassName(Base1, Base2, Base3):  属性的规则是深度优先，从左到右
#struct An empty class definition will do nicely:
class Employee:
    pass
john = Employee() # Create an empty employee record
# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000
# Generators 生成器。
# 返回数据的时候用yield
f
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
for char in reverse('golf'):
    print char
#8.11 Generator Expressions )生成表达式 
print sum(i*i for i in range(10))
# 9 Brief Tour of the Standard Library 标准库
# 参见study2
