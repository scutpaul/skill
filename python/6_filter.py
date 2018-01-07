# -*- coding: utf-8 -*-
'''
create at 2018.01.07
@author scutpaul
'''
'''
和map()类似，filter()也接收一个函数和一个序列。
和map()不同的是，filter()把传入的函数依次作用于每个元素，
然后根据返回值是True还是False决定保留还是丢弃该元素。
'''

'''
只取奇数
'''
def odd(n):
    return n%2 == 1
L = range(10)
print("只取奇数：",list(filter(odd,L)))

'''
去空格
'''
def not_empty(s):
    return s and s.strip()
L = 'hello my name is chen haoxin'
print("去空格",list(filter(not_empty,L)))
