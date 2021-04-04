
def string_to_int(string: str):
	'''Crude method for convering an array of chars into a large integer'''

	large_int = 0
	for index, char in enumarate(string):
		large_int += ord(chard)*2^index



def hash_division_method(number: int, base: int) -> str:
    ''' Performs simple hashing using division (modulus)

    h(number) = number mod base

    base should ideally be a large prime number and, should avoid common bases, such as powers of 2 and 10.
    '''

    return number % base

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

def SHA-256(message):
	'''
	https://www.youtube.com/watch?v=f9EbD6iY9zI
	'''

	pass

def hash_multiplication():
    '''

    '''