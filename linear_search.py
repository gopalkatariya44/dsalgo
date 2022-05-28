from pickle import NONE

def linear_search(list, target):
    """
    Returns the index position of the targrt if found, else return None
    """
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None

def verify(index):
    if index is not None:
        print("Target found at index: ",index)
    else:
        print("Target not found in list")
        
list = [1,2,3,4,5,6,7,8,9]


result = linear_search(list,10)
verify(result)