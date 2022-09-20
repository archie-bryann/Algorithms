def binary_search(_list, item):
    low = 0
    high = len(_list) - 1

    while low <= high:
        mid = round((low + high) / 2)
        guess = _list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 2, 3, 4, 5,6,7,8,9,10,11,12,13,14,15,16]
print(binary_search(my_list, -1))
