#练习题
import matplotlib.pyplot as l
x_values =list(range(1,10)
y_values = [x**3 for  x in x_values]
l.scatter(x_values,y_values,s=40)
squers=[1,8,9,64,125,216]
"""线条加粗"""
l.plot(squers,linewidth=5)
"""图标显示横坐标和纵坐标"""
l.title("my is num",fontsize=13)
l.xlabel("time",fontsize=13)
l.ylabel("value",fontsize=13)
l.plot(squers)
l.axis([0,10,0,100000])
l.show()
