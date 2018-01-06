# -*- coding: utf-8 -*-

classmates = ['Michael', 'Bob', 'Tracy']
print("classmates:",classmates)
print(len(classmates))
print("classmates[0]",classmates[0])
print("下面就是神奇的例子：逆向索引")
print("classmates[-1]",classmates[-1])
print("尾部增加：classmates.append('Adam')")
classmates.append('Adam')
print("classmates:",classmates)
print("中间插入：classmates.insert(1, 'Jack')")
classmates.insert(1, 'Jack')
print("classmates:",classmates)
print("尾部删除：classmates.pop()")
classmates.pop()
print("classmates:",classmates)
print("中间插入:classmates.pop(1)")
classmates.pop(1)
print("classmates:",classmates)

混合 = ['混合',123,True]
print("混合list:",混合)

嵌套list = ['外层',["内层1","内层2",123],234]
print("嵌套list",嵌套list)
print("嵌套list[0]",嵌套list[0])
print("嵌套list[1][0]",嵌套list[1][0])