#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        iterations = len(nums) - (k % (len(nums))) 
        standby = []

        nums.reverse()
        for i in range(iterations):
            standby.append(nums.pop())

        nums.reverse()
        standby.reverse()

        for i in range(iterations):
            nums.append(standby.pop())
            

        
        
# @lc code=end

