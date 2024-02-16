# print set using set intersection method
# intersection or {&} //returns a set that contains the similarity between two or more sets.
# eg(1)
s1 = {1000, 2000, 3000, 4000}
s2 = {3000, 4000, 5000, 6000}
print(s1.intersection(s2))  # {3000, 4000}

# eg(2)
s1 = {1000, 2000, 3000, 4000}
s2 = {3000, 4000, 5000, 6000}
print(s1 & s2)  # {3000, 4000}
