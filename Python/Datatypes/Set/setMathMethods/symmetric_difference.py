# print set using set symmetric_difference method
# union or {^} //returns a set that contains all items from both set, but not the items that are present in both sets.
# eg(1)
s1 = {1000, 2000, 3000, 4000}
s2 = {3000, 4000, 5000, 6000}
print(s1.symmetric_difference(s2))  # {1000, 2000, 5000, 6000}

# eg(2)
s1 = {1000, 2000, 3000, 4000}
s2 = {3000, 4000, 5000, 6000}
print(s1 ^ s2)  # {1000, 2000, 5000, 6000}
