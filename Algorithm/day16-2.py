#斐波那切数字
fab_list =[1,1]
def fab(n):
    if n < len(fab_list):
        return fab_list[n]
    else:
        fab_n=fan(n-1)+fab(n-2)
        fab_list.append(fab_n)
        return fab_n
if __name__=='_main_':
    for i in range(40,53):
        print('f({0}) ={1}',format(i,fab(i)))
