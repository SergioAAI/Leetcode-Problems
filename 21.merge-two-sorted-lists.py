#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = list1
        curr2 = list2
        head = None
        temp = None
        if not curr:
            return curr2
        if not curr2:
            return curr

        if curr.val <=  curr2.val:
            head = curr
            while curr.next:
                if curr.next.val <= curr2.val:
                    curr = curr.next
                else:
                    break
            temp = curr.next
            curr.next = curr2 
            curr  = temp
        else:
            head = curr2
            while curr2.next:
                if curr2.next.val < curr.val:
                    curr2 = curr2.next
                else:
                    break
            temp = curr2.next
            curr2.next = curr 
            curr2  = temp
    


        while curr and curr2:
            if curr.val <=  curr2.val:
                while curr.next:
                    if curr.next.val <= curr2.val:
                        curr = curr.next
                    else:
                        break
                temp = curr.next
                curr.next = curr2 
                curr  = temp
            else:
                while curr2.next:
                    if curr2.next.val < curr.val:
                        curr2 = curr2.next
                    else:
                        break
                temp = curr2.next
                curr2.next = curr 
                curr2  = temp
        return head
        
 

        
# @lc code=end

