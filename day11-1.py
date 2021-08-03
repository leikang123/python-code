import json
username = input(what is you name ? )
filename = 'username.json'
with open(filename,'w') as obj:
    json.dump(username,obj)
    print(" come wecome " + username + "!")
