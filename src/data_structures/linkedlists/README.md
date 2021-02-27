# Linked List
Datastructure where objects are arranged in a linear order, with orders determined by pointers in each object. They provide an easy method for creating dynamic sets.


```al
List-Search(L,k)
x = L.head
while X != NIL and x.key != k
	x = x.next
return x
```

```al
List-Insert(L,X)

```


## Build

$ cmake -H. -Bbuild
$ cd build; make
$ ./linkedlist

Or manually using g++
$ g++ --std=c++1z main.cpp