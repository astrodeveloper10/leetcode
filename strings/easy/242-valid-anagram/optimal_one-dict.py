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
        s_len = len(s)
        t_len = len(t)
        s_map = {}

        # Check if the given strings have the same length
        if t_len != s_len:
            return False

        for i in range(s_len):
            s_map[s[i]] = s_map.get(s[i], 0) + 1
        
        for i in range(t_len):
            currEl = t[i]
            count = s_map.get(currEl, 0)

            if count == 0:
                return False
            
            s_map[currEl] = s_map[currEl] - 1
        
        return True


s = Solution()
print(s.isAnagram("anagram", "nagaram"))
print(s.isAnagram("anagramb", "nagaramc"))
print(s.isAnagram("rat", "car"))

# Time complexity: O(n)
# Space complexity: O(1)