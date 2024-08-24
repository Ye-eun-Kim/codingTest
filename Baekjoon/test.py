from collections import deque
queue = deque()
queue.append(0)
queue.append(7)
queue.append(9)

queue.pop()

print(queue, len(queue))