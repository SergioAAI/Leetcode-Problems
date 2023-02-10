#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for n in s:
            if n not in d:
                d[n] = 1
            else:
                d[n] += 1
        
        for n in t:
            if n not in d:
                return False
            d[n] -= 1
        all_values = d.values()
        for n in all_values:
            print(n)
            if n is not 0:
                return False
        return True


        
# @lc code
