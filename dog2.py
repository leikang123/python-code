from dog import Dog


class Dog():

    def _init_(self,name,age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title()+"is now sitting")

    def roll_over(self):
        print(self.name.title()+"roll over.")

    
my_dog = Dog('While',6)
my_dog.sit()
my_dog.roll_over()

print("my dog's name is "+my_dog.name.title() +".")
print("my dog is "+str(my_dog.age)+"year old.")
