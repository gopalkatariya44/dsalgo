def selection_sort(list):
    sorted_list = []
    # print("%-25s %-25s" % (list,sorted_list))
    for i in range(0, len(list)):
        sorted_list.append(list.pop(index_of_min(list)))
        # print("%-25s %-25s" % (list,sorted_list))
    return sorted_list


def index_of_min(list):
    min_index = 0
    for i in range(0, len(list)):
        if list[i] < list[min_index]:
            min_index = i
    return min_index


ls = [2, 1, 4, 5, 6, 7, 0, 100, 47, 382, 377, 832, 999]

print(selection_sort(ls))
