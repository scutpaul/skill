# -*- coding: utf-8 -*-

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module ' #注释

__author__ = 'scutpaul' #作者

import sys #导入模块

def test():
    args = sys.argv #模块内的参数
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')


'''
#只有在命令行执行时__name__才为__main__所以用于测试
'''
if __name__=='__main__':  
    test()
    
'''
作用域：
private用'_abc'此类表示
编程习惯要避免出现引用'_abc'此类，但python并不会阻止你。
'''