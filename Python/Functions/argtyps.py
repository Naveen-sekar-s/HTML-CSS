# arguments have 4 types there are;
# positional argument
def add(a, b):
    print(a + b)


add(10, 20)


# named arguments
def add(a, b):
    print(a + b)


add(b=20, a=10)


# default arguments
def add(a, b, c=100):
    print(a + b + c)


add(b=20, a=10)


# variable , length arguments
def add(a, b, *c):
    print(a, b, c)


add(10, 20, 30)
add(10, 20, 30, 40)
add(10, 20, 30, 50, 60)
add(10, 20, 30, 70, 80, 90)
