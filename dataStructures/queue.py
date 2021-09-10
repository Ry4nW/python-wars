# Implementing a queue using a list and append()/pop() as enqueue()/dequeue

queue = []

for i in range(3):
    queue.append(i)

print(queue)

print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

# Python's Collections Module 

from collections import deque

queue = deque()

for i in range(3):
    queue.append(i)

print(queue)