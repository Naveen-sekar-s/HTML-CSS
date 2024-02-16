# delete a particular in a dict using del method
d1 = {"ids": 133, "name": "Mandela", "sal": 75000, "loc": ["Heaven", "Hell"]}

# printing dict
print(d1)

# delete loc key
del d1["loc"]
print(d1)

# deletig sal key
del d1["sal"]
print(d1)

# deleting name key
del d1["name"]
print(d1)

# deleting ids key
del d1["ids"]
print(d1)
