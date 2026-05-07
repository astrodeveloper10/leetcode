"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving 
the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Explanation:

The strings s and t can be made identical by:
    Mapping 'e' to 'a'.
    Mapping 'g' to 'd'.

Example 2:
Input: s = "f11", t = "b23"
Output: false

Explanation:

The strings s and t can not be made identical as '1' needs to be mapped to both '2' and '3'.

Example 3:
Input: s = "paper", t = "title"
Output: true

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
"""
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)

        # If the lengths are not equal, then they are not isomorphic
        if s_len != t_len:
            return False
        
        s_map_t = {}
        t_map_s = {}

        for i in range(s_len):
            s_char = s[i]
            t_char = t[i]
            
            if s_char not in s_map_t:
                if t_char in t_map_s:
                    return False

                s_map_t[s_char] = t_char
                t_map_s[t_char] = s_char
            else:
                if s_map_t[s_char] != t_char:
                    return False

        return True


s = Solution()
print(s.isIsomorphic("egg", "add"))
print(s.isIsomorphic("f11", "b23"))
print(s.isIsomorphic("paper", "title"))
print(s.isIsomorphic("badc", "baba"))