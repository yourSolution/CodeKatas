def remove_smallest(numbers):
    if numbers == [] or len(numbers) == 1:
        numbers = []
    else:
        lowestValue = min(numbers)
        i = 0
        for item in numbers:
            if lowestValue == item and i == 0:
                numbers.remove(lowestValue)
                i =+ 1
    return numbers


""" Study this one """