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
        size_s = len(s)
        size_t = len(t)

        if size_s != size_t:
            return False
        
        counter_s = {}

        for ch in s:
            counter_s[ch] = counter_s.get(ch, 0) + 1
        
        for ch in t:
            # If the character is not in counter_s then they are not anagrams
            # If the frequency of the character is 0, it means that "t"
            # contains the character more number of times than "s"
            if ch not in counter_s or counter_s[ch] == 0:
                return False

            counter_s[ch] -= 1
        
        return True


s = Solution()
print(s.isAnagram("anagram", "nagaram"))
print(s.isAnagram("anagramb", "nagaramc"))
print(s.isAnagram("rat", "car"))

# Time complexity: O(n + m)
# Space complexity: O(1)