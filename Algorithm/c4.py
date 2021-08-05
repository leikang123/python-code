def fab(n):
    return 1 if  n < 2 else fab( n-1) + fab(n-2)
if __name__=='__main__':
       for i in range(int(input("输入数字"))) :
        print('f({0}) ={1}'.format(1,fab(i)))