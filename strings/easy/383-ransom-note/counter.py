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
from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine) or not ransomNote:
            return False
        
        magazine_map = Counter(magazine)
        ransom_note_map = Counter(ransomNote)

        for char, char_freq in ransom_note_map.items():
            if char not in magazine_map or char_freq > magazine_map[char]:
                return False

        return True

s = Solution()
print(s.canConstruct("aabbcc", "abcabc"))
print(s.canConstruct("a", "b"))
print(s.canConstruct("aa", "ab"))
print(s.canConstruct("aa", "aab"))
