def FibonacciNumbers(range):
    fibList = [1,2,3]
    newList = []

    while fibList[-1] < range:
        for number in fibList:
            newList.append(number + (fibList[fibList.index(number) - 1]))
            print(newList)

FibonacciNumbers(10)


#return index of list ["foo","bar","baz"].index("bar") = 1