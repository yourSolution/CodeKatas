def disemvowel(string):
    vowels = ["a","e","i","o","u", "A", "E", "I", "O", "U"]
    newList = []
    for item in string:
        newList.append(item)
        for item2 in newList:
            if item2 in vowels:
                newList.remove(item2)
    return "".join(newList)


print(disemvowel("This website is for losers LOL!"))