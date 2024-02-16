#we not call the inner function outside of the function
def outerFunction():
    print("Outer function printed")

    def innerFunction():
        print("Inner function printed")


outerFunction()
innerFunction()  # when we invoke a inner function outside the function we get (name error) innerFunction is not defined.
