# -*- coding: utf-8 -*-
'''
create at 2018.01.07
@author scutpaul
'''

class Animal(object):
    def run(self):
        print('Animal is running....')
        
'''
Dog->Animal,继承
run方法重写，多态
'''
class Dog(Animal):
    def run(self):
        print('Dog is running....')#重载
    def eat(self):
        print('Dog is eating..')#增加方法

if __name__=='__main__':
    puppy = Dog()
    print('isDog',isinstance(puppy,Dog))
    print('isAnimal',isinstance(puppy,Animal))
'''
isinstance也可以判断是否是父类继承而来的
同时也是父类也会是True
'''

'''
多态的进一步理解：函数
新增一个Animal的子类，不必对run_twice()做任何修改，
实际上，任何依赖Animal作为参数的函数或者方法都可以不加修改地正常运行，原因就在于多态
'''
def run_twice(animal):
    animal.run()
    animal.run()
    
if __name__ == '__main__':
    puppy = Dog()
    chen = Animal()
    run_twice(puppy)
    run_twice(chen)
    print(dir(puppy))
    
'''
对扩展开，对修改闭：（软件工程：面向对象编程的原则之一）
对于一个变量，我们只需要知道它是Animal类型，无需确切地知道它的子类型，
就可以放心地调用run()方法，而具体调用的run()方法是作用在Animal、Dog、Cat还是Tortoise对象上，
由运行时该对象的确切类型决定，
这就是多态真正的威力：调用方只管调用，不管细节，
而当我们新增一种Animal的子类时，只要确保run()方法编写正确，不用管原来的代码是如何调用的。

对扩展开放：允许新增Animal子类；

对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。
'''

'''
对于静态语言（例如Java）来说，如果需要传入Animal类型，
则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。

对于Python这样的动态语言来说，则不一定需要传入Animal类型。
我们只需要保证传入的对象有一个run()方法就可以了：
'''
class Timer(object):
    def run(self):
        print('Start...')
#也可以使用run_twice