"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
"""
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        size_s1 = len(s1)
        size_s2 = len(s2)

        if size_s1 > size_s2:
            return False
        
        counter_s1 = Counter(s1)
        counter_s2 = Counter()

        for i in range(size_s2):
            ch = s2[i]
            counter_s2[ch] = counter_s2.get(ch, 0) + 1

            if i >= size_s1:
                if counter_s2[s2[i - size_s1]] == 1:
                    del counter_s2[s2[i - size_s1]]
                else:
                    counter_s2[s2[i - size_s1]] -= 1
            
            if counter_s1 == counter_s2:
                return True
        
        return False


s = Solution()
print(s.checkInclusion("ab", "eidbaooo"))