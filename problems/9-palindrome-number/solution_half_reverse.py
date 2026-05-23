"""
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-.
Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:

-231 <= x <= 231 - 1
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Condition 1: Negative numbers can't be palindromes (they have a "-" sign)
        # Condition 2: Numbers ending in 0 can't be palindromes (except 0 itself)
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        # Variable to store reverse of x
        reverse_x = 0

        # Keep reversing the second half of x until
        # we've reversed half the digits
        while x > reverse_x:
            # Extract last digit and add to reversed number
            reverse_x = reverse_x * 10 + x % 10
            x = x // 10

        # Your explanation handles both even and odd length palindromes correctly.
        # For odd-length numbers (like 121), x == reverse_x // 10 handles the middle digit.
        # For even-length numbers (like 1221), x == reverse_x works.
        return x == reverse_x or (x == reverse_x // 10)


s = Solution()
print(s.isPalindrome(121))
print(s.isPalindrome(-121))
print(s.isPalindrome(0))
