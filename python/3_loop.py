# -*- coding: utf-8 -*-

sum = 0
for x in [1,2,3]:
    sum = sum + x
print(sum)

sum =0
for x in range(101):
    sum = sum + x
print(sum)

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

#也可以用break、continue