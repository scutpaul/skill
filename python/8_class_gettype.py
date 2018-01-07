# -*- coding: utf-8 -*-
'''
create at 2018.01.07
@author scutpaul
'''
'''
type()获取类别
'''
print(type(None))
print(type(1))
print(type('str'))
print(type(abs))
print(type('str')==str)
'''
types模块判断一个对象是否有函数
'''
import types
def fn():
    pass

print(type(fn)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x:x*x)==types.LambdaType)
print(type(x for x in range(10)) == types.GeneratorType)

'''
isinstance()对于继承的关系更方便
可以识别到父类
'''

'''
使用dir()获取此类的所有属性与方法
'''
#####################################print(dir('abc'))
#len('abc')等价于 'abc'.__len__()
'''
配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：
'''
print("\n\n\nhasattr")
class MyObject(object):
    def __init__(self):
        self.x =9
    def power(self):
        return self.x*self.x
    
obj = MyObject()
print("是否有x属性",hasattr(obj,'x'))
print("是否有y属性",hasattr(obj,'y'))
setattr(obj,'y',19)
print("设置y属性之后",hasattr(obj,'y'))
#print(dir(obj))
print("获取y属性的值",getattr(obj,'y'))
#获取不存在的属性的时候会抛出AttributeError的错误
#或者设置默认值
print("获取zz属性没有的默认",getattr(obj,'z',404))

'''
只有在不知道属性的直接获取方法，才去使用attr()
'''

'''
正确使用的姿势
'''

def readImage(fp):
    def read(fp):
        pass
    if hasattr(fp, 'read'):#先确认是否有该方法
        return read(fp)
    return None




