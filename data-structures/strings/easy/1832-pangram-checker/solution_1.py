"""
1832. Check if the Sentence Is Pangram

A pangram is a sentence where every letter of the English alphabet appears at least once.
Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

Example 1:
Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.

Example 2:
Input: sentence = "leetcode"
Output: false

Constraints:
1 <= sentence.length <= 1000
sentence consists of lowercase English letters.
"""
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(sentence) < 26:
            return False

        counter = [0] * 26
        char_a = ord('a')

        for ch in sentence:
            index = ord(ch) - char_a
            counter[index] += 1
        
        for count in counter:
            if count == 0:
                return False
        
        return True

s = Solution()
print(s.checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))
print(s.checkIfPangram("leetcode"))