# -*- coding: utf-8 -*-
'''
create at 2018.01.06
@author scutpaul
'''
'''
变量可以指向函数
以下以abs为例
'''
#
print("关于abs的指向")
print("abs:",abs)
a = abs
print("a:",a)
#abs = 10
print("after_abs:",abs)
print("after:",a)

def add(x,y,f):
    return f(x)+f(y)

print(add(-1,-2,abs))

'''
编写高阶函数，就是让函数的参数能够接收别的函数。
*****
把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。
'''