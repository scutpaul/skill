理解图：
![](https://scutpaul-1252936646.cos.ap-guangzhou.myqcloud.com/skill/matlab/CNN/img/conv.jpg)
这个的层：
* 输入层：28\*28
* 一层卷积：卷积核5\*5，输出：6个，卷积核数量：1\*6
* 一次下采样：大小：2 即窗口[24,24]变[12,12]，其他不变
* 二层卷积：卷积核5\*5，输出：6个，卷积核数量：6\*12
* 二次下采样：大小：2
* 输出层：展开二次下采样的所有核

原始窗口大小：
```
inputmaps = 1;
%输入窗口的大小[28,28],squeeze是压缩掉[28,28,1]的一维
mapsize = size(squeeze(x(:, :, 1)));
```

卷积层：
```
if strcmp(net.layers{l}.type, 'c')% 卷积层
    % feature map大小 = 上层-卷积核大小+1
    mapsize = mapsize - net.layers{l}.kernelsize + 1;
    % 输出的所有链接：卷积核数*卷积核大小 一层：6*25 二层:12*25
    fan_out = net.layers{l}.outputmaps * net.layers{l}.kernelsize ^ 2;
    for j = 1 : net.layers{l}.outputmaps  %  output map
        % 卷积核数 = 输入*输出
        % fan_in：本层一个输出map对应的所有卷积核，包含的权值的总数 = 1*25,6*25
        fan_in = inputmaps * net.layers{l}.kernelsize ^ 2;
        for i = 1 : inputmaps  %  input map
            %卷积核的初始化生成一个5*5的卷积核，值为-1~1之间的随机数
            %再乘以sqrt(6/(7*25))，sqrt(6/(18*25))
            net.layers{l}.k{i}{j} = (rand(net.layers{l}.kernelsize) - 0.5) * 2 * sqrt(6 / (fan_in + fan_out));
        end
        % 偏置置为0，每个输出map有一个bias.输出map为各卷积核的结果加上bias
        net.layers{l}.b{j} = 0;
    end
    inputmaps = net.layers{l}.outputmaps;
end
```
降采样层
```
if strcmp(net.layers{l}.type, 's')% 采样层
    mapsize = mapsize / net.layers{l}.scale;%降采样的feature，[28:28]->[14:14]的scale==2
    assert(all(floor(mapsize)==mapsize), ['Layer ' num2str(l) ' size must be integer. Actual: ' num2str(mapsize)]);
    for j = 1 : inputmaps % 设置降采样的输出map，bias
        net.layers{l}.b{j} = 0;
    end
end
```

尾部感知机的设置：
```
% fvnum 最后一层展开输出的长度
fvnum = prod(mapsize) * inputmaps;
% 分类类别
onum = size(y, 1);

net.ffb = zeros(onum, 1);
net.ffW = (rand(onum, fvnum) - 0.5) * 2 * sqrt(6 / (onum + fvnum));
```
