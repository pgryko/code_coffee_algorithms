# Implement an algorithm to determine if a string as all unique characters

# There is a difference between Unicode and ASCII characters. By default python3 uses unicode utf-8
# https://docs.python.org/3/howto/unicode.html
# Unicode allows for a max of 1,114,112 characters

def isunique(my_string: str):
    # Allocate bit array to keep track of whether we've seen
    # this is very memory in-efficient (around 8.5 MB)
    # A more memory efficient way would be to use a set()
    bit_array = [0]*1114112
    for char in my_string:
        char_val = ord(char)
        if not bit_array[char_val]:
            bit_array[char_val] = 1
        else:
            return False
    return True
