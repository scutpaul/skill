# -*- coding: utf-8 -*-
'''
create at 2018.01.06
@author scutpaul
'''
#查找最大值
def findMinAndMax(L):
#也可用if len(L):
    if L == []:
        return (None,None)
    min_ = L[0]
    max_ = L[-1]
    for i in L:
        if i > max_:
            max_ = i
        if i < min_:
            min_ = i
    return (min_,max_)
# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
