def outerFunction():
    print("Outer function printed")

    def innerFunction():
        print("Inner function printed")

    return innerFunction  # when we refer the innerFunction must not use paranthesis()


x = outerFunction()

x()
x()  # using with the help of outerfunction return reference to invoke a innerFunction lot of times
