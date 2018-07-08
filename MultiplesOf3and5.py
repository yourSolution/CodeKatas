def sumOfMultiples3and5(ranges):
    sumList = []
    for i in range(1, ranges):
        if i % 3 == 0 or i % 5 == 0:
            sumList.append(i)
    return sum(sumList)


print(sumOfMultiples3and5(1000))
