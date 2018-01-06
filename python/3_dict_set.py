# -*- coding: utf-8 -*-

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])
d['Adam'] = 67
print(d)
d['Adam'] = 70
print(d)
print("一个key只能有一个value")

print("查看是否有元素：'chen' in d = ","chen" in d)
print("获取位置：d.get('chen') = ",d.get('chen'),d.get('Thomas',-1))
print("删除可以用pop")
print(d)
d.pop('Bob')
print(d)

print("\n\n set")
print("set有key无value")
s = set([1, 1, 2, 2, 3, 3])
print(s)
s.add(4)
print(s)
s.remove(4)
print(s)
print("两个set可以做数学意义上的交集、并集等操作")
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1&s2)
print(s1|s2)

print("str-------")
a = ['a','c','b']
print(a)
a.sort()
print("a.sort",a)

a = 'abc'
print(a)
print("a.replace('a','A')",a.replace('a','A'))
print("a",a)
