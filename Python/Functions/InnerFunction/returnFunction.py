def outerFunction():
    print("Outer function printed")

    def innerFunction():
        print("Inner function printed")

    return innerFunction()  # when we return the innner function we get the values ,  function works But we not call the (innerFunction) separetly


outerFunction()
innerFunction() #name error : innerFunction is not defined.
