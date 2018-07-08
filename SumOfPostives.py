def positive_sum(arr):
    i = 0
    for item in arr:
        if item < 0:
            arr[i] = 0
        i += 1
    return (sum(arr))

array = [-1,-2,-3,-4,-5]

print(positive_sum(array))

""" 
What I learned from this:
    Functions to remove items from a list:
    
        list.pop(index) - removes and returns the index. No parameter returns the last index.
        del list[] - remove item at specific index
        list.remove - the value in the list
    
    del does not work with lists when you don't index them 
    remove does not work in this case either
    
    


"""