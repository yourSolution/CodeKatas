def high_and_low(numbers):

    stringList = list(map(int,numbers.split())) #Gets rid of spaces and turns str List to int List
    highestNum = stringList[0]
    lowestNum = stringList[0]

    for item in stringList:

        if  highestNum < item:
            highestNum = item

        elif lowestNum > item:
            lowestNum = item
    return str(str(highestNum) + " " + str(lowestNum))

""" What I learned:
Line 3 with the .split() and map()
split get rids of spaces and map converts str to int
Make sure we know what Outputs and Inputs we want
"""