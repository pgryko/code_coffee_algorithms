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


class HashChaining:

    def __init__(self):
        self.data = []
        self.size = 0
        self.modulus = 31

    def string_to_int(string: str) -> int:
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

        """
        return abs(self.string_to_int(message)) % self.modulus
