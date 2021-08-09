"""
#汽车租
car = input("what is it car ?")
print("Let mw see if I can find you a Subaru :"+' '+car)
print("\n")
men = int(input("how much have pople meat,please?"))
print(men)
if men > 8 :
     print("Not")
else :
     print("Yes")
print("\n")
number = int(input("please input number :"))
print(number)
if number % 10 == 0 :
    print("Yes")
else :
    print("No")
#
per = " please input pizza:"
while True :
    message = input(per)

    if message == 'quite' :
       break
    else:
      print("ok, This is pizza"+' '+message)
      """
"""
age = "please input you age :"
while True:
    num = int(input(age))

    if num < 3:
        print("免费")
    elif  num < 12 :
        print("$10")
    elif num >= 12:
        print("$15")
    elif num == 'quite':
        print("bye")
        """
print("\n")
so = ['pas','pizza','hu']
fs = [];
while so :
  us = so.pop()
  print(us.title())
  fs.append(us)
for s in fs :
    print(s.title())
    
