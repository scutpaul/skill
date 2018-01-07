# -*- coding: utf-8 -*-
'''
create at 2018.01.07
@author scutpaul
'''

__author__ = 'scutpaul'

class Student(object):
#object为继承的类
    def __init__(self,name,score):
        self.name = name
        self.score = score
# __init__的第一个参数必须是self，表示示例本身，可以把各种属性绑定到self,
# 创建实例时必须传入与__init__的形参（self除外）相匹配的参数
    def print_score(self):
        print('%s : %s'%(self.name,self.score))
# 第一个参数为self，调用函数的话使用过实例调用的
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >60:
            return 'C'
        else:
            return 'F'
        
        
if __name__ == '__main__':
    chen = Student('chen',95)
    chen.print_score()
    print(chen)
    print(chen.get_grade())
    bart = Student('Bart Simpson', 59)
    bart.age = 18
    print(bart.age)
    
'''
和静态语言不同，Python允许对实例变量绑定任何数据，
对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同
'''

