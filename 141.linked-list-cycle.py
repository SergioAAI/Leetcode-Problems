#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        nums = {}
        curr = head
        while curr != None:
            if id(curr) in nums:
                return True
            else:
                nums[id(curr)] = True
                curr = curr.next

        return False

        
# @lc code=end

