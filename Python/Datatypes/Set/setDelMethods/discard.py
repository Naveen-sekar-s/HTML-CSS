# discard() discard particular element in the set
# if the specified element is not there we not get any error
# eg(1)
a1 = {1000, 2000, 3000, 4000}
a1.discard(2000)
print(a1)

# eg(2)
b1 = {1000, 2000, 3000, 4000}
b1.discard(5000)
print(b1)

# eg(3)
enames = {"Ragul", "Sonia", "Reddy", "Priyanka", "Mandela", "Modi"}
enames.discard("Reddy")
print(enames)
