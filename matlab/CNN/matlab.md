[matlab中的convn函数](http://blog.csdn.net/what_lei/article/details/49019049)

w=convn（u,v）;

计算矩阵u，v的卷积，w的尺寸为size（u）+size（v）-1；

w=convn（u,v,'shape'）;

返回卷积的一部分，这部分有参数shape决定：

full  返回完整的卷积（默认）；

same  返回卷积的中心部分，与u有相同的大小；

valid 仅返回卷积中的那些被计算而没有填充零的部分，w的尺寸大小为max（size（u）-size（v）+1，0）.
