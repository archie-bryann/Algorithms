def qsort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    lesser = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]
    return qsort(lesser) + [pivot] + qsort(greater)