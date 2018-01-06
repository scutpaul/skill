# -*- coding: utf-8 -*-
'''
create at 2018.01.06
@author scutpaul
'''

#生成器
'''
在Python中，这种一边循环一边计算的机制，称为生成器：generator
减少内存占用！
'''

g = (x * x for x in range(10))
print("可以发现g是一个生成器入口",g)
#打印生成器
print("打印生成器: next")
for i in range(3):
    print(next(g))
print("generator保存的是算法，每次调用next(g)，",
      "就计算出g的下一个元素的值，直到计算到最后一个元素")
print("直接for 循环也行的")
for i in g:
    print(i)
print("计算过就没了！")

'''
遇到yeild则返回
'''
print('yield!!!')
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)
o = odd()
next(o)
next(o)
next(o)