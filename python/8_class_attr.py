# -*- coding: utf-8 -*-
'''
create at 2018.01.07
@author scutpaul
'''
'''
类属性与实例属性
'''

class Student(object):
    def __init__(self, name):
        self.name = name

s = Student('Bob')
s.score = 90
print(s)

class Student(object):
    name = 'Student'
s = Student()
print("s",s.name)#当实例属性没有时,查找类属性
print("student",Student.name)
s.name = 'Michael' # 给实例绑定name属性
print("实例绑定name后的s",s.name)
del s.name # 如果删除实例的name属性
print("删除后的s",s.name)


'''
测试
'''
class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count+=1

# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')
