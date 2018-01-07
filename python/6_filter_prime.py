# -*- coding: utf-8 -*-
'''
create at 2018.01.07
@author scutpaul
'''
'''
生成素数
'''
#产生器
def _odd_filter(): 
    n = 1
    while(True):
        n = n+2 
        yield n
# 过滤规则
def _not_divisible(n):
    return lambda x: x%n > 0
#过滤器
def primes():
    yield 2
    it = _odd_filter() #init
    while True:
        n = next(it) #get next
        yield n 
        it = filter(_not_divisible(n),it) #filter
#打印  
for n in primes():
    if n<1000:
        print(n)
    else:
        break
