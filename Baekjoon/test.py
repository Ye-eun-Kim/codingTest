from collections import deque
queue = deque()
queue.append(0)
queue.append(7)
queue.append(9)

queue.pop()
for el in queue:
    print(el)
print(queue, len(queue))