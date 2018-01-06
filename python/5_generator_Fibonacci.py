# -*- coding: utf-8 -*-

'''
create at 2018.01.06
@author scutpaul
'''
'''
函数实现
'''
def fibonacci(_max):
    n,a,b = 0,0,1
    while n< _max:
        print (b)
        a,b = b,a+b
        n = n+1
    return 'done'

fibonacci(5)
'''
生成器生成
遇到yeild就返回
'''
def fib(_max):
    n,a,b = 0,0,1
    while n< _max:
        yield (b)
        a,b = b,a+b
        n = n+1
    return 'done'
print("yield_fid:")
for i in fib(6):
    print(i) 
    
print("yield_fib的return")
g = fib(6)
while True:
    try:
        x = next(g)
        print (x)
    except StopIteration as e:
        print("Generator end value",e.value)
        break
'''

'''
