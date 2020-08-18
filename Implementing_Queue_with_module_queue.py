#implementing queue with from collection module as deque class
from queue import Queue
#initializing an empty queue
q = Queue( maxsize = 4)
#inserting elements into the queue
q.put('a')
q.put('b')
q.put('c')
q.put('d')

#intial queue

#removing an element from queue

print("Queue after one pop operation is ")
print(q.get())
print(q.get())

