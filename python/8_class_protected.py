# -*- coding: utf-8 -*-
'''
create at 2018.01.07
@author scutpaul
'''

'''
内部属性不被改变！
变量头部加入'__'就是private
要注意的是：！！
双下划线开头的实例变量是不是一定不能从外部访问呢？
其实也不是。不能直接访问__name是因为Python解释器-
-对外把__name变量改成了_Student__name，
所以，仍然可以通过_Student__name来访问__name变量

'''
class student(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score
    def get_name(self):
        print(self.__name)
    def get_score(self):
        print(self.__score)
    def set_name(self,name):
        self.__name = name
    def set_score(self,score):
        self.__score = score
        
if __name__=='__main__':
    chen = student('chen',100)
    chen.get_name()
    chen.get_score()
    chen.set_name('hao')
    chen.get_name()
    chen._student__name = 'xin'#还是可以改的
    chen.get_name()