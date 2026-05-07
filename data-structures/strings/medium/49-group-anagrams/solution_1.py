"""
49. Group Anagrams
Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:
There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""
from collections import Counter

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagarams = []
        n = len(strs)
        seen = {}

        for i in range(n):
            currItem = strs[i]
            currItemSize = len(currItem)

            if currItem in seen:
                continue

            temp = [currItem]
            seen[currItem] = True
            currItemMap = Counter(currItem)
            
            for j in range(i + 1, n):
                if currItemSize != len(strs[j]):
                    continue

                if currItemMap == Counter(strs[j]):
                    temp.append(strs[j])
                    seen[strs[j]] = True
            
            anagarams.append(temp)
        
        return anagarams
        
        
s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
