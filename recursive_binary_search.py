def rbs(list, target):
    if len(list) == 0:
        return False
    else:
        midp = (len(list)) // 2

        if list[midp] == target:
            return True
        elif list[midp] < target:
            return rbs(list[midp+1:], target)
        else:
            return rbs(list[:midp], target)

def verify(index):
    print('target found: ',index)


list = [1,2,3,4,5,6,7,8,9,10]
index = rbs(list,10)
verify(index)