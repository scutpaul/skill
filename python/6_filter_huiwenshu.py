# -*- coding: utf-8 -*-

'''
create at 2018.01.07
@author scutpaul
'''

def is_palindrome(n):
    L = str(n)
    L2 = L[::-1]
    if L2 == L:
        return L
    else:
        return None

output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')