# print set using set union method
# union or {|} //returns a set that contains all items from the original and specified set(s)
# eg(1)
s1 = {1000, 2000, 3000, 4000}
s2 = {3000, 4000, 5000, 6000}
print(s1.union(s2))  # {1000,2000,3000,4000,5000,6000}

# eg(2)
s1 = {1000, 2000, 3000, 4000}
s2 = {3000, 4000, 5000, 6000}
print(s1 | s2)  # {1000,2000,3000,4000,5000,6000}
