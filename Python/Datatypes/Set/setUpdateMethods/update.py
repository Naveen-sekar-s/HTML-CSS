# update() update the multiple elements in the set
# update iterable objects in the set
# eg(1)
eid = {40, 60, 70, 80, 90, 100}
newids = {10, 20, 30, 50}
eid.update(newids)
print(eid)

# attendance here
# eg(2)
empset = {
    "Arun",
    "Balaji",
    "Dinesh",
    "Elizabath",
    "Farzila",
}
newemp = {5, "Mohan"}
empset.update(newemp)
print(empset)

# eg(3)
ids = {101, 102, 103, 104, 105}
ids.update([106, 107], range(9))
print(ids)
