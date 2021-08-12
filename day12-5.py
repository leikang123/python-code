#绘制散点图
import matplotlib.pyplot as plt
x_values=[1,3,5,7,9,11,13,15]
y_values=[1,4,7,9,12,14,16,19]
plt.scatter(x_values,y_values,s=100)
plt.scatter(2,4,s=200)
plt.title("my is squers",fontsize=15)
plt.xlabel("time",fontsize=15)
plt.ylabel("value",fontsize=15)
#设置刻度标记大小
plt.tick_params(axis='both',which='major',labelsize=14)
plt.show()
