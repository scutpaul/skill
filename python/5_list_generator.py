# -*- coding: utf-8 -*-
'''
create at 2018.01.06
@author scutpaul
'''
#列表生成list(range(1, 11))
print("list(range(1, 11))=",list(range(1, 11)))

'''
进阶版生成
[1*1,2*2,3*3]
'''
print("进阶版")
print("[x*x for x in range(1,11)] = ",[x*x for x in range(1,11)])

'''
再次进阶
[m1+n1,m2+n2,m3+n3]
'''
print("再进阶")
print("[m + n for m in 'ABC' for n in 'XYZ']:\n",
      [m + n for m in 'ABC' for n in 'XYZ'])

'''
用于多变量
'''
print("多变量for")
d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.items():
    print(k,'=',v)
test_list = [k+'='+v for k,v in d.items()]
print(test_list)

'''
应用：列出目录
'''
import os
print("\n---------------------------------\n列出目录:")
test_os = [dirs for dirs in os.listdir('.')]
print(test_os)
print("------------------------------------\n")
'''
遍历将字符串最小化
'''
print("\n小写化数组")
L = ['Hello', 'World', 'IBM', 'Apple']
str2 = [s.lower() for s in L]
print(str2)
'''
加入列表的if
'''
print("\n加入if的列表生成器")
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x,str)]
print(L1)
print(L2)