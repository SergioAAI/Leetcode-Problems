#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letters_to_words = defaultdict(list)
        for word in strs:
            letters_to_words[tuple(sorted(word))].append(word)
        return list(letters_to_words.values())
        
        
        
         
                




        
        
# @lc code=end

