#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
from collections import deque
from typing import List
     
# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        numsQ = deque(nums)
        def recursive (numsDeque:deque , currentStr: List[List]):
            if(len(nums) == len(currentStr)):
                answer.append(currentStr[:])
                return
            for _ in range(len(numsDeque)):
                currentStr.append(numsDeque.pop())
                recursive(numsDeque, currentStr)
                numsDeque.appendleft(currentStr.pop())
        
        recursive(numsQ, [])
        return answer



            



            


        
# @lc code=end

