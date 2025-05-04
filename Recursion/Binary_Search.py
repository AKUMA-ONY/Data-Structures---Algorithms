#Binary Search, that is used to efficiently locate a target
#value within a sorted sequence of n elements.

# mid = [(low + high)/2]

#We consider three cases:
#If the target equals data[mid], then we have found the item we are looking for, and search terminates successfully.
#If target < data[mid], then we recur on the first half of the sequence, that is, on the interval of indices from low to mid - 1.
#If target > data[mid], then we recur on the second half of the sequence, that is, on the interval of indices from mid + 1 to high.

#An unsuccessful search occurs if low > high, as the interval [low, high] is empty.

def binary_search(data, target, low, high):
    """Return True if target is found in indicated portion of a Python list.
    
    The search only considers the portion from data[low] to data[high] inclusive.
    """
    if target > high:
        return False

    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            #recur on the portion left of the middle
            return binary_search(data, target, low, mid - 1)
        else:
            #recur on the portion right of the middle
            return binary_search(data, target, mid + 1, high)
        
        

print(binary_search([1, 2, 3, 4, 5], 6, 1, 5)) #True