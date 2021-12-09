#coding=gbk
#反向不归零编码
import matplotlib.pyplot as plt
import numpy as np
N=16 #码元数
a=128#采样次数
n=a*N
x=np.linspace(0,N,n)
y=np.linspace(0,N,n)#x,y对应的采样点数目
RAN = [0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1]
p = 0
p1 = 0
for i in range(N):
    #RAN=int(round(np.random.random()))#生成0-1之间的随机浮点数,并且四舍五入
    b=i*a

    if RAN[i]==1:
        if p == 0:
            p = 1
            p1 = 0
        else:
            p = 0
            p1 = 1
        for j in range(128):
            y[b + j] = p1
        for j in range(63,a):
            y[b + j] = p
            #如果输入为1,将改码元的所有采样点赋值1
    else:
        for j in range(a):
            y[b + j] = p
            #如果输入为0,将改码元的所有采样点赋值0
plt.xlim(0,N)
plt.ylim(-1,2)                        #x,y轴的范围
plt.title("NRZI")                        #设置标题
for i in range(N):
    plt.plot(x,y,color='r',linewidth=0.5,linestyle="-")   #绘制波形
plt.show()

