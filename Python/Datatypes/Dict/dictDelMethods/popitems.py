# popitem method is not a correct way to remove a elements in dict
# bcoz dict indexing concept are not applicable. it removes the random element in a entire dict
d1 = {"ids": 133, "name": "Mandela", "sal": 75000, "loc": ["Heaven", "Hell"]}

# printing dict
print(d1)

# using pop item to deleting random key , values in a dict
d1.popitem()
print(d1)

d1.popitem()
print(d1)

d1.popitem()
print(d1)

d1.popitem()
print(d1)
