#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        queue = []
        if len(s) %2 != 0:
            return False
        for char in s:
            if char == ")":
                if len(queue) == 0:
                    return False
                elif queue.pop() == "(":
                    continue
                else:
                    return False
            if char == "]":
                if len(queue) == 0:
                    return False
                elif queue.pop() == "[":
                    continue
                else:
                    return False
            if char == "}":
                if len(queue) == 0:
                    return False
                elif queue.pop() == "{":
                    continue
                else:
                    return False
            queue.append(char)
        if len(queue) == 0:
            return True
        else:
            return False

                    



        
# @lc code=end

