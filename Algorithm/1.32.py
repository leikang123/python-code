from c4 import fab;
'''定义一个方法，表示怎么计算斐波纳函数'''

def fab_sum(n):
    return fab(n+2) -2
'''方法主方法的输出'''

if __name__=='__main__':
     print('S(12) =',fab_sum(12))
