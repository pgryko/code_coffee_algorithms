# Stacks

Last-in, first-out (LIFO) queues. Support Push and Pop operations.
They can be implemented using a linked list or inside an array (risks head & tail running into each other)

```al
Stack-Empty(S):

if S.top == 0
	return True
else return False
```

```al
Push(S,x):
S.top = S.top + 1
S[S.top] = x
```

```al
Pop(S):
if Stack-Empty(S)
	error "underflow"
else S.top = S.top -1
	return S[S.top + 1]
```
