# -*- coding: utf-8 -*-
'''
create at 2018.01.07
@author scutpaul
'''
import time, functools
def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args,**kw):
        start = time.clock()
        print("start",start)
        k = fn(*args,**kw)#原函数在中间运行！！！！
        elapsed = (time.clock() - start)
        print('%s executed in %s s' % (fn.__name__, elapsed))
        return k#放回原函数运行结果！！！
    return wrapper


@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')

