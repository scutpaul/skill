# -*- coding: utf-8 -*-
'''
create at 2018.01.07
@author scutpaul
'''
'''
在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便
匿名函数有个限制，就是只能有一个表达式
'''
'''
例子
'''
L = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print("list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))\n",L)
#关键字lambda表示匿名函数，冒号前面的x表示函数参数
print("关键字lambda表示匿名函数，冒号前面的x表示函数参数")

'''
匿名函数有个限制，就是只能有一个表达式
'''
f = lambda x: x * x
print(f)
print(f(4))
'''
lambda作为返回值
'''
def build(x, y):
    return lambda: x * x + y * y
print(build(1,2))
print(build(1,2)())

'''
lambda改写函数
'''
print("\nlambda改写函数")
def is_odd(n):
    return n % 2 == 1
L = list(filter(is_odd, range(1, 20)))
print(L)
L = list(filter(lambda x:x%2==1,range(1,20)))
print("改写之后",L)