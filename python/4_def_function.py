# -*- coding: utf-8 -*-


def my_abs(x):
    if x>=0:
        return x
    else:
        return -x
print (my_abs(-1))


def nop():
    pass

print('pass是作为占用符，什么都不做，占坑')

#参数检查
#要自己设置
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
    
print(my_abs(-1))

#返回多值
print("测试多值返回")
def return_two():
    return 1,2
x , y = return_two()
print("x:",x,"y:",y)
z = return_two()
print("z",z)

#默认参数
print("默认参数")
def test_default(a,b=2,c='a'):
    return a+b
print("test_default(1)=",test_default(1))
print("test_default(1,3)=",test_default(1,3))
print("test_default(1,c='jiji')=",test_default(1,c='jiji'))
print("如果使用默认list要注意了")
print("定义默认参数要牢记一点：默认参数必须指向不变对象！")

def add_end(L=[]):
    L.append('END')
    return L
print(add_end())
print(add_end())

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
print(add_end())
print(add_end())
#可变参数
print("\n可变默认参数")
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print("使用list即可")
print("calc([1,2,3])=",calc([1,2,3]))
print("但是这要构造[1,2,3]")
#关键字
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print("calc(1,2,3)=",calc(1,2,3))
print("这样加上*就在函数构造一个tuple")
print("使用list传入呢：")
num = [1,2,3]
print("calc(*num)=",calc(*num))

#关键字参数
print("(**num)关键字整合成一个dict")
def key_num(a,**num):
    print("a:",a,"num:",num)
    
print('默认为空的',key_num(1))
print(key_num(1,name='chen',age=20))
extra={'name':'chen','age':20}
print(key_num(1,**extra))

#限制传入关键字
print("关键字的传输")
def person(name, age, *, city, job):
    print(name, age, city, job)
person('Jack', 24, city='Beijing', job='Engineer')
#从这里开始*args关键字了
print("\ncity与job必须加入关键词")
def person(name, age, *args, city, job):
    print(name, age, args, city, job)
print(" person('Jack', 24, city='Beijing', job='Engineer')")
person('Jack', 24, city='Beijing', job='Engineer')
print("这里的name\age是位置参数，city\job是关键字参数")