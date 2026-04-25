"""
Given a string s, return true if the s can be palindrome after deleting 
at most one character from it.

Example 1:
Input: s = "aba"
Output: true

Example 2:
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Example 3:
Input: s = "abc"
Output: false

Constraints:
1 <= s.length <= 105
s consists of lowercase English letters.
"""
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(s, left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                
                left += 1
                right -= 1
            
            return True
        
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return checkPalindrome(s, left, right - 1) or checkPalindrome(s, left + 1, right)
            
            left += 1
            right -= 1
        
        return True

s = Solution()
print(s.validPalindrome("aba"))
print(s.validPalindrome("abca"))
print(s.validPalindrome("abc"))
print(s.validPalindrome("cbbcc"))
print(s.validPalindrome("zryxeededexyz"))
print(s.validPalindrome("eceec"))
