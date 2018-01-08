# -*- coding: utf-8 -*-
'''
create at 2018.01.07
@author scutpaul
'''
'''
将get_score的方法弄得像一个变量！
'''
class Student_(object):

    def get_score(self):
         return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
'''
上面是set_score
下面使用装饰器
'''
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.score = 60# OK，实际转化为s.set_score(60)
print(s.score)# OK，实际转化为s.set_score()

'''
我们在对实例属性操作的时候，就知道该属性很可能不是直接暴露的，而是通过getter和setter方法来实现的。
还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：
'''
class Student__(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth

'''
练习
'''
class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,value):
        self._width = value
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,value):
        self._height = value
    @property
    def resolution(self):
        return self._width*self._height
    
# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')