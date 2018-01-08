# -*- coding: utf-8 -*-
'''
create at 2018.01.08
@author scutpaul
'''
'''
继承多个父类，而不是多层次继承
'''

class Animal(object):
    pass

# 大类:
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

# 
'''
狗会跑和哺乳动物
会跑-会飞
鸟类-哺乳类
排列组合
'''

class Runnable(object):
    def run(self):
        print('Running...')

class Flyable(object):
    def fly(self):
        print('Flying...')
        
'''
Dog 继承两个父类
'''
class Dog(Mammal, Runnable):
    pass


'''
设计类别继承时，需要有一个主线，其他就是额外功能的实现了。MixIn
如小狗主类是动物；mixin跑、肉食性
class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
    pass
编写一个多进程模式的TCP服务
class MyTCPServer(TCPServer, ForkingMixIn):
    pass
编写一个多线程模式的UDP服务
class MyUDPServer(UDPServer, ThreadingMixIn):
    pass
一个更先进的协程模型
class MyTCPServer(TCPServer, CoroutineMixIn):
    pass
'''


'''
'''
'''
1.有两个基类A和B,A和B都定义了方法f(),C继承A和B,那么调用C的f()方法时会出现不确定。
2.有一个基类A，定义了方法f()，B类和C类继承了A类（的f()方法），D类继承了B和C类，那么出现一个问题，D不知道应该继承B的f()方法还是C的f()方法

'''
"""

#1.
class A(object):
    def f(self):
        print "A"

class B(object):
    def f(self):
        print "B"

class C(B,A):
    pass
c = C()
c.f()#会输出什么?

#"A" or "B"

#结论:输出什么的决定性因素是C在继承父类时的顺序!

#即靠近左边的先输出!
"""

#2.
class A(object):
    def f(self):
        print ("A")

class B(A):
    def f(self):
        print ("AB")
class C(A):
    def f(self):
        print ("CA")

class D(C,B):
    pass

d = D()
d.f()

#输出AB--取决于继承的顺序