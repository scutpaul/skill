# -*- coding: utf-8 -*-
'''
初级hanoi
'''
def hanoi(n,a,b,c):
    if(n==1):
        print(a ,'--->',c)
    else:
        hanoi(n-1,a,c,b)
        hanoi(1,a,b,c)
        hanoi(n-1,b,a,c)
#hanoi(6,"A","B","C")

'''
加入类
'''
class Tower(object):
    
    def __init__(self):
        self.counter = 0
    
    def hanoi(self,n,a,b,c):
        if(n==1):
            print(a ,'--->',c)
            self.counter += 1
            #print(self.counter)
        else:
            self.hanoi(n-1,a,c,b)
            self.hanoi(1,a,b,c)
            self.hanoi(n-1,b,a,c)
            
def check_hanoi(*argc):
    tower = Tower()
    tower.hanoi(*argc)
    print('移动次数{0}'.format(tower.counter))
    
check_hanoi(3,"A","B","C")

'''
使用全局变量
'''
couter=0
def hanoi_couter(n,a,b,c):
    global couter
    if(n==1):
        print(a ,'--->',c)
        couter = couter+ 1
    else:
        hanoi_couter(n-1,a,c,b)
        hanoi_couter(1,a,b,c)
        hanoi_couter(n-1,b,a,c)
hanoi_couter(3,"A","B","C")
print("移动次数{}".format(couter))