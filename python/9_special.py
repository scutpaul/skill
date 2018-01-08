# -*- coding: utf-8 -*-
'''
create at 2018.01.08
@author scutpaul
'''
'''
__str__

直接显示变量调用的不是__str__()，而是__repr__()，
两者的区别是__str__()返回用户看到的字符串，
而__repr__()返回程序开发者看到的字符串，
也就是说，__repr__()是为调试服务的。
'''

class Student(object):
    pass
chen = Student()
print("实例的__str__：",chen)

class Student_(object):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return 'Student_ object (name :%s)'% self.name
    __repr__ = __str__#将在python直接显示变量的换成好看的str~
    
chen = Student_('chen')
print("重载__str__后的：",chen)

'''
__iter__
'''
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值
'''
__iter__
如果一个类想被用于for ... in循环，类似list或tuple那样，
就必须实现一个__iter__()方法，该方法返回一个迭代对象，
然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，
直到遇到StopIteration错误时退出循环
'''
class Fib(object):
    def __init__(self):
        self.a,self.b = 0,1
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b = self.b,self.a+self.b
        if self.a>100000:
            raise StopIteration()
        return self.a
    
for n in Fib():
    print(n)
    
'''
__getitem__

可以取第N个元素
Fib()[5]
'''
class Fib(object):
    def __getitem__(self,n):
        a,b = 1,1
        for x in range(n):
            a,b = b,a+b
        return a
print(Fib()[10])
#__getitem__就是对传入的[]进行处理
class Fib(object):
    def __getitem__(self,n):
        if isinstance(n,int):
            a,b = 1,1
            for x in range(n):
                a,b = b,a+b
            return a
        if isinstance(n,slice):
            start = n.start
            stop = n.stop
            if start == None:
                start = 0
            a,b = 1,1
            L = []
            for x in range(stop):
                if x>=start:
                    L.append(a)
                a,b = b,a+b
            return L
print("__getitem__",Fib()[:5])
'''
__setitem__ __delitem__
'''
'''
__getattr__
只有在没有找到属性的情况下，才调用__getattr__，
已有的属性，比如name，不会在__getattr__中查找
'''
class Student(object):
    def __init__(self):
        self.name = 'chen'
    def __getattr__(self,attr):
        if attr == 'age':
            return 19
        raise AttributeError('Student object has no attribute:%s'% attr)
#要让class只响应特定的几个属性，我们就要按照约定，抛出AttributeError的错误：
cheng = Student()
print("get_attr_",cheng.age,cheng.name)
#print(cheng.score)

'''
__getattr__
API动态的调用
'''
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__
    
print("动态调用:",Chain().status.user.timeline.list)
'''
__call__
__call__()还可以定义参数。
对实例进行直接调用就好比对一个函数进行调用一样，
所以你完全可以把对象看成函数，把函数看成对象，
因为这两者之间本来就没啥根本的区别
'''
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)
s = Student('Michael')
s()
'''
Callable:
    一个对象可以被调用
'''
print("\n是否可以被调用（含call）")
print("Student'callable:",callable(Student))
print("max'callable:",callable(max))
print("list'callable:",callable([1,2,3]))
print("None'callable:",callable(None))
print("str'callable:",callable('str'))
'''
GET /users/:user/repos
Chain().users('michael').repos
user('**')会调用__call__(**)的。
'''
print("\n动态实现:user('***')")
class Chain(object):
    def __init__(self,path=''):
        self._path = path
    
    def __getattr__(self,attr):
        if attr == 'users':
            return Chain('/%s'%attr)
        return Chain('%s/%s'%(self._path,attr))
    
    def __call__(self,path=''):
        return Chain('%s/%s'%(self._path,path))
    
    def __str__(self):
        return self._path
    __repr__ = __str__    
        
print(Chain().users('michael').repos)
'''
先把user定义出来
'''
class Chain(object):
    def __init__(self, path=''):
        self._path = path
    def users(self,name):
        return Chain('%s/users/%s' % (self._path, name))
    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))
    def __str__(self):
        return self._path
    __repr__ = __str__
print(Chain().users('michael').repos)

'''
链式调用的方法就是先执行第一个调用方法，这个方法返回自身，
这样就可以继续调用第二个方法，
'''
class Person:  
    def name(self, name):  
        self.name = name  
        return self  

    def age(self, age):  
        self.age = age  
        return self  

    def show(self):  
        print ("My name is", self.name, "and I am", self.age, "years old." )  

p = Person()  
p.name("Li Lei").age(15).show()