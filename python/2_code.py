# -*- coding: utf-8 -*-
'''
create on 2018.01.05
@athuor: scutpaul
'''
print('ASCII是专为英文的，每个1字节')
print('各个国家根据自己具体情况做了各自的；如中国GB2312')
print('统一的是：Unicode，但是英文也是2字节，浪费空间')
print('UTF-8是变长的，在传输文件中节省字节数')

print('----所以-------')
print('内存中式Unicode统一处理，而传输时UTF-8')

print('\n\n 实践字符编码：')
print("ord('A') = ",ord('A'))
print("ord('中') = ",ord('中'))
print("chr(20013) = ",chr(20013))

print("\n\n encode")
print("将内存中的编码为以Unicode的str存储变为字节")
print("")
print("'ABC'.encode('ascii')",'ABC'.encode('ascii'))
print("'中文'.encode('utf-8')",'中文'.encode('utf-8'))
print("'中文'.encode('gb2312')",'中文'.encode('gb2312'))
print("\n decode")
print("b'ABC'.decode('ascii')",b'ABC'.decode('ascii'))
print(r"b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')",
      b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

print('\n\n 计算str字符数')
print("len('ABC')=",len('ABC'))
print("len('中文')=",len('中文'))
print("\n,计算bytes数")
print("len(b'ABC')=",len(b'ABC'))
print(r"len(b'\xe4\xb8\xad\xe6\x96\x87')=",len(b'\xe4\xb8\xad\xe6\x96\x87'))
print("len('中文'.encode('utf-8'))=",len('中文'.encode('utf-8')))

print("\n\n 填充变量：与C语言一直")
print("'Hello, %s' % 'world' = \n",'Hello, %s' % 'world')
print("多变量呢：")
print("'Hi, %s, you have $%d.' % ('Michael', 1000000) = \n",
      'Hi, %s, you have $%d.' % ('Michael', 1000000))
print("'%.2f' % 3.1415926 = \n",'%.2f' % 3.1415926)