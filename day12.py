def greet(names):
    for name in names :
      mag ="hello"+name.title()
      print(mag)
user = ['llle','hg','kl']
greet(user)
#
print("\n")
def show_magicians(names2):
    for name2 in names2 :
        mag2 = "hello"+' '+name2.title()
        print(mag2)

mag_name = ['leilei','wangkai','ghf']
show_magicians(mag_name)
#
print("\n")
def make_pizza(*topping):
    print(topping)
make_pizza('pop')
make_pizza('mus','hjk','extra')
print("\n")
def make_pizza2(size,*toppings):
    print("\nmakeing a:"+' '+str(size)+"pizza is topping")

    for top in toppings :
        print(top)
#实力化
make_pizza2(19,"oiuy")
make_pizza(13,"music","lkjh","mkjh")
    
