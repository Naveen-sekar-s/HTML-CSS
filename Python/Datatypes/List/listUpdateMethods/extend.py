# print list using list Extend method
# extend()Adding another list in the present list
# eg(1)
a1 = [1000, 2000, 3000, 4000]
b1 = [5000, 6000, 7000, 8000]
a1.extend(b1)
print(a1)

# eg(2)
# adding new emp names in attendance
emplist = ["Arun", "Balaji", "Charan", "Dinesh", "Elizabath", "Farzila"]
newemplist = ["Madhu", "Nivetha"]
emplist.extend(newemplist)
print(emplist)
