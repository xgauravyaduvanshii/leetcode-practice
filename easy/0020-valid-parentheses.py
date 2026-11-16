# LeetCode 20. Valid Parentheses — Easy
# https://leetcode.com/problems/valid-parentheses/
# Submission 2197268513 — Accepted, Python3
#
# My thinking: opening brackets go on a stack. When I see
# a closing bracket, the top of the stack has to be its
# matching opener — if not, the string is wrong. At the
# end the stack has to be empty, otherwise some bracket
# was never closed.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching_opener = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in matching_opener:
                # a closing bracket — check the last opener
                if not stack or stack[-1] != matching_opener[char]:
                    return False
                stack.pop()
            else:
                # an opening bracket — remember it
                stack.append(char)

        # valid only if every opener got closed
        return len(stack) == 0
