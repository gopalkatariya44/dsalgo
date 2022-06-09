def quick_sort(list):
    if len(list) <= 1:
        return list
    else:
        less_then_pivot = []
        greater_then_pivot = []
        pivot = list[0]
        for i in list[1:]:
            if i <= pivot:
                less_then_pivot.append(i)
            else:
                greater_then_pivot.append(i)
        print("%15s %1s %-15s" % (less_then_pivot, pivot, greater_then_pivot))
        return quick_sort(less_then_pivot) + [pivot] + quick_sort(greater_then_pivot)


ls = [2, 7, 8, 9, 1, 4, 6, 0, 3]
print(ls)
print(quick_sort(ls))
