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
    for index, char in enumerate(string):
        # ord() returns an integer representing a unicode character
        large_int += ord(char) * 31 ^ index
    return large_int


def hash_division_method(number: int, base: int) -> int:
    ''' Performs simple hashing using division (modulus)

    h(number) = number mod base

    base should ideally be a large prime number and, should avoid common bases, such as powers of 2 and 10.
    '''

    return number % base


def SHA256(message: str) -> int:
    '''
    https://www.youtube.com/watch?v=f9EbD6iY9zI
    '''

    return 0


def md5(message):
    '''MD5 processes a variable length message into an output of 128 bits.
    Its an insecure (not suitable for cryptography) hash

    Input message is broken up into chunks of 512-bit blocks (16 32-bit words), with the message padded so that it is
    divisible by 512 (2^9).
    Padding is performed as follows:

    First a single bit 1 is appended to the end of the message. This is followed by as many zeros, untill the message
    is 64 bits fewer, than being divisible by 512. The remaining bits are filled up with 64 bits representing
    length of the original message, mod 2^64

    The main MD5 algorithem operates on a 128 bit state, divied into four 32-bit words, denoted A, B, C, D.
    These are initialised into fixed constants. The main alogrithem uses each 512 block in turn to modify the state.

    https://referencesource.microsoft.com/#System.Workflow.Runtime/MD5HashHelper.cs,5a97802b6014fccc,references
    '''
    pass
