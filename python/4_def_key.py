# -*- coding: utf-8 -*-

def f1(a,b,c=0,*args,**kw):
    print("f1==a:",a,"b:",b,"c:",c,"args:",args,"kw:",kw)
def f2(a, b, c=0, *, d, **kw):
    print('f2==a:', a, 'b:', b, 'c:', c, 'd:', d, 'kw:', kw)

f1(1,2,3,4)
f2(1,2,3,d=4)

f1(1,2)

args = (1,2,3,4,5)
kw = {'d':'99','name':'chen','test':"54656"}
f1(*args,**kw)

args = (1,2,3)
kw = {'d':'88','name':'chen','test':"54656"}
f2(*args,**kw)