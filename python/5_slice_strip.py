# -*- coding: utf-8 -*-
#去空格
'''
create at 2018.01.06
@author scutpaul
'''

def trim(s):
    if s == '':
        return s
    while(s[0]==' '):
        s = s[1:]
        if s == '':
            return s
    while(s[-1]==' '):
        s = s[:-1]
    return s

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')