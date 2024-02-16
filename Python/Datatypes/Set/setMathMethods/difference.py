# print set using set difference method
# difference or {-} //returned set contains items that exist only in the first set, and not in both sets.
# eg(1)
s1 = {1000, 2000, 3000, 4000}
s2 = {3000, 4000, 5000, 6000}
print(s1.difference(s2))  # {1000, 2000}

# eg(2)
s1 = {1000, 2000, 3000, 4000}
s2 = {3000, 4000, 5000, 6000}
print(s1 - s2)  # {1000, 2000}
