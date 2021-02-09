# Queues

First in, First out (FIFO) Queues, supporting Insert, Enqueue, Dequeue, Pop.
The Queues have a head and a tail.

```al
ENQUEUE(Q,x):
Q[Q.tail] = x
if Q.tail == Q.length
	Q.tail = 1
else Q.tail = Q.tail + 1
```

```al
DEQUEUE(Q):
x = Q[Q.head]
if Q.head == Q.length
	Q.head = 1
else Q.head = Q.head + 1
return x
```