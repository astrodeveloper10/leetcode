"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def char_count(s):
            count = {}

            for ch in s:
                if ch not in count:
                    count[ch] = 0
                
                count[ch] += 1
            
            return count
        
        return char_count(s) == char_count(t)


s = Solution()
print(s.isAnagram("anagram", "nagaram"))
print(s.isAnagram("anagramb", "nagaramc"))
print(s.isAnagram("rat", "car"))

# Time complexity: O(n + m)
# Space complexity: O(n + m)