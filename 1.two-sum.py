#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targetNums = {}
        position = []

        for i, num in enumerate(nums):
            targetNums[target - num] = [i, num]

        for i, num in enumerate(nums):
            currentNum = targetNums.get(num)
            if currentNum == None:
                continue
            elif currentNum[0] != i:
                position.append(i)
                position.append(currentNum[0])
                break

        return position


# @lc code=end
