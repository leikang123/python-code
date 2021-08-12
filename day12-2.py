#函数存储在模块中
def make_pizza(size,*topping):
    print("\n makeing:"+' '+str(size))
    for p in topping:
        print(p)
