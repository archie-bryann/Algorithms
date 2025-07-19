# Quick sort uses Divide and Conquer
# D&C algorithms are recursive algorithms

def qsort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    lesser = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]
    return qsort(lesser) + [pivot] + qsort(greater)

print(qsort([3,5,2,1,4]))
