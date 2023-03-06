#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = []

        if not bool(root):
            return root
        curr = root 
        if curr.left : queue.append(root.left)
        if curr.right: queue.append(root.right)
        curr.left, curr.right = curr.right, curr.left 
        while bool(queue):
            curr = queue.pop(0)
            if curr.left : queue.append(curr.left)
            if curr.right: queue.append(curr.right)
            curr.left, curr.right = curr.right, curr.left 
        return root 




        
# @lc code=end

