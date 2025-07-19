# YouTube: Heaps and Priority Queue (Greg)

import heapq
from collections import Counter

A = [-4, 0, 1, 3, 2, 5, 10, 8, 12, 9]

heapq.heapify(A)
print(A)

# Heap Push (Insert Element)
# Time: O(log n)
heapq.heappush(A, 4)
print(A)

# Heap Pop (Extract min)
# Time: O(log n)
minn = heapq.heappop(A)
print(A, minn)

# Heap Sort
# Time: O(n log n), Space: O(n)
# Note: O(1) is possible via swapping, but this is complex
def heapsort(arr):
    heapq.heapify(arr)
    n = len(arr)
    new_list = [0] * n

    for i in range(n):
        minimum = heapq.heappop(arr)
        new_list[i] = minimum

    return new_list

print(heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))

# Heap Push Pop: Time O(log n)
heapq.heappushpop(A, 99)
print(A)

# Peek at Min: TIme O(1)
print(A[0])

# Max Heap
B = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]
n = len(B)

# for i in range(n):
#     B[i] = -B[i]

B = [-n for n in B]

heapq.heapify(B)
print(B)

# Insert 7 into the max heap
heapq.heappush(B, -7)
print(B)

# Build heap from scratch - Time O(n log n)
C = [-5, 4, 2, 1, 7, 0, 3]

heap = []
for x in C:
    heapq.heappush(heap, x)
    print(heap, len(heap)) # Check size on heap

# Putting tuples of items on the heap
D = [5, 4, 3, 5, 4, 3, 5, 5, 4]
counter = Counter(D)
print(counter)

heap = []

for k, v in counter.items():
    heapq.heappush(heap, (v, k)) # sort itself by v, then use k as a tie-breaker

print(heap)

