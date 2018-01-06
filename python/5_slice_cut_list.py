# -*- coding: utf-8 -*-
'''
create at 2018.01.06
@author scutpaul
'''
L = [0, 1, 2, 3, 4]
print(L)

#切片
#List
print("切片：L[0:2] = ",L[0:2])
print("切片由0至2，不包括2")
print("L[-2:0]",L[-3:-1])
L = list(range(100))
print("前十个数",L[:10])
print("后十个数",L[-10:])
print("前十个间隔取",L[:10:2])
print("每5个取一个",L[::5])

#tuple
tuple_test = (1,2,3,4,5)
print("tuple:",tuple_test[:2])
#结果也是tuple

#str
str1 = "hello my name is haoxin chen"
print("str间隔取",str1[::2])

