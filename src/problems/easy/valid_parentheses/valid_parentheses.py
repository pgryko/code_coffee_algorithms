"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

"""
from collections import deque


def isValid(s: str) -> bool:
    stack = deque()

    open_bracket_set = {"(", "[", "{"}

    negation_kv = {")": "(", "]": "[", "}": "{"}

    for char in s:
        if char in open_bracket_set:
            stack.append(char)

        elif char in negation_kv:
            opening_bracket = negation_kv[char]

            if stack[-1] == opening_bracket:
                stack.pop()

    return not bool(len(stack))
