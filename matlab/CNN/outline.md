# CNN by Matlab
> [github](https://github.com/rasmusbergpalm/DeepLearnToolbox)

>[csdn](http://blog.csdn.net/u013007900/article/details/51428186)

## CNN结构

调用关系：
![call](https://scutpaul-1252936646.cos.ap-guangzhou.myqcloud.com/skill/matlab/CNN/img/callRelation.jpg)
网络架构：
![cnnNet](https://scutpaul-1252936646.cos.ap-guangzhou.myqcloud.com/skill/matlab/CNN/img/cnnNet.jpg)

## 数据集介绍

mnist的数字mnist_uint8.mat

样本：28*28的向量
训练集：60000
测试集：10000

## test_example_CNN
* 设置CNN的参数：卷积、下采样的数量、卷积核的大小、下采样的幅度
* cnnsetup函数初始化卷积核、偏置
* cnntrain函数训练cnn、分为batch，再调用
    * cnff完成训练的前向
    * cnbp完成误差的后向传播
    * cnnapplygrads改模型
* cnntest函数，测试当前的模型准确度

<br/>
代码解读：

转换格式
```
train_x = double(reshape(train_x',28,28,60000))/255;
test_x = double(reshape(test_x',28,28,10000))/255;
train_y = double(train_y');
test_y = double(test_y');
```
 设置网络结构
 ```
rand('state',0)
cnn.layers = {
    struct('type', 'i') %input layer
    struct('type', 'c', 'outputmaps', 6, 'kernelsize', 5) %convolution layer
    struct('type', 's', 'scale', 2) %sub sampling layer
    struct('type', 'c', 'outputmaps', 12, 'kernelsize', 5) %convolution layer
    struct('type', 's', 'scale', 2) %subsampling layer
};
 ```
设置训练batch
```
opts.alpha = 1;
opts.batchsize = 50;
opts.numepochs = 1;
```
初始化网络与训练
```
cnn = cnnsetup(cnn, train_x, train_y);
cnn = cnntrain(cnn, train_x, train_y, opts);
```
测试
```
[er, bad] = cnntest(cnn, test_x, test_y);
```
输出
```
figure; plot(cnn.rL);
```

[cnnsetup](cnnsetup.md)
[cnntrain](cnntrain.md)
