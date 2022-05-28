from cv2 import merge, split


def merge_sort(list):
    """
    Sorts a list in ascending order\n
    return a new sorted list\n

    Divide: find the midpoint of the list and divide into sublists\n
    Conquer: Recursively sort the sublist created in previous step\n
    Combine: Merge the sorted sublists created in previous step
    """
    print("merge_sort used")
    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(list):
    """
    Divide the unsorted list at midpoint into sublists
    Returns two sublists - left and right
    """

    mid = len(list)//2

    left = list[:mid]
    right = list[mid:]

    return left, right


def merge(left, right):
    """
    Merges two lists (arrays), sorting them in the process\n
    Returns a new merged lisst
    """

    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1
    while i < len(left):
            l.append(left[i])
            i += 1
    while j < len(right):
            l.append(right[j])
            j += 1
    return l


def verify_sorted(list):
    n = len(list)

    if n == 0 or n == 1:
        return True
    return list[0] < list[1] and verify_sorted(list[1:])

mylist = [1,2,3,4,5,1]

print(verify_sorted(mylist))