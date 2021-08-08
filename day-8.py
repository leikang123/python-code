#字典存储信息,k-v使用{}括号，列表使用[]括号
infos = {'first':'lei','last':'kang','age':32,'city':'wuhan'}
print(infos)
print("\n")
names_infos = {'黄忠':12,'曹值':34,'刘备':8,'孙建':22,'周瑜':21,'张飞':100}
for key,value in names_infos.items() :
     print(key.title()+' '+"数据真实吗")
     print(value)
print(names_infos)
 
#words
words ={'java':'面向对象','c':'面向过程','php':'一种做好的语言','python':'数据分析的语言','julia':'一种科学计算语言'}

for word in words.keys():
    print(word)
for word_2 in words.values():
    print(word_2)
print("\n")
for word_3 in sorted(words.keys()):
    print(word_3)

for word_4 in sorted(words.values()):
    print(word_4)
#字典遍历方式：1.for key,value in 字典名.items();2.for 变量名 in 字典名.keys()/values();3.排序遍历
    #for 变量名 in sorted(字典名.keys()/values()):
    rivers = {'Amazon River':'USA','Nile river':'egypt','Panama Canal':'camca'}
for key,value in rivers.items():
    print(key.title()+"The Nile runs througs Egpet")
    print(value.title())
for river in rivers.keys():
    print(river)
for river_2 in rivers.values():
    print(river_2)
#
print("\n")
user = {'jen':'python','sarch':'c','edware':'ruby','phil':'python'}
user_2 = ['jen','phil','alice','rode']
for user_3 in user.keys():
    print(user_3)

    if user_3 in user_2:
        print(user_3.title()+' '+"thank!")

    else :
        print("canyu")
print("\n")
#
people ={'shan':2,'jkl':3,'yu':8}
people_2 ={'sure':'ghj','kill':'oiu'}
people_3 = {'wuhan':32,'beijing':'first','nanjing':90}
#列表里的字典不能是字符串，否则信息丢失。
pes = [people,people_2,people_3]
for p in pes :
    print(p)
print("\n")
#创建三个字典，然后创建一个列表，判断是否有里面的人
dogs = {'name':'wawa','age':2,'women':'qq'}
cats = {'name':'huhu','age':7,'women':'rr'}
tiger = {'name':'huanangu','age':12,'women':'wu'}
pets =[dogs,cats,tiger]
for pets_2 in pets :
    print(pets_2)
print("\n")
#遍历多个k-v，v里面也有多个k-v,
cities ={'wuhan':{'country':'china','population':'1000milon','fact':'hero'},'new york':{'country':'USA','population':'1000milon',
 
                                                                                        'fact':'ziyou'},'Tony':{'country':'Janpa','population':'1000milon','fact':'lishi'}}
# 遍历k-v字典
for c,p in cities.items():
    print("City:"+c)
    guojia = p['country']
    pop = p['population']
    f = p['fact']
    print("guojia:"+guojia.title())
    print("pop:"+pop.title())
    print("f:"+f.title())
