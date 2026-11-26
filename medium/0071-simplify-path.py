# LeetCode 71. Simplify Path — Medium
# https://leetcode.com/problems/simplify-path/
# Submission 2203842397 — Accepted, Python3
#
# My thinking: I split the path on slashes and walk the parts with a
# stack. A normal name goes on the stack, ".." pops the last directory
# if there is one, and "." and empty parts are ignored. Joining the
# stack with slashes and putting one slash in front gives the clean
# canonical path.

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for part in path.split('/'):
            if part == '' or part == '.':
                continue
            if part == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        return '/' + '/'.join(stack)
