#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        p1, p2 = 0, max(piles)
        res = max(piles)

        def eating(k: int):
            answer = 0
            for pile in piles:
                answer = answer + math.ceil(pile / k) 
            return answer
            
        while p1 < p2:
            mid = p1 + (p2 - p1)//2
            eatingSpeed = eating(mid)
            if eatingSpeed <= h:
                res =  min(mid,res)
                p2 = mid - 1
            else:
                p1 = mid +1
                
        return res







        



        


        
# @lc code=end

