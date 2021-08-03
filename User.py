class User():

      def __init__(self,fname,lname):
          self.fname = fname
          self.lname = lname

      def d_user(self):
          print("my first is :" + self.fname.title())
          print("my last is :" + self.lname.title())

      def greet_user(self):
          print("hello !")
          
my_user = User("lei","kang")
haha_user = User("li","jian")
kaka_user = User("fang","zhi")
my_user.d_user()
my_user.greet_user()
haha_user.d_user()
haha_user.greet_user()
kaka_user.d_user()
kaka_user.greet_user()
