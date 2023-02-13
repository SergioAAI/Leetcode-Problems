#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first_p = 0
        second_p = len(numbers)-1
        while first_p < second_p:

            if (numbers[first_p] + numbers[second_p]) == target:
                return [first_p + 1,second_p + 1]
            
            if numbers[first_p] + numbers[second_p] < target:
                first_p += 1
            else:
                second_p -= 1
            
            



        
# @lc code=end

