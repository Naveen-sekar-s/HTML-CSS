# get a key using a get method
d1 = {"ids": 133, "name": "Mandela", "sal": 75000, "loc": ["Heaven", "Hell"]}

# print ids
print(d1.get("ids"))

# print name
print(d1.get("name"))

# print sal
print(d1.get("sal"))

# print loc
print(d1.get("loc"))

# print location list using indexing
print(d1.get("loc")[1])

# print name without using get method
print(d1["name"])
