enames = ["Ragul", "Sonia", "Reddy", "Priyanka", "Mandela", "Modi", "Roja", "kuja"]

# print list using while loop
i = 0
while i <= 5:
    print(enames[i])
    i = i + 1

# using len() to find indexing length
i = 0
while i <= (len(enames)) - 1:
    print(i)
    i = i + 1

# Using while loop to instantly update & print enames
i = 0
while i <= len(enames) - 1:
    print(enames[i])
    i = i + 1

# print list using for loop
for enamess in enames:
    print(enamess)
