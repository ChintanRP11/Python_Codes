import json

data = {'name':'chintan', 'age':20, 'rno':111}

jsondata = json.dumps(data)
print(jsondata)
print(type(jsondata))

dict1 = json.loads(jsondata)
print(type(dict1))
print(dict1)
