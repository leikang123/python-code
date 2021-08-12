#自动计算数据
import matplotlib.pyplot as plt
x_values=list(range(1,10001))
y_values=[x*2 for x in x_values]
// 设置属性
plt.scatter(x_values,y_values,s=40,edgecolor='none',c='red')
plt.title("squers is",fontsize=10)
plt.xlabel("time",fontsize=15)
plt.ylabel("value",fontsize=15)
plt.axis([0,1000,0,110000])
// 展示图方法
plt.show()
