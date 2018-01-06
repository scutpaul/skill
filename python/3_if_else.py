# -*- coding: utf-8 -*-

age_str = input("请输入你的年龄")
age = eval(age_str) #str->int
str1 = "你已经成年"
str2 = "未成年不可查看"
str3 = "你太老了"
if age >70:
    print(str3)
elif age > 18:
    print(str1)
else:
    print(str2)