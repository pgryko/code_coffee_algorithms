"""
Given a string s, find the length of the longest
substring
 without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

"""


def longest_substring(string: str) -> int:

    max_substring = 0
    max_running_window = 0

    seen = set()

    start = 0
    end = 0

    while start < len(string) and end < len(string):
        if string[end] in seen:
            max_substring = max(max_substring, max_running_window)
            seen.remove(string[start])
            start = start + 1
            max_running_window -= 1
        else:
            max_running_window += 1
            seen.add(string[end])
            end = end + 1
    return max(max_substring, max_running_window)
