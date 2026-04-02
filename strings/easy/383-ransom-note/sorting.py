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
        
        ransom_note_arr = sorted(ransomNote)
        magazine_arr = sorted(magazine)
        ransom_note_len = len(ransom_note_arr)

        i = 0
        j = 0

        while i < ransom_note_len and j < len(magazine_arr):
            # If both chars are equal, increment both by 1
            if ransom_note_arr[i] == magazine_arr[j]:
                i += 1
                j += 1
            # If ransom note character is greater than the current magazine character
            # then, increment j by 1
            elif ransom_note_arr[i] > magazine_arr[j]:
                j += 1
            else:
                return False
        
        # If i is not equal to ransom note list length, it means that the ransom note
        # is not iterated completely
        return i == ransom_note_len
        
        

s = Solution()
print(s.canConstruct("aabbcc", "abcabc"))
print(s.canConstruct("a", "b"))
print(s.canConstruct("aa", "ab"))
print(s.canConstruct("aa", "aab"))
print(s.canConstruct("apples", "apple"))