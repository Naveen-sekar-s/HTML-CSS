# local scope varible , use this variable in a set of blocks only
a = 20  # global scope variable


def add():
    b = 30  # local scope variable
    print(a)
    print(b)
    return


add()  # 20,30


def add():
    print(a)
    print(b)  # there b is not defined // bcoz this function not contains a var(b)
    return


add()  # 20 & (gets name error (b) is not defined)
