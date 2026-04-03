"""
Given two strings ransomNote and magazine, return true if ransomNote can be 
constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true

Constraints:
    - 1 <= ransomNote.length, magazine.length <= 105
    - ransomNote and magazine consist of lowercase English letters.
"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine) or not ransomNote:
            return False
        
        magazine_map = {}

        for char in magazine:
            magazine_map[char] = magazine_map.get(char, 0) + 1
        
        for char in ransomNote:
            if char not in magazine_map or magazine_map[char] == 0:
                return False
            
            magazine_map[char] -= 1

        return True

s = Solution()
print(s.canConstruct("aabbcc", "abcabc"))
print(s.canConstruct("a", "b"))
print(s.canConstruct("aa", "ab"))
print(s.canConstruct("aa", "aab"))
