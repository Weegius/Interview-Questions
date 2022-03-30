"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # first, check if the number is negative
        if x < 0:
            return False
        # then, check if the number is palindrome
        elif x == 0:
            return True
        # otherwise, convert the number to a string
        else:
            x_str = str(x)
            # check if the string is palindrome
            return x_str == x_str[::-1]