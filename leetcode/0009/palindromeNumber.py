"""
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:
-231 <= x <= 231 - 1
 
Follow up: Could you solve it without converting the integer to a string?
"""


def palindromeNumber(x):
    if x < 0:
        return False
    # xString = str(x)

    # l = 0
    # r = len(xString) - 1
    # while l < r:
    #     if xString[l] != xString[r]:
    #         return False
    #     l += 1
    #     r -= 1
    # return True

    # return xString == xString[::-1]
    # O(n) time 
    # O(1) space

    inputNum = x
    res = 0
    while x > 0:
        res = res * 10 + x % 10
        x = x // 10
    return res == inputNum

print(palindromeNumber(-121))
