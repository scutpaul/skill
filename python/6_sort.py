# -*- coding: utf-8 -*-
'''
create at 2018.01.07
@author scutpaul
'''

'''
对列表排序
'''
print("sorted([36,8,-5,86,-6])",sorted([36,8,-5,86,-6]))

'''
sorted也是高阶函数，可以接受其他函数
'''
print("sorted([-36,8,-5,86,-6],key=abs)",sorted([-36,8,-5,86,-6],key = abs))

'''
sorted str->chr 的ascii
'''
print("sorted(['bob', 'about', 'Zoo', 'Credit'])\n",sorted(['bob', 'about', 'Zoo', 'Credit']))

'''
sorted的高阶特性
'''
print(" sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)\n",
      sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
'''
反向排序
'''
print("sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)\n",
      sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

'''
测试，姓名排序
'''
def by_name(n):
    return n[0]
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L2 = sorted(L, key=by_name)
print(L2)
#按成绩排序
def by_score(t):
    return t[1]
L3 = sorted(L,key=by_score,reverse=True)
print(L3)

