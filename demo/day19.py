import threading
# 创建一个线程对象带参数，次处是继承参数里的类
class MyThread(threading.Thread):
    # 继承重写方法
     def __init__(self,num):
         threading.Thread.__init__(self)
         self.num = num
     def run(self):
         print('\nIm {0}'.format(self.num))
# 创建线程对象
t1 = MyThread(1)
t2 = MyThread(2)
t3 = MyThread(3)
# 启动线程
t1.start()
t2.start()
t3.start()