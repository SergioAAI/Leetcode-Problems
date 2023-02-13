#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = s.lower()
        queue = []
        for c in st:
            if(97 <= ord(c) <= 122 or 48 <= ord(c) <= 57):
                queue.append(c)
        if queue == list(reversed(queue)):
            return True
        else:
            return False
    
        
# @lc code=end

