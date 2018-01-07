# -*- coding: utf-8 -*-
'''
create at 2018.01.07
@author scutpaul
'''

def now():
    print('2018-01-07')
f = now
f()

print("now.__name__ :",now.__name__)
print("f.__name__ :",f.__name__)
#now = 10
#print("now.__name__ :",now.__name__)
print("f.__name__ :",f.__name__)
'''
增加装饰器：
要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义
'''
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
'''
使用@log相当于now = log(now)
'''
@log
def now():
    print('2018-01-07')
print("\n装饰器")
now()
f = now
f()
'''
装饰器传入参数
效果相当于
now = log('execute')(now)
'''
def log(text): #参数传入
    print('test_log')
    def decorator(func): #函数传入
        print('test_func')
        i = [0] 
        def wrapper(*args, **kw): #函数体的参数传入
            i[0]=i[0]+1  #记得7_return_func中的程序闭包
            print("test_wrapper:",i)
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('Execute')
def now():
    print('2018-01-07')
print("传入参数的log")
f = now
f()
f()
'''
装饰器的实质是将返回一个函数应用到了
'''
print("实际上的装饰器是将放回函数应用了")
print("现在的now的函数名：",now.__name__)
#返回之后才会修改的。


'''
关于修改函数名的：
需要把原始函数的__name__等属性复制到wrapper()函数中，
否则，有些依赖函数签名的代码执行就会出错
不需要编写wrapper.__name__ = func.__name__这样的代码，
Python内置的functools.wraps就是干这个事的
'''
import functools

def log(func):
    @functools.wraps(func)#就是这一句大概就是实现 wrapper.__name__ = func.__name__
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
@log
def now():
    print('2018-01-07')
print("能自己修改过程中函数名的")
f = now
f()
f()

'''
针对带参数的：
import functools
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
'''

