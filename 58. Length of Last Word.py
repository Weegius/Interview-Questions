"""
Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # first, split the string into words
        words = s.split()
        # if there are no words, return 0
        if len(words) == 0:
            return 0
        # otherwise, return the length of the last word
        else:
            return len(words[-1])