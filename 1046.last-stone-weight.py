#
# @lc app=leetcode id=1046 lang=python3
#
# [1046] Last Stone Weight
#
import heapq 
# @lc code=start
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_heap = [x for x in stones]
        stones_heap = heapq.heapify(stones_heap)
        
# @lc code=end

