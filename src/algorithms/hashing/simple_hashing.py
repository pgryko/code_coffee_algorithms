'''
Examples of simple hashing techniques that can be used for hash tables
'''


def hashcode(string: str):
	'''Converts a string into a large integer
    
    both the name and method is based off java's
    hashcode function.

    For a string s, of length n, a hash is calculated using

    h(s) = s[0]*31^(0) + s[1]*31^(1) ... + s[n-2]*31^(n-2) + s[n-1]*31^(n-1)

    the reason 31 is chosen, is that its a prime number.
    If it where even and the multiplication overflowed, information
    would be lost.
    A neat property of 31 is that the multiplication can be replaced by a
    shift and subtraction for better performance.

    31^i === (i << 5) - i

    Most compilers and vms already optimise this
    '''

	large_int = 0
	for index, char in enumarate(string):
		large_int += ord(chard)*31^index

    return large_int



def hash_division_method(number: int, base: int) -> str:
    ''' Performs simple hashing using division (modulus)

    h(number) = number mod base

    base should ideally be a large prime number and, should avoid common bases, such as powers of 2 and 10.
    '''

    return number % base