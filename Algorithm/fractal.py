import matplotlib.pyplot as plt
import numpy as np

"""定义分形的属性方法，fai=向量的初始角度，theta=向量每次逆时针旋转的角度，depth=树的高度
==0的时候停止分形，ax=subplots;调用的库的方法"""
def draw(fai,theta,depth,ax):
    """x1=上一个枝干的终点，y1=上一个枝干的终点，fai=前枝干逆时针旋转的角度，depth=树的深度"""
    def draw_line(x1,y1,fai,depth):
        #如果树的深度==0，就停止，返回
        if depth ==0:

          return
        #转换公式，角度转换孤度
        radian = np.radians(fai)
        # x2 =
        x2 =x1+np.cos(radian) * depth
        y2 = y1+np.sin(radian) * depth
        #画出枝干
        ax.plot([x1,x2],[y1,y2],color ='red')
        #继续分行
        draw_line(x2,y2,fai+theta,depth -1)
        draw_line(x2,y2,fai - theta,depth -1)
    draw_line(0,0,fai,depth)
#绘制图形树
_,ax = plt.subplots()
plt.axis('off')
plt.axis('equal')
draw(90,30,8,ax)
plt.show()
#继续分型
fig = plt.figure()
for i in range(1, 10):
    ax = fig.add_subplot(3, 3, i)
    plt.axis('off')
    plt.axis('equal')
    plt.title('depth=' + str(i))
    draw(90, 30, i, ax)
plt.show()
