"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. 

Specifically:
Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.

Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Explanation:
The bijection can be established as:
'a' maps to "dog".
'b' maps to "cat".

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false

Constraints:

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.
"""
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words_s = s.split()
        words_s_len = len(words_s)
        pattern_len = len(pattern)

        if pattern_len != words_s_len:
            return False
        
        word_to_letter_map = {} # word to letter map
        letter_to_word_map = {} # letter to word map

        for i in range(pattern_len):
            letter = pattern[i]
            word = words_s[i]

            if (letter in letter_to_word_map and letter_to_word_map[letter] != word) or (
                word in word_to_letter_map and word_to_letter_map[word] != letter):
                return False

            letter_to_word_map[letter] = word
            word_to_letter_map[word] = letter
        
        return True
            

s = Solution()
print(s.wordPattern("abba", "dog cat cat dog"))
print(s.wordPattern("abba", "dog cat cat fish"))
print(s.wordPattern("aaaa", "dog cat cat dog"))
print(s.wordPattern("abba", "dog dog dog dog"))

