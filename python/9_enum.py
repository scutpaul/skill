# -*- coding: utf-8 -*-
'''
create at 2018.01.08
@author scutpaul
'''
'''
枚举类型定义一个class类型，然后，每个常量都是class的一个唯一实例
'''
from enum import Enum ,unique
Month = Enum('Months', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

@unique
class Week(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Web = 3
    Thu = 4
    Fri = 5
    Sat = 6
    #HHH = 6

'''
@unique装饰器可以帮助我们检查保证没有重复值。
'''
day1 = Week.Mon
print(day1)
print(Week['Mon'])
print(Week.Sat.value)
for name,member in Week.__members__.items():
    print(name,'=>',member,',',member.value)
'''

既可以用成员名称引用枚举常量，又可以直接根据value的值获得枚举常量。

Enum可以把一组相关常量定义在一个class中，且class不可变，而且成员可以直接比较。
'''

'''
测试
'''

class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        # 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')
