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
        char_index_map = {}

        # Check if the given strings have the same length
        if t_len != s_len:
            return False

        for i in range(t_len):
            currEl = t[i]
            j = char_index_map.get(currEl, 0)
            
            while j < t_len:
                # If the currEl is found, update the associated currEl value in the hashmap to j + 1
                # This is where we will start the iteration from the next time we visit the same element
                if currEl == s[j]:
                    char_index_map[currEl] = j + 1
                    break

                j += 1
            
            if j == t_len:
                return False

        return True


s = Solution()
print(s.isAnagram("anagram", "nagaram"))
print(s.isAnagram("anagramb", "nagaramc"))
print(s.isAnagram("rat", "car"))

# Time complexity: O(n^2)
# Space complexity: O(1)