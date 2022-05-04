#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        begin = 0
        num = []
        
        end = len(nums) - 1
        mid = len(nums) // 2
        while end - begin >= 0:
            if(nums[mid] == target):
                return mid
            if(nums[mid] < target):
                
                begin = mid + 1
                mid = ((end - begin) // 2) + begin
                continue
            if(nums[mid] > target):
                end = mid - 1
                mid = ((end - begin) // 2) + begin
                continue
        return -1


# @lc code=end
