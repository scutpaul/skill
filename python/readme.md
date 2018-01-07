# python学习
>学习内容[廖雪峰的官方网站](https://www.liaoxuefeng.com/)

## 初次见面
* 基本的输入：input() [1_do_input](https://github.com/scutpaul/skill/blob/master/python/1_do_input.py)


## 基本的数据类型
* 编码：ASCII UTF-8 Unicode [2_code](https://github.com/scutpaul/skill/blob/master/python/2_code.py)
* 变量：转义 [2_data_type](https://github.com/scutpaul/skill/blob/master/python/2_data_type.py)
* List类型 可变长的 [2_list](https://github.com/scutpaul/skill/blob/master/python/2_list.py)
* Tuple类型 常量
[2_tuple](https://github.com/scutpaul/skill/blob/master/python/2_tuple.py)

## 比较高级的数据结构
* dict字典，set集合 [3_dict_set](https://github.com/scutpaul/skill/blob/master/python/3_dict_set.py)


## 函数控制结构
* if_else [3_if_else](https://github.com/scutpaul/skill/blob/master/python/3_if_else.py)
* loop [3_loop](https://github.com/scutpaul/skill/blob/master/python/3_loop.py)
* for: for x in rang(1,11)
[5_for_in](https://github.com/scutpaul/skill/blob/master/python/5_for_in.py)
[5_generator](https://github.com/scutpaul/skill/blob/master/python/5_generator.py)
、取最大最小[5_find_min_max](https://github.com/scutpaul/skill/blob/master/python/5_find_min_max.py)


## 函数
* 使用系统函数 max abs [4_use_function](https://github.com/scutpaul/skill/blob/master/python/4_use_function.py)
* 定义 def 可变参数 默认参数 关键词参数  [4_def_function](https://github.com/scutpaul/skill/blob/master/python/4_def_function.py)
[4_def_key](https://github.com/scutpaul/skill/blob/master/python/4_def_key.py)
* 递归的设计 汉诺塔
[4_digui](https://github.com/scutpaul/skill/blob/master/python/4_digui.py.py)
[4_hanoi_tower](https://github.com/scutpaul/skill/blob/master/python/4_hanoi_tower.py)

## 高级特性
* 切片 取第i到n的数，可倒序取、间隔取[5_slice_cut_list](https://github.com/scutpaul/skill/blob/master/python/5_slice_cut_list.py) 、去空格[5_slice_strip](https://github.com/scutpaul/skill/blob/master/python/5_slice_strip.py)
* 迭代 判断是否可迭代 enumerate把一个list变成索引-元素对 [5_for_in](https://github.com/scutpaul/skill/blob/master/python/5_for_in.py)
* 列表生成 使用列表生成式生成复杂的列表 有if for [5_list_generator](https://github.com/scutpaul/skill/blob/master/python/5_list_generator.py)
* 生成 列表生成器限制，故使用yield 每次遇到yield就停
[5_generator](https://github.com/scutpaul/skill/blob/master/python/5_generator.py)斐波那契数列 [5_generator_Fibonacci](https://github.com/scutpaul/skill/blob/master/python/5_generator_Fibonacci.py)
杨辉三角[5_generator_Pascal_Triangle](https://github.com/scutpaul/skill/blob/master/python/5_generator_Pascal_Triangle.py)
* 迭代 可迭代（可for）与迭代器（不存储） [5_iterable](https://github.com/scutpaul/skill/blob/master/python/5_iterable.py)

## 函数式编程

* 高阶函数： 支持传入参数为函数[6_higher_other](https://github.com/scutpaul/skill/blob/master/python/6_higher_other.py)
* MapReduce map作用于每个元素相同,reduce迭代作用 [lambda] [6_map_reduce](https://github.com/scutpaul/skill/blob/master/python/6_map_reduce.py) str2int、str2float[6_str2int](https://github.com/scutpaul/skill/blob/master/python/6_str2int.py)
* Filter:决定是否要过滤 筛选函数作用于每一个元素 [6_filter](https://github.com/scutpaul/skill/blob/master/python/6_filter.py) 生成素数 [6_filter_prime](https://github.com/scutpaul/skill/blob/master/python/6_filter_prime.py) 生成回文字 [6_filter_huiwenshu](https://github.com/scutpaul/skill/blob/master/python/6_filter_huiwenshu.py)
* Sort 排序sorted()可支持列表、与key函数等函数传入 [6_sort](https://github.com/scutpaul/skill/blob/master/python/6_sort.py)
* 返回函数 程序的闭包变量[循环变量会保存] [7_return_func](https://github.com/scutpaul/skill/blob/master/python/7_return_func.py)
* Lambda 匿名函数：python中函数可以作为参数传输、只能有一个表达式 [7_lambda](https://github.com/scutpaul/skill/blob/master/python/7_lambda.py)
* Decorator 装饰器：使用@log(可带参数):实现：now = log('execute')(now) 作为装饰器[7_decorator](https://github.com/scutpaul/skill/blob/master/python/7_decorator.py)打印程序运行时间[7_decorator_time](https://github.com/scutpaul/skill/blob/master/python/7_decorator_time.py)
* partical function: 偏函数[固定住函数的默认函数] [7_partial_function](https://github.com/scutpaul/skill/blob/master/python/7_partial_function.py)

## 模块
* 模块的介绍 [廖雪峰的网站](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014318447437605e90206e261744c08630a836851f5183000)
* 使用模块 __name__ 的使用 [hello](https://github.com/scutpaul/skill/blob/master/python/hello.py)

## 面向对象编程
* 类与示例 实例参数self、继承类object 、动态添加实例的属性 [8_class_instance](https://github.com/scutpaul/skill/blob/master/python/8_class_instance.py)
* 访问限制 保护 私有变量使用下划线 但是python并不是保护起来只是把外部名字改了。[8_class_protected](https://github.com/scutpaul/skill/blob/master/python/8_class_protected.py)
* 继承与多态 多态的开闭原则：包含文字解释[8_class_dog_cat](https://github.com/scutpaul/skill/blob/master/python/8_class_dog_cat.py)
* 获取对象的信息 type()获取类别、types模块类别、isinstance()父子类别、dir类的所有属性与方法、attr的操作：（get、has、set）[8_class_gettype](https://github.com/scutpaul/skill/blob/master/python/8_class_gettype.py)
* 类属性与实例属性 [8_class_attr](https://github.com/scutpaul/skill/blob/master/python/8_class_attr.py)
