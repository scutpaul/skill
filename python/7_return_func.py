# -*- coding: utf-8 -*-
'''
create at 2018.01.07
@author scutpaul
'''
'''
懒计算、等到要用到才计算
'''
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
'''
将返回的函数赋值给变量，变量可以多次调用
'''
f = lazy_sum(1,2,3)
print(f())


'''
程序的闭包
当一个函数返回了一个函数后，其内部的局部变量还被新函数引用
返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
'''
def count():
    fs = []
    for i in range(1, 4):
        print(i)#在赋值的时候已经执行只是return的函数没计算而已
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1)
print(f2)
print(f3)
print(f1(),f2(),f3())

'''
如果一定要引用循环变量怎么办？
方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，
无论该循环变量后续如何更改，已绑定到函数参数的值不变
'''
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        print(i)
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
print("")
'''
lambda解决
'''
def count_():
    fs = []
    def f(j):
        return lambda :j*j
    for i in range(1, 4):
        print(i)
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
print("解决变量绑定")
f1, f2, f3 = count_()
print(f1,f2,f3)
print(f1(),f2(),f3())

'''
利用闭包返回一个计数器函数，每次调用它返回递增整数
'''
print("闭包计数器")
#list
def createCounter():
    i = [0]
    def counter():
        i[0] = i[0]+1
        return i[0]
    return counter
#生成器方法：
def createCounter_():
    def f():
        n = 0
        while True:
            n += 1
            yield n
    sum = f()
    def counter():
        return next(sum)
    return counter
#全局变量方法
def createCounter__():
    i = 0
    def counter():
        nonlocal i #加上这句之后就可以了
        i += 1
        return i
    return counter

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
