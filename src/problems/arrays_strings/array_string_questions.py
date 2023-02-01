# Implement an algorithm to determine if a string as all unique characters

# There is a difference between Unicode and ASCII characters. By default python3 uses unicode utf-8
# https://docs.python.org/3/howto/unicode.html
# Unicode allows for a max of 1,114,112 characters


def is_unique(my_string: str):
    # Allocate bit array to keep track of whether we've seen
    # this is very memory in-efficient (around 8.5 MB)
    # A more memory efficient way would be to use a set()
    # Or copy and sort the string
    bit_array = [0] * 1114112
    for char in my_string:
        char_val = ord(char)
        if not bit_array[char_val]:
            bit_array[char_val] = 1
        else:
            return False
    return True


# Given two strings, write a method to check if one is a permutaiton of another
# Ask whether it should be case sensitive
# two ways to approach this:
# Either sort the arrays and then compare
# Use an int vector and compare the count of each letter


def is_permutation(string1: str, string2: str):
    if len(string1) != len(string2):
        return False

    if sorted(string1) == sorted(string2):
        return True
    return False


# Palindrome Permutation: Given a string write a function which checks if it is a permutation of a palindrome
# A palindrome is a word or phrase that is the same forwards as it is backwards
# Example input: Tact Coa
# Output (permutations: 'taco cat', 'atco cta', etc)
# the trick is that for an odd length string, at most one character is allowed to be odd
# otherwise chars need to be even
# this can be said that no more than one char can be odd for both cases


def is_palindrome_permutation(my_string: str):
    if len(my_string) < 1:
        return False

    storage_dict = {}
    for char in my_string:
        if char not in storage_dict:
            storage_dict[char] = 1
        # Toggle value
        else:
            storage_dict[char] = not storage_dict[char]

    # There's a bit trick that can be done here, where if you subtract one and then 'AND' it
    # with the new number you get zero
    # 00010000 - 1 = 00001111
    # 00010000 & 00001111 = 0
    # This would work nicely with a C like language, but for python
    count = 0
    for values in storage_dict.values():
        count += values
    if count > 1:
        return False
    return True


# There are 3 types of edits that can be done on a string, insertion, replacement and deletion.
# Given a string, write a function that checks if they are one edit (or zero edits) away
# Example
# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bake -> false


def is_oneaway(string1: str, string2: str):
    def _single_insert(longstring: str, shortstring: str):
        # check whether a single insert has occurred
        # by default if longstring == shortstring + 1
        # at least they diff by one char, so check they only diff by one char
        index_long = 0
        b_diff = False
        for index_short in range(0, len(shortstring)):
            if shortstring[index_short] != longstring[index_long]:
                if b_diff:
                    return False
                b_diff = True
                index_long += 1

            index_long += 1

        return True

    # check for 3 cases
    if len(string1) == len(string2):
        # replacement
        bool_diff = False
        # As both strings are the same length, move between them comparing them
        for index in range(0, len(string1)):
            if string1[index] != string2[index]:
                # we want to track that ONLY one diff has changed
                if bool_diff:
                    # If boolean has previously been flipped false to true
                    # it means we've seen a diff before, so return false
                    return False
                bool_diff = True
        # return result (i.e. we've seen a diff (true), or not (false)
        return bool_diff

    if len(string1) == len(string2) + 1:
        # deletion
        return _single_insert(longstring=string1, shortstring=string2)
    elif len(string2) == len(string1) + 1:
        # insertion, note we've switched the string params
        return _single_insert(longstring=string2, shortstring=string1)
    # Else Strings differ by more than 1
    else:
        return False


# Implement a method to perform basic string compression using counts of repeated characters.
# E.g. aabcccccaaa -> a2b1c5a3.
# If the compressed string would not become smaller than the original, then return original string
# assume only uppercase and lowercase (a-z)


def string_compress(input_string: str):
    # Appending strings is expensive. Strings are immutable so
    # string concatenation requires all characters to be copied, this is a O(N+M)
    # operation (where N and M are the sizes of the input strings).
    # M appends of the same word will trend to O(M^2) time therefor.
    buffer = []
    consecutive = 0
    for index in range(0, len(input_string)):
        consecutive += 1

        if (
            index + 1 < len(input_string)
            and input_string[index] != input_string[index + 1]
        ):
            buffer.append(input_string[index] + str(consecutive))
            consecutive = 0
        elif index + 1 == len(input_string):
            buffer.append(input_string[index] + str(consecutive))
            consecutive = 0

    return "".join(buffer)


def reflect_matrix(matrix: list[list]) -> list[list]:
    # Reflect horizontally

    for n in range(0, len(matrix) // 2):
        matrix[n], matrix[-(n + 1)] = matrix[-(n + 1)], matrix[n]

    return matrix


def transpose_matrix(matrix: list[list]) -> list[list]:
    for i in range(0, len(matrix)):
        for j in range(i + 1, len(matrix[0])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    return matrix


#  Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes,
#  write a method to rotate the image by 90 degrees. Do this in place.
#  Tip: this involves a transpose and a reflection (order doesn't matter).
#  A reflection in the row results in a counter-clockwise transform
#  A reflection in the column results in a clockwise transform
def rotate_matrix(matrix: list[list]) -> list[list]:
    """Rotate a matrix 90 in place"""
    reflect_matrix(matrix)
    transpose_matrix(matrix)

    return matrix
