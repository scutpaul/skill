# -*- coding: utf-8 -*-
'''
create at 2018.01.07
@author scutpaul
'''

'''
在介绍函数参数的时候，通过设定参数的默认值，可以降低函数调用的难度。
而偏函数也可以做到这一点
'''
'''
functools.partial的作用就是，
把一个函数的某些参数给固定住（也就是设置默认值），
返回一个新的函数，调用这个新函数会更简单
'''

def int2(x, base=2):
    return int(x, base)

'''
change to partial
固定住Int的默认参数
'''
import functools
int_ = functools.partial(int, base=2)
#此处int_相同于int2
print('int2',int2('10010'))
print('int_',int_('10010'))

'''
还可以作为*args的参数传入
'''
max2 = functools.partial(max,10)
print(max2(5,6))