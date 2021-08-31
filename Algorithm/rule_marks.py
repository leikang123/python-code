import matplotlib.pyplot as plt
import matplotlib.patches as mpathes

marks = [];
def ruler(l,r,h):
    m =(1+r) // 2
    if h > 0:
        ruler(l,m,h-1)
        mark(m,h)
        ruler(m,r,h-1)
def mark(m,h):
    marks.append((m,h))

def show():
    fig,ax = plt.Subplots()
    rect =mpathes.Rectangle([0,0],8,1,fill =False)
    ax.add_patch(rect)
    for m,h in marks :
        plt.vlines(x=m,ymin=0,ymax=h *0.2,colors='b')
    plt.axis('equal')
    plt.axis('off')
    plt.show()
if __name__=='_main_':
    ruler(0,8,3)
    print(marks)
    for _,h in marks :
     print('_' * h)
     show()
