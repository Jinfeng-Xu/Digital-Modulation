#coding=gbk
#���򲻹������
import matplotlib.pyplot as plt
import numpy as np
N=16 #��Ԫ��
a=128#��������
n=a*N
x=np.linspace(0,N,n)
y=np.linspace(0,N,n)#x,y��Ӧ�Ĳ�������Ŀ
RAN = [0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1]
p = 0
p1 = 0
for i in range(N):
    #RAN=int(round(np.random.random()))#����0-1֮������������,������������
    b=i*a
    if RAN[i]==1:
        for j in range(128):
            y[b + j] = 0
        for j in range(63,a):
            y[b + j] = 1
            #�������Ϊ1,������Ԫ�����в����㸳ֵ1
    else:
        for j in range(128):
            y[b + j] = 1
        for j in range(63, a):
            y[b + j] = 0
            #�������Ϊ0,������Ԫ�����в����㸳ֵ0
plt.xlim(0,N)
plt.ylim(-1,2)                        #x,y��ķ�Χ
plt.title("ME")                        #���ñ���
for i in range(N):
    plt.plot(x,y,color='r',linewidth=0.5,linestyle="-")   #���Ʋ���
plt.show()

