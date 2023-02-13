#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
from collections import defaultdict

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = defaultdict(int)

        for num in nums:
            num_dict[num] += 1
        
        num_sorted = dict(sorted(num_dict.items(), key=lambda item: item[1]))
        keys = list(num_sorted.keys())
        return keys[-k:]
        




        
# @lc code=end

