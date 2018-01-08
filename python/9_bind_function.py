# -*- coding: utf-8 -*-
'''
create at 2018.01.07
@author scutpaul
'''

'''
绑定方法
'''

class Student(object):
    pass

s = Student()
s.name = 'chen'
print(s.name)

def set_age(self, age):
    self.age = age
from types import MethodType
s.set_age = MethodType(set_age, s) # 给实例绑定一个方法

s.set_age(25) # 调用实例方法
print("测试加入方法:",s.age)

'''
为类加上类方法
'''
def set_score(self, score):
    self.score = score
Student.set_score = set_score
s2 = Student()
s2.set_score(11)
print("加入类方法",s2.score)

'''
__slots__可以限制实例的属性：不随便加
'''
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
#Student只能加限制的属性
s = Student() # 创建新的实例
s.name = 'chen'
#s.score=33#不行的
'''
__slots__仅对当前的类有效，对子类无效
'''

    
