"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0

Explanation:
The character 'l' at index 0 is the first character that does not occur at any other index.

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1

Constraints:
1 <= s.length <= 105
s consists of only lowercase English letters.
"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_counter = {}

        # Traverse the string
        for ch in s:
            # Add the frequency of each character to the dictionary
            s_counter[ch] = s_counter.get(ch, 0) + 1

        # Traverse the string again 
        for index, ch in enumerate(s):
            # For each index, check if the character count is 1 at that index
            # Return the index, if True
            if s_counter[ch] == 1:
                return index
        
        return -1
    
s = Solution()
print(s.firstUniqChar("leetcode"))
print(s.firstUniqChar("loveleetcode"))

# Time complexity: O(n)
# Space complexity: O(1) since the string contains only lower case letters