# -*- coding: utf-8 -*-
'''
create at 2018.01.07
@author scutpaul
'''

'''
python 内置map reduce!
'''
def multi(x):
    return x*x

r = map(multi,[1,2,3,4,5,6,7,8,9])
#map(第一个参数、结果r是一个迭代器。通过list将它导出)
print("第一个参数、结果r是一个迭代器。通过list将它导出")
L = list(r)
print(L)


'''
map是作为高阶函数，可以将其他函数作为参数的。
'''
print("list(map(str,[1,2,3,4]))=",list(map(str,[1,2,3,4])))

'''
reduce 
reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
'''
print("\nreduce")

print("reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)")
from functools import reduce
def add(x, y):
    return x+y

print("reduce(add,[1,3,5,7,9])=",reduce(add,[1,3,5,7,9]))

def trans_to_in(x,y):
    return x*10+y
print("reduce(trans_to_in,[1,3,5,7,9])",reduce(trans_to_in,[1,3,5,7,9]))

'''
应用例子：
str2in
'''


