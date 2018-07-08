import math

def comp(array1, array2):
    switch = True
    if not array1 and not array1:
        switch = False
    else:
        while switch == True:
            for item in array2:
                if math.sqrt(item) in array1:
                    switch = True
                else:
                    switch = False
                    break
            break

    return switch

a1 = [113, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]

print (comp(a1,a2))

# What I learned:
"""             Sqrt 
                Test for all cases"""