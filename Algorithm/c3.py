def is_price(a):
    if a < 2 :
        return False, []
    elif a ==2 :
        return True,[]
    divmod = [ x for x in range(2,a)if a % x ==0]
    return len(divmod) == 0 ,divmod
