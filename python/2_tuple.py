# -*- coding: utf-8 -*-

print("元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改")
classmates = ('Michael', 'Bob', 'Tracy')
print("classmates:",classmates)
print("所以tuple更加安全")

print("tuple的不变性")
tuple = ("a","b",["1","2"])
print("tuple = (\"a\",\"b\",[\"1\",\"2\"])\n",tuple)
tuple[2][0] = '3'
tuple[2][1] = '4'
print("改变后的tuple",tuple)
print("变的不是tuple而是list指向变了")

print("\ntuple中保存的是内存地址：")
list_ = [1,2]
list_1 = ["A","B"]
test = (list_,list_1)
test_list = test[0]
print("初始化-------------")
print("list",list_)
print("test",test)
print("改变list的整体-----------")
list_ = [3,4]
print("list",list_)
print("test",test)
print("so：list改变指向")
print("改变list内的一个------------")
list_[0] = 1
print("list",list_)
print("test",test)
print("so:List是全新的了")
print("重新将list指向回来------------")
list_ = [1,2]
list_[0] = 3
print("list",list_)
print("test",test)
print("test_list->tuple[0]",test_list)
print("so:即使将list指向回原常量，改变不了tuple")
print("直接修改tuple-------------")
test[0][1] = 3
print("list",list_)
print("test",test)
print("test_list->tuple[0]",test_list)
print("so:只有直接改变tuple内的才可以。自带的test_list也改变")
print("修改list_1---------------")
list[1] = "D"
print("list_1",list_1)
print("test",test)
print("so:tuple内list是无法独自修改的")
print("修改tuple内的--------------")
test[1][0] = "D"
print("list_1",list_1)
print("test",test)
print("so:只有通过tuple[][]才可改变")

print("\ntuple(list)是如何？")
list_1 = [1]
tuple_1 = (list_1)
print("初始化-------------------")
print("list_1",list_1)
print("tuple_1",tuple_1)
tuple_1[0] =14
print("改变tuple-----------")
print("list_1",list_1)
print("tuple_1",tuple_1)
print("这种方法并不是一种Tuple")

print("\n测试一个元素的初始化")
tuple_2 = (1,)
print("tuple_2 = (1,)\n",tuple_2)