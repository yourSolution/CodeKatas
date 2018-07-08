def largestPrimeFactor(numbers):
    #returns the largest prime factors of "number"
    newList = []
    for number in range(1, numbers):
        if numbers % number == 0:
            newList.append(number)
    return newList

print(largestPrimeFactor(600851475143))


