# -*- coding: utf-8 -*-

'''
create at 2018.01.06
@author scutpaul
'''
'''
def triangles():
    num = [1]
    while True:
        yield num
        num = [num[i] + num[i-1] for i in range(len(num))if i != 0]
        num.append(1)
        num.insert(0,1)
'''
def triangles():
    L2 = []
    while True:
        tuple_ = L2.copy()
        for i in range(1,len(tuple_)):
            L2[i] =tuple_[i]+tuple_[i-1]
        L2.append(1)
        L2[0] = 1
        yield L2[:]#改变指向！不然都是L2的对象，每次生成必须不同！！
        #print (L2)
'''
如果是temp = num，那么相当于temp和num指向了同一个对象，
这样如果num改变，temp会跟着改变，所以需要用temp = num[:]
来复制一个当前num的副本，这样num改变就不会影响到temp的值
'''
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
print (results)
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
