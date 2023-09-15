#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start


from collections import deque


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      dq = deque()
      longestLength = 0
      i = 0

      while i < len(s):
        if s[i] not in dq:
          dq.append(s[i])
          i = i + 1
          if len(dq) > longestLength:
            longestLength = len(dq)
        else:
          dq.popleft()

      
      return longestLength




        
# @lc code=end

