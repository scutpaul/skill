# 该函数用于训练CNN。
生成随机序列，每次选取一个batch（50）个样本进行训练。
批训练：计算50个随机样本的梯度，求和之后一次性更新到模型权重中。
在批训练过程中调用：
Cnnff.m 完成前向过程
Cnnbp.m 完成误差传导和梯度计算过程
Cnnapplygrads.m 把计算出来的梯度加到原始模型上去

```
%net为网络,x是数据，y为训练目标，opts (options)为训练参數
function net = cnntrain(net, x, y, opts)
```

```
net.layers{1}.a{i}是第i层的数据
```
分批：
```
m = size(x, 3);
%一批的数量
numbatches = m / opts.batchsize;
if rem(numbatches, 1) ~= 0
    error('numbatches not integer');
end
%rL是最小均方误差的平滑序列，绘图要用
net.rL = [];
% 迭代次数
for i = 1 : opts.numepochs
    %显示当前是第几个迭代
    disp(['epoch ' num2str(i) '/' num2str(opts.numepochs)]);
    tic;
    %随机序列1~m的无重复排序，用于打乱训练次序
    kk = randperm(m);
    %分批
    for l = 1 : numbatches
        %取样：一个batchsize的大小（乱序）
        batch_x = x(:, :, kk((l - 1) * opts.batchsize + 1 : l * opts.batchsize));
        batch_y = y(:,    kk((l - 1) * opts.batchsize + 1 : l * opts.batchsize));

        net = cnnff(net, batch_x);% 前向
        net = cnnbp(net, batch_y);% 误差后向
        net = cnnapplygrads(net, opts);% 调整模型
        %net.L为模型的costFunction,即最小均方误差mse
        %net.rL是最小均方误差的平滑序列
        if isempty(net.rL)
            net.rL(1) = net.L;
        end
        net.rL(end + 1) = 0.99 * net.rL(end) + 0.01 * net.L;
    end
    toc;
end
```

# cnnff.m
输入：网络架构+训练数据
```
function net = cnnff(net, x)
```
初始化：
```
%网络层数
n = numel(net.layers);
%输入层
net.layers{1}.a{1} = x;
inputmaps = 1;
```

对于卷积层：
```
if strcmp(net.layers{l}.type, 'c')
    %  !!below can probably be handled by insane matrix operations
    for j = 1 : net.layers{l}.outputmaps   %  for each output map
        % z = zeros([28,28,50]-[4,4,0]) = zeros([24,24,50]) 输出层的创建
        z = zeros(size(net.layers{l - 1}.a{1}) - [net.layers{l}.kernelsize - 1 net.layers{l}.kernelsize - 1 0]);
        for i = 1 : inputmaps   %  for each input map
        %  convolve with corresponding kernel and add to temp output map
            z = z + convn(net.layers{l - 1}.a{i}, net.layers{l}.k{i}{j}, 'valid');
        end
        %  加入偏置，做sigmo
        net.layers{l}.a{j} = sigm(z + net.layers{l}.b{j});
    end
%  这层输出做下层输入
inputmaps = net.layers{l}.outputmaps;
```
对于降采样层：
```
elseif strcmp(net.layers{l}.type, 's')
    %  downsample
    for j = 1 : inputmaps
        %卷积一个[0.25,0.25;0.25,0.25]的降采样层
        z = convn(net.layers{l - 1}.a{j}, ones(net.layers{l}.scale) / (net.layers{l}.scale ^ 2), 'valid');   %  !! replace with variable
        %跳着取(计算浪费)
        net.layers{l}.a{j} = z(1 : net.layers{l}.scale : end, 1 : net.layers{l}.scale : end, :);
    end
end
```
尾部单层感知机
```
%  concatenate all end layer feature maps into vector
net.fv = [];
%拼成列向量
for j = 1 : numel(net.layers{n}.a)
    %size of/ sa = [4, 4, 50];得到Sfm2的一个输入图的大小
    sa = size(net.layers{n}.a{j});
    %reshape(A,m,n);
    %把矩阵A改变形状，编程m行n列。（元素个数不变，原矩阵按列排成一队，再按行排成若干队）
    %把所有的Sfm2拼合成为一个列向量fv，[net.fv; reshape(net.layers{numLayers}.a{j}, 4*4, 50)];
    %最后的fv是一个[16*12*50]的矩阵
    net.fv = [net.fv; reshape(net.layers{n}.a{j}, sa(1) * sa(2), sa(3))];
end
%  feedforward into output perceptrons
%net.ffW是[10,192]的权重矩阵
%net.ffW * net.fv是一个[10,50]的矩阵
%repmat(net.ffb, 1, size(net.fv, 2)把 bias复制成50份排开
net.o = sigm(net.ffW * net.fv + repmat(net.ffb, 1, size(net.fv, 2)));
```

# cnnbp.m
* 该函数实现2部分功能，计算并传递误差，计算梯度

输入 网络数据与标签
```
function net = cnnbp(net, y)
```
计算误差：最小二乘
```
% error
net.e = net.o - y;
%loss function
net.L = 1/2* sum(net.e(:) .^ 2) / size(net.e, 2);
```
计算尾部单层感知机的误差
```
net.od = net.e .* (net.o .*(1 - net.o)); %output dalta, sigmoid 误差
%fvd, feature vector delta, 特征向里误差,上一层收集下层误差,size = [192*50]
net.fvd = (net.ffW' * net.od);
%如果MLP的前一层（特征抽取最后一层）是卷积层，卷积层的输出经过sigmoid函数处理，error求导
%在数字识别这个网络中不要用到
if strcmp(net.layers{n}.type, 'c')
    %对于卷基层，它的特征向里误差再求导(net.fv .* (1-net.fv))
    net.fvd = net.fvd .*(net.fv .* (1 - net.fv));
end
```
