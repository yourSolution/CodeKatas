def accum(s):
    final_string = ""
    i = 0
    for item in s:
        final_string += str(item.capitalize()) + item.lower() * i + "-"
        i += 1
    return (final_string[0:-1])

print(accum("abcdefghiJ"))

"""What I Learned 
        Remembering how to concatenate a string
        .capitalize()
        .lower()
"""