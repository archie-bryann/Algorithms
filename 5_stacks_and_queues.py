# Stacks(LIFO): Last in, First Out
stack = []
stack.append(5)
stack.append(10)
stack.append(15)
stack.append(20)
stack.pop()
stack.pop()
print("stack", stack)

# Queues(FIFO): First in, First Out
queue = []
# enqueue
queue.append(5)
queue.append(10)
queue.append(15)
queue.append(20)
# dequeue
queue.pop(0)
queue.pop(0)
print("queue", queue)

