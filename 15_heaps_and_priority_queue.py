# A heap is a specialized tree-based data structure that satisfied the heap property: if B is a child node of A,
# then key(A) ≥ key(B). This is a max heap. A min heap works in reverse.

# A priority queue is a special type of queue in which each element is associated with a priority value. And,
# elements are served on the basis of their priority. That is, higher priority elements are served first. However,
# if elements with the same priority occur, they are served according to their order in the queue.

# A heap is an implementation of priority queue. It's a binary tree. Runtime is O(log n) unlike sorting.

from heapq import heapify, heappop, heappush, _heapify_max, _heappop_max, merge

data = [10, 20, 43, 1, 2, 65, 17, 44, 2, 3, 1]

heapify(data)  # min-heap
print(data)

heappop(data)  # this pops the first elements and heapify's the data unlike the usual 'pop'
print(data)

heappush(data, 1)
print(data)

_heapify_max(data) # max-heap
print(data)

print(_heappop_max(data)) # pop first elm from max-heap

l1 = [10, 20, 30, 40, 50]
l2 = [15, 25, 35, 45, 55]

l3 = merge(l1, l2)
print(list(l3))



# i
# 2*i+1
# 2*i+2

