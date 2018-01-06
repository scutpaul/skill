# -*- coding: utf-8 -*-

def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)

print(fact(10))

##关于尾递归
'''
尾递归：通过返回值是一个函数
如下fact_item返回还是fact_item
'''
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

print(fact(10))