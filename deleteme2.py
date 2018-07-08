


newList = []
for number in range(1, 600851475143, 2):
    if 600851475143 % number == 0:
        print(number)
        newList.append(number)


list = [71,839,1471,6857,59569,104441,486847,1234169,5753023,10086647,87625999,408464633,716151937,8462696833]



def delete2(number):
    newerList= []
    for numbers in range(1, number):
        if number % numbers == 0:
            print(numbers)
            newerList.append(numbers)
