"""
Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.

Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

Constraints:
1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s) - 1
        last_word_length = 0

        # Traverse the string from right to left until we encounter a letter
        # This is where the last word begins
        while n >= 0 and s[n] == " ":
            n -= 1

        # Traverse the string from the right to left until we encounter a whitespace
        while n >= 0 and s[n] != " ":
            last_word_length += 1
            n -= 1

        return last_word_length


s = Solution()
print(s.lengthOfLastWord("   fly me   to   the moon  "))
print(s.lengthOfLastWord("Hello World"))
print(s.lengthOfLastWord("luffy is still joyboy"))
