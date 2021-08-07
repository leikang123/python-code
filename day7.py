# 定义汽车品牌
car = 'subaru'
# 打印汽车品牌是否跟定义的车牌相同
print("Is car == 'subaru' ? I predit True.")
print(car == 'subaru')

print("is car == 'audi' ? I predict false.")
print(car == 'audi')
# 定义动物
zool ='tiger'
print("Is zool == 'dog'? I sure True.")
print(zool == 'tiger')

print("Is zool == 'element' I sure false.")
print(zool == 'element')
# 字符串
string = 'lkjh'
string_2 = 'dfg'
string_3 ='lkjh'
print(string == string_2)
print(string == string_3)
print(string_2 == string_3)
print(string.lower() == string_3.upper())
number = 4
number_2 = 6
print(number == number_2)
print("\n")
number_3= 4
number <3

#
names =['lilei','wanglaoshi','junjun']
name_2 = 'lilei'
print(names == name_2)
if name_2  in names :
    print(name_2.title()+' '+ "I really")
#if .. else,if ..elif.. else;
alien_color = ['green','yellow','red']
if 'li' in alien_color :
    print("获得5个点")
else:
    print("玩家获得10个点")
###
alient_color_2 = ['green','yellow','red']
if 'green' in alient_color_2:
    print("five")
elif 'yellow' in alient_color_2:
    print("ten")
else :
    print("fifteen")
#
ages = int(input("please input age"))
if ages < 2 :
    print("He is babay")
elif ages >= 2 and ages < 4 :
    print("他正在学步")
elif ages >= 4 and ages < 13 :
    print("he is child")
elif ages >=13 and ages < 20 :
    print("he is pople")
elif ages >=20 and ages < 65 :
    print("he is young")
else :
    print("die")
# fruit
favorite_fruits = ['banana','apply','grape']
if 'banana' in favorite_fruits :
    print("You really like bananans")
elif 'apply' in favorite_fruits :
    print(" You favorite_fruits")
elif 'orangle' in favorite_fruits :
    print("No ")
elif 'grape' in favorite_fruits :
    print(" You really")
else :
    print("die")
for lss in favorite_fruits :
    print("I like eat:"+' '+lss)
#
names_2 = ['admin','user','nany','wang','mn']
if names_2 :
    for a in names_2 :
        print("No")
else :
    print("Yes")
for name_2 in names_2 :
     if 'admin' in name_2 :
         print("Hello admin,would you like to see a status report?")
     else :
         print("Hello Eric,thank you ")
         
         
print("hello"+' '+name_2.title())
#定义两个用户名
c_user = ['zhangsan','liyuan','ququ','wuwu']
n_user = ['leilei','junjun','ququ','yuyu','wuwu']
// 遍历用户名
for n_user_2 in n_user :
    // 用户名是否被使用
    if n_user_2 in c_user :
        print(n_user_2.title()+' '+"己经使用")
    else :
        print(n_user_2.title()+' '+"未使用")
        
#定义一个数字，并遍历
number_2 = [1,2,3,4,5,6,7,8,9]
for number_3 in number_2 :
     if number_3 == 1 :
         print("1st")
     elif number_3 == 2 :
         print("2st")
     elif number_3 == 3 :
         print("3st")
     elif number_3 == 4 :
         print("4st")
         
print(number_3)
