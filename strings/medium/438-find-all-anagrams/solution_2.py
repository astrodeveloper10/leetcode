"""
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

Constraints:

1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.
"""
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        size_s = len(s)
        size_p = len(p)

        if size_p > size_s:
            return []
        
        counter_p = Counter(p)
        counter_s = Counter()
        result = []

        for i in range(size_s):
            counter_s[s[i]] = counter_s.get(s[i], 0) + 1

            if i >= size_p:
                if counter_s[s[i - size_p]] == 1:
                    del counter_s[s[i - size_p]]
                else:
                    counter_s[s[i - size_p]] -= 1
            
            if counter_s == counter_p:
                result.append(i - size_p + 1)
        
        return result


s = Solution()
print(s.findAnagrams("cbaebabacd", "abc"))

# Time complexity: O(n)
# Space complexity: O(k)