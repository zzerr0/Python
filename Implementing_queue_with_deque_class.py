#implementing queue with from collection module as deque class
from collections import deque
#initializing an empty queue
queue = deque()
#inserting elements into the queue
queue.append('a')
queue.append('b')
queue.append('c')
queue.append('d')

#intial queue
print("Initial queue is ")
print(queue)

#removing an element from queue
queue.popleft()
print("Queue after one pop operation is ")
print(queue)

