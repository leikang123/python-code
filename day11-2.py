import json


filename = 'username.json'
try:
    with open(filename) as obj:
       username = json.load(obj)
except FileNotFoundError:
    username = input(" what is you name?")
    with open(filename,'w')as obj:
        json.dump(username,obj)
        print(" well come you "+ username +"!")
else:
    print("I read is " + username +"!")
 
