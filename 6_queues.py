# We make use of a library because
# de-queuing with .pop(0) produced a
# runtime of O(n) which is slow,
# hence we use this to reduce runtime to O(1)

from collections import deque

data = deque()
data.append("Caleb")
data.popleft()
print(data)
