"""import json

numbers = [2,3,4,5,6,7,8,9]

filename = 'numbers.json'
with open(filename,'w') as f_obj:
    json.dump(numbers,f_obj
"""
import json
filename = 'numbers.json'
with open(filename) as f_bat:
     numbers = json.load(f_bat)
print(numbers)
