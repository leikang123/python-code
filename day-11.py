def greet_user():
    print("leikang")  
greet_user()
print("\n")
#定义一个函数带参数行参数
def greet_user2(username):
    print("hello"+' '+username.title())
# 参数实参数，赋值给username
greet_user2('leikang')
greet_user2('lk')
#
print("\n")
def display_message():
    print("charet learn")
display_message()
def books(title='ve'):
    print("hello ,I like :"+' '+title.title())
books()    
#
print("\n")
#函数方法第一个行参数是不能单独赋值的，要么两个行参数一起，要么第二个参数单独赋值。
def make_shirt(sample,size):
    print("size is :"+''+str(size)+' '+"sample :"+' '+sample)
make_shirt(size=17,sample='Lo')
make_shirt(size =12,sample="op")
make_shirt(sample="leikang",size=3)
print("\n")
#
def des_city(city_name,country):
    full = city_name+' '+country
    return full.title()
    #print("Reykjava is in:"+' '+city_name)
    # print("\n")
   # print("country:"+country.title())
mas = des_city('dongjing','janpan')
print(mas)

#
print("\n")
def make_album(singer_name,album_name,album_number=''):
    music ={'singer':singer_name,'album':album_name}
    if album_number :
        music['album_number']=album_number
        return music
asd = make_album('maike'," Iove you",12)
make_album('alice',"qingqing")
make_album('cindy',"stret")
print(asd)
#带有循环体的函数
print("\n")
def make_album2(singer_name,album_name):
    full_name = singer_name +' '+album_name
    return full_name
while True :
    s_name = input(" please you name's")
    if s_name =='q':
        break
    
    a_name = input("please is album_name")
    if a_name =='q':
        break
        
lisd = make_album2(s_name,a_name)
print(lisd)
