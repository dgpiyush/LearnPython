
# write 
# file = open('my_file.txt','w')
# file.write('hello')
# file.close()

# read 
# file = open('my_file.txt','r')
# print(file.read())
# file.close()


# append mode

# file = open('my_file.txt','a')
# file.write('hello')
# file.close()


# file = open('my_file.txt','w+')
# file.write('hello')
# print(file.read())
# file.close()

# with open('my_file.txt') as f:
#     print(f.read())


# import requests
# network_call = requests.get('https://media.istockphoto.com/id/487506120/photo/reticulated-python.jpg?s=2048x2048&w=is&k=20&c=JNXUfRxuEwHc_ar3vm8RRCjSi8GU18TZqJA117y7vOs=')
# imgfile = open('python.jpg','wb')
# imgfile.write(network_call.content)
# imgfile.close()

# import os 

# is_exist = os.path.exists('python1.jpg')
# # os.remove('python.jpg')
# os.rename('change.py','change.d')

# print(os.name)

# 13-python-files
# os.chdir('/Users/piyushmishra/Developer/code/py/LearnPython/13-python-files/de')
# de folder
# open("change.d","r")

# file = open("new.txt", 'w+')

# file.write("this is a new file")

# file.seek(0)

# print(file.read())

# file.write("hello")

# file.seek(0)
# print(file.read())

# file.close()

import json



# json.loads('{"name":"jhon"}')

# d = {
#     "name": "john",
#     "age": 30
# }
# js = json.dumps(d)
# print(js)
# print(type(js))
# with open('demo.txt','w') as f:
#     f.write(js)

users = []

with open("demo.txt") as f:
    data =  f.read()
    if data:
        users =  json.loads(data)
# register
# john 
user = {
    "name": "john",
    "age":80,
    "number": 4384398437,
    }
users.append(user)
json.dump(users)


# with open('demo.txt') as f:
#     data = f.read()
#     data = json.loads(data)
#     print(f.read())

# user management








