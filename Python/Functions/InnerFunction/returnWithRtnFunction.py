def outerFunction():
    print("Outer function printed")

    def innerFunction():
        print("Inner function printed")
        print("hello")
        return innerFunction  # refer the innerFunction must not use paranthesis()

    return (
        innerFunction()
    )  # when we before invoke the innerFunction we must reference the innerFunction by the help of return


x = outerFunction()
x()
