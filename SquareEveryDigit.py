def square_digit(num):
    strNum = str(num)
    finalNum = []
    for number in strNum:
        finalNum.append(str((int(number) ** 2)))
    return int("".join(finalNum))
print(square_digit(9119))