def fibonacciNumbers(range):
    list = [1,2]
    i = 0
    while list[-1] < range:
        firstNum = list[i]
        secondNum = list[i + 1]

        list.append(firstNum + secondNum)
        i += 1
    del list[-1]
    return list
print(fibonacciNumbers(10))


def getEvenNumbers(list):
    evenList = []
    for number in list:
        if number % 2 == 0:
            evenList.append(number)
    return sum(evenList)

print(getEvenNumbers(fibonacciNumbers(4000000)))




