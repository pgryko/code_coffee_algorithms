"""A simple example hashing with chaining, with collisions handled via a linked list.
 This is equivalent to unordered sets rather than dicts, as we are not storing key value pairs
 Note: the python hash function salts the input before hashing.
 Hence hash(k) is deterministic only with the same process

 https://docs.python.org/3.9/reference/datamodel.html#object.__hash__

 For more deterministic hashing, cryptographic hash functions are available here

 https://docs.python.org/3.9/library/hashlib.html

 For this exercise, we will use a simple custom hash function, as we want some collisions to occur
 to demonstrate chaining

 References:
 https://algs4.cs.princeton.edu/34hash/
 https://softwareengineering.stackexchange.com/questions/49550/which-hashing-algorithm-is-best-for-uniqueness-and-speed

"""
import copy


class BinarySearchTree:

    def __init__(self):
        self.data = [None for _ in range(7)]
        self.capacity = 7
        self.count = 0

    def __len__(self):
        return self.count

    def search(self,value):
        pass

    def minimum(self):
        pass

    def predecessor(self,value):
        pass

    def successor(self,value);
        pass

    def insert(self,value):
        pass

    def delete(self, value):
        pass



