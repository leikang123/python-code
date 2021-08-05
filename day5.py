message = 'we come to beijing'
print(message)
message2 = ' I come form china '
print(message2+message)
name ='lei kang is china '
''' title() 表示每个单词首字母大写'''
print(name.title())
name2 = 'Eric'
print('hello'+' '+name2 + ' ' +'would you like to learn some Python today')
name_3 ='eric losry'
# 输出名字小写
print('my name‘s :'+' '+name_3.lower())
# 输出名字大写
print('my name‘s :'+' '+name_3.upper())
# 输出名字显示
print('my name‘s :'+' '+name_3.title())
# 打印名人名言
print('Albert Einisterin once said,"Aperson who nerver made a mistake nerver tried anying new",')
print('mdding once said," women is have hight is to lao ," ')
famous_person = 'mading'
message_1 = 'IS women have dakjh dg'
print(famous_person+' '+message_1)
name_4 =' leikang '
print("\t leikang")
print("\n lei kang")
print(name_4.rstrip())
print(name_4.lstrip())
print(name_4.strip())
print(6+2)
print(12-4)
print(4 * 2)
print(2 ** 3)
print(8 / 2)
print(16 / 2)
number  = 8
print(str(number)+' I like number.')
#存储一个列表名字，将其打印出来
name_5 = ['李俊','王朗','丰子恺','天寒','小看','乐乐','张东镇','李济生','严峻','黄亮亮']
print(name_5)
print(name_5[2])
message_2 = '长得帅的'+name_5[0]+'.'
print(message_2)
message_3 = 'like huanghuang is '+name_5[1]
print(message_3)
# 自己的出行但因列表，将其打印出来
travel_mode =['bucycle','bus','subway','taxi','walk']
declaration = '锻炼身体，又能环保'+travel_mode[0]
print(declaration)
declaration_2='省钱，人有多，没有污染'+travel_mode[1]
print(declaration_2)
name_6 =['xiaomi','wangxiang','liuhuan']
print(name_6)
# append():表示用来添加元素到末尾
name_6.append('lilei')
print(name_6)
print(name_6[1]+'wufa fuyue')
name_6[1]='lilei'
print(name_6)
# inser()用来表示添加元素到索引处元素，insert(2)添加元素到第2个
name_6.insert(2,'lk')
print(name_6)
name_6.insert(3,'ou')
print(name_6)
#del 表示删除元素 语法格式是 del 变量名[x];x表示索引处，要删除的元素
del name_6[0]
print(name_6)
del name_6[-1]
print(name_6)
#pop(x):表示要删除的元素，一般从尾部删除，也可以指定索引数字删除指定位置的元素
name_6.pop(1)
name_6_1 = name_6.pop(1)
print(name_6_1)
print(name_6)
# remove():根据值来删除元素，括号里表示要删除的名字
name_6.remove('lilei')
print(name_6)
#存储城市名
city = ['huanshan','xihu','tiananmen']
print(city)
# 城市名字排序，按字母字母顺序
city.sort()
print(city)
// 城市排名反序
city.sort(reverse= True)
print(city)
city.reverse()
print(city)
print(sorted(city))
#列表的存储大小，从1 开始计算列表存储的长度大小
print(len(city))
