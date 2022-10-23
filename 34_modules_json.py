import json

data = {'name':'chintan', 'age':20, 'rno':111}

# it stores dictionary data into json format. here it is stored as string
jsondata = json.dumps(data)
print(jsondata)
print(type(jsondata))

# it extract data from json to dictionary
dict1 = json.loads(jsondata)
print(type(dict1))
print(dict1)
