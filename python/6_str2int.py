# -*- coding: utf-8 -*-
'''
create at 2018.01.07
@author scutpaul
'''
from functools import reduce

digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def trans_to_dec(x,y):
    return x*10+y

def char2num(x):
    return digits[x]

test = reduce(trans_to_dec,map(char2num,'12345'))
print(test)


def str2int(str1):
    def trans_to_dec(x,y):
        return x*10+y
    def char2num(x):
        return digits[x]
    return reduce(trans_to_dec,map(char2num,str1))


print(str2int('123456'))

'''
lambda的加入
'''

def str2int2(str2):
    return reduce(lambda x,y:x*10+y,map(lambda x:digits[x],str2))
print(str2int2('568'))

'''
def normalize(name):
'''
'''
def normalize(name):
    for x in range(len(name)):
        if x == 0:
            name[x]=name[x].upper()
        else:
            name[x]=name[x].lower()
    return name
'str' object does not support item assignment
出错：str为常量
'''
# 测试:
def normalize(name):
    return name[0].upper()+name[1:].lower()
def normalize_(name):
    return name.title()
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
'''
乘积
'''
def prod(L):
    return reduce(lambda x,y:x*y, L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')
    
'''
str2float
'''
def str2float(s):
    #将字符串由.分成两部分
    s = s.split('.')
    snew = s[1]
    #小数部分字符串颠倒
    s[1] = snew[::-1]
    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    def fint(s):
        return DIGITS[s]
    #整数部分
    def f1(x,y):
        return x * 10 + y
    #小数部分
    def f2(x,y):
        return x *0.1 +y
    t = reduce(f2,map(fint,s[1]))
    return reduce(f1,map(fint,s[0])) + t * 0.1

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
