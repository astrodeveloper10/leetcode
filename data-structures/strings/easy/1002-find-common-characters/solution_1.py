"""
1002. Find Common Characters

Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). 
You may return the answer in any order.

Example 1:
Input: words = ["bella","label","roller"]
Output: ["e","l","l"]

Example 2:
Input: words = ["cool","lock","cook"]
Output: ["c","o"]
 
Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.
"""
class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        words_size = len(words)
        result = []
        common_character_counts = {}

        for ch in words[0]:
            common_character_counts[ch] = common_character_counts.get(ch, 0) + 1
        
        for i in range(1, words_size):
            current_character_counts = {}
            
            for ch in words[i]:
                current_character_counts[ch] = current_character_counts.get(ch, 0) + 1
            
            for ch in common_character_counts.keys():
                common_character_counts[ch] = min(common_character_counts[ch], current_character_counts.get(ch, 0))
        
        for ch, count in common_character_counts.items():
            if count:
                for _ in range(count):
                    result.append(ch)
        
        return result

        
s = Solution()
print(s.commonChars(["bella","label","roller"]))
print(s.commonChars(["cool","lock","cook"]))