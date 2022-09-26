def sum_of_arr(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + sum_of_arr(arr[1:])


def num_of_arr(arr):
    if not arr:
        return 0
    else:
        return 1 + num_of_arr(arr[1:])


def max_of_arr(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = max_of_arr(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max




