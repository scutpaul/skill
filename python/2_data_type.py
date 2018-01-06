# -*- coding: utf-8 -*-

#转义的测试

print("Sen1:这个可以显示'的,不用转义")
print('Sen2:这个需要转移,如\'\"')
print(r'Sen3:在前面加上r就可以转义没用了\\\t\\\想打就打')
print('''Sen4:前面\'\'\'可以多行！\n \\n也用
...test1
...test2''')

print('\n\n bool:')
print(not True)
print(True)
print(1>2)


print('\n\n 变量的实质')
a = 123
b = a
a = 'ABC'
print('a = 123')
print('b = a')
print('a = \'ABC\'')
print('now a = ',a)
print('now b = ',b)

print('\n\npython的常量是用大写的（假常量）')
PI = 3.14
print('PI = ',PI)
PI = 6.28
print('改变之后PI = ',PI)

print('\n\n +-*/')
print('10%3=',10%3)
print('10//3=',10//3)
print('10/3=',10/3)
print('9/3=',9/3)

print('\n\n 总结')
n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''
print('n=',n)
print('f=',f)
print('s1=',s1)
print('s2=',s2)
print('s3=',s3)
print('s4=',s4)