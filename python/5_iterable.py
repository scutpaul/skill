# -*- coding: utf-8 -*-

'''
create at 2018.01.06
@author scutpaul
'''
'''
我们已经知道，可以直接作用于for循环的数据类型有以下几种：
一类是集合数据类型，如list、tuple、dict、set、str等；
一类是generator，包括生成器和带yield的generator function。
这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。
可以使用isinstance()判断一个对象是否是Iterable对象
'''

#判断是否为可迭代
print("是否可迭代")
from collections import Iterable
list_ = []
dict_ = {}
str_ = 'ab'
print("list_is_iterable:",isinstance(list_,Iterable))
print("dict_is_iterable:",isinstance(dict_,Iterable))
print("str_is_iterable:",isinstance(str_,Iterable))
print("list_generator_is_iteratable",isinstance((x for x in range(10)), Iterable))

#判断是否为迭代器
print("是否为迭代器")
from collections import Iterator
print("list_is_iterator:",isinstance(list_,Iterator))
print("dict_is_iterator:",isinstance(dict_,Iterator))
print("str_is_iterator:",isinstance(str_,Iterator))
print("list_generator_is_iterator",isinstance((x for x in range(10)), Iterator))

#iter
print("使用iter使之成为迭代器")
print("list_iter_is_iterator:",isinstance(iter(list_),Iterator))
print("dict_iter_is_iterator:",isinstance(iter(dict_),Iterator))
print("str_iter_is_iterator:",isinstance(iter(str_),Iterator))

'''
iterator并不存储

这是因为Python的Iterator对象表示的是一个数据流，
Iterator对象可以被next()函数调用并不断返回下一个数据，
直到没有数据时抛出StopIteration错误。
可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，
只能不断通过next()函数实现按需计算下一个数据，
所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
'''
#迭代中修改
list_test = [1,2,3,4,5]
for x in list_test:
    print (x)
    list_test.pop()