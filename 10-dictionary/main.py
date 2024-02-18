

l = [2,4,6,7]


"""
2=>0
4=>1
6=>2
7=>3

l[0]

user1['name'] 
"""


user = {"name": "John", "age": 30, "city": "New York","name":"mike"}
# print(user)
# user["age"] = 31
# user['salary'] = 100
# print(user)

# get method 

# print(user.get("name","not found"))

# pop 
# print(user.pop("name"))
# print(user)

# popitem
# print(user)
# print(user.popitem())
# print(user)
# nesting 

user = {
    "name": "John",
    "age": 30,
}


user2 = { "key "+i :i  for i in user  }

print(user2)


