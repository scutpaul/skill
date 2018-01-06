# -*- coding: utf-8 -*-

'''
create at 2018.01.06
@author scutpaul
'''

#for_in
d = {'a':1,'b':2,'c':3}
#dict 支持整型的
#ss = {3:1,4:2}

for key in d:
    print(key)
#str 
str1 = 'chen'
for ch in str1:
    print(ch)
    
    
#判断是否可迭代
print("判断是否可迭代")
from collections import Iterable
print("str",isinstance('abc',Iterable))
print("list",isinstance([1,2,3], Iterable))
print("int",isinstance(123, Iterable)) 

#enumerate 把一个list变成索引-元素对
print("enumerate 把一个list变成索引-元素对")
for i, value in enumerate(['A', 'B', 'C']):
    print(i,value)
print("多变量迭代")
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x,y)


