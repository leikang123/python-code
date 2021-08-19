"""快速排序算法"""
import random
"""定义排序方法，a 带排序的列表，l左侧元素下表，r右侧元素下标注"""
def sort(a,l,r):
    m =partition(a,l,r)
    sort(a,l,m-1)
    sort(a,m+1,r)
def partition(a,l,r):
    i,j,v=1,r-1,a[r]
    while True:
        while a[i] <v:
            i +=1
        while a[j] >= v:
            if j == i:
                break
            j -=1
        if i >=j:
            break
        a[i],a[j]=a[j],a[i]
    a[i],a[r]=a[r],a[i]
    return i
if __name__=='_main_':
    a =[random.randint(1,100) for i in range(100)]
    print(a)
    sort(a,0,len(a) -1)
    print(a)