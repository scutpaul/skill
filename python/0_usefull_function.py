# -*- coding: utf-8 -*-
'''
create at 2018.01.06
@author scutpaul
'''

'''
isinstance(变量,类型)
'''
x = 123
x_is_int = isinstance(x,int)
print("x is int:",x_is_int)

'''
enumerate 把一个list变成索引-元素对
'''
print("enumerate 把一个list变成索引-元素对")
for i, value in enumerate(['A', 'B', 'C']):
    print(i,value)

'''
如果是temp = num，那么相当于temp和num指向了同一个对象，
这样如果num改变，temp会跟着改变，所以需要用temp = num[:]
来复制一个当前num的副本，这样num改变就不会影响到temp的值
'''
'''
我们已经知道，可以直接作用于for循环的数据类型有以下几种：
一类是集合数据类型，如list、tuple、dict、set、str等；
一类是generator，包括生成器和带yield的generator function。
这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。
可以使用isinstance()判断一个对象是否是Iterable对象
'''
'''
使用reduce 将列表转成数字
'''
from functools import reduce
def trans_to_in(x,y):
    return x*10+y
print("reduce(trans_to_in,[1,3,5,7,9])",reduce(trans_to_in,[1,3,5,7,9]))

'''
lambda
'''

'''
str title首字母大写
'''
print('CHHH'.title())
'''
str split
'''
s = '123.456'
s = s.split('.')
print('s.split:',s)

import time
start = time.clock()#程序自开始运行的时间：s为单位