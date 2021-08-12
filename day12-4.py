#绘制折线图
import matplotlib.pyplot as plt
squares = [1,4,9,16,25,30,50,80]
#打开图形方法
plt.plot(squares,linewidth=5)
plt.title("sqiers",fontsize=24)
plt.xlabel("value",fontsize=10)
plt.ylabel("value is ",fontsize=10)
plt.tick_params(axis="both",labelsize=14)
plt.show()
