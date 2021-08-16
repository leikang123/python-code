#递归算法
# n=初变量值，k=递归的次数计数器
def sus(n,k):
   print('\t' *k,'sus({0})'.format(n))
   if n==1:
        return 1
   elif n & 1 ==1:
       return sus(n* 3+1,k+1)
   else:
       return sus(n //2,k+1)
sus(9,1)
       
