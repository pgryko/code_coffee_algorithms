"""A simple hashmap, with collisions handled via a linked list
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


class HashChaining:

    def __init__(self):
        self.data = [None for _ in range(7)]
        self.capacity = 7
        self.count = 0

    def __len__(self):
        return self.count

    def string_to_int(self, string: str) -> int:
        """Converts a string into a large integer

        Method is based off java's hashcode function.

        For a string s, of length n, a hash is calculated using

        h(s) = s[0]*31^(0) + s[1]*31^(1) ... + s[n-2]*31^(n-2) + s[n-1]*31^(n-1)

        the reason 31 is chosen, is that its a prime number.
        If it where even and the multiplication overflowed, information
        would be lost.
        A neat property of 31 is that the multiplication can be replaced by a
        shift and subtraction for better performance.

        31^i === (i << 5) - i

        Most compilers and vms already optimise this
        """

        large_int = 0
        for index, char in enumerate(string):
            large_int += ord(char) * 2 ^ index
        return large_int

    def hash(self, message: str):
        """Generate a simple hash using division method

        base should ideally be a large prime number and,
        should avoid common bases, such as powers of 2 and 10.

        For signed ints, a trick is to use bit masking to
        mask out the signed bit (turn 32-bit signed int into 31-bit unsigned)
        key.hashCode() & 0x7fffffff

        For python, the % operator always returns a positive number
        regardless
        """
        return self.string_to_int(message) % self.capacity

    def _resize(self):
        """Resize data array

        Once data array becomes more than half full, change of collisions increases, so double + 1 size
        of underlying array
        """

        old_data = copy.deepcopy(self.data)

        # keep capacity odd to avoid powers of 2
        self.capacity = self.capacity * 2 + 1
        self.data = [None for _ in range(self.capacity)]
        self.count = 0

        for element in old_data:
            if element and len(element) > 0:
                for elem in element:
                    self.put(elem)

    def exists(self, message: str):
        index = self.hash(message)

        if self.data[index] is None or self.data[index] is []:
            return False

        if message in self.data[index]:
            return True
        else:
            return False

    def put(self, message: str):

        if self.exists(message):
            return

        # Re-size the underlying array if count becomes
        # larger than half the capacity
        if self.count > self.capacity // 2:
            self._resize()

        index = self.hash(message)

        if self.data[index] is None or self.data[index] is []:
            self.data[index] = [message]
        else:
            # Perform a linear search to see if element is in list
            if message not in self.data[index]:

                self.data[index].append(message)
                self.count += 1

    def delete(self, message: str):

        if not self.exists(message):
            raise IndexError

        index = self.hash(message)

        self.data[index].remove(message)
        self.count -= 1






