#定义一个集合列表
names = ['雷昂','张三','杨类','杨叶子','吹风子','王老师']
# 遍历列表的元素
for name in names :
    #打印列表元素
    print(name)
// 定义一个比萨列表
pizzas = ['applypizza','bananapizza','Shortbreadpizza']
// 遍历比萨列表
for pizza in pizzas :
    print(pizza)
    print("I like peppersion pizza"+' '+pizza.title())
        
print("I really love pizza")

#定义动物集合列表
zools = ['monkey','gorilla','Macaque','tiger']
// 遍历列表
for zool in zools :
    print(zool.title() +' '+"A dog would  make  a great pet")
print("Any  of these animals would make a great pet!")
    
#for 循环打印
for number in range(1,21):
    print(number)
#for 打印1000000
#for number_2 in range(1,1000001):
 #   print(number_2)
#1-100000的和
numbers_3 = list(range(1,1000001))
print(min(numbers_3))
print(max(numbers_3))
print(sum(numbers_3))
numbers_4=list(range(1,21,2))
print(numbers_4)
number_5 = list(range(3,31,3))
print(number_5)
number_6 = [value **3 for value in range(1,10)]
print(number_6)
#切片
message = ['The','first','three','items','in','the','list','are']
me = message[0:3]
print(me)
print(message[3:6])
print(message[-3:])
friend_pizza = pizzas;
print(friend_pizza)
friend_pizza.append('beef_pizza')
print(friend_pizza)
#for friends_pizza in friend_pizza :
#print(friends_pizza)
# 元组
foods = ['beef','childen','salad','ice','coffer']
for food in foods :
 print(food)
foods[0] = 'lobster'
print(foods)
foods_1 = ['beef','lobster','salad','ice','jelly']
print(foods_1)
for food_1 in foods_1 :
    print(food_1)
