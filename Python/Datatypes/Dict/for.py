# print dict items using for loop
d1 = {"ids": 133, "name": "Mandela", "sal": 75000, "loc": ["Heaven", "Hell"]}

# normal print method
for d in d1:
    print(d)

print("-------------------")

# print dict keys only
for keys in d1.keys():
    print(keys)

print("-------------------")

# print dict values only
for values in d1.values():
    print(values)

print("-------------------")

# print overall dict items
for keys, values in d1.items():
    print(keys, ":", values)
