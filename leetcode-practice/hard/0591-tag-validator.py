# LeetCode 591. Tag Validator — Hard
# https://leetcode.com/problems/tag-validator/
# Submission 2198664480 — Accepted, Python3
#
# My thinking: I scan the code left to right with a
# stack of open tags. A CDATA block is only allowed
# inside a tag and runs to the next ]]>. An opening
# tag must be one to nine capital letters, a closing
# tag must match the top of the stack, and once the
# root tag closes nothing else may follow.

class Solution:
    def isValid(self, code: str) -> bool:
        stack = []
        i = 0
        n = len(code)
        while i < n:
            if i > 0 and not stack:
                return False
            if code.startswith("<![CDATA[", i):
                if not stack:
                    return False
                end = code.find("]]>", i + 9)
                if end == -1:
                    return False
                i = end + 3
            elif code.startswith("</", i):
                end = code.find(">", i + 2)
                if end == -1 or end == i + 2:
                    return False
                name = code[i + 2:end]
                if not stack or stack[-1] != name:
                    return False
                stack.pop()
                i = end + 1
            elif code.startswith("<", i):
                end = code.find(">", i + 1)
                if end == -1 or end == i + 1 or end - i - 1 > 9:
                    return False
                name = code[i + 1:end]
                if not all("A" <= c <= "Z" for c in name):
                    return False
                stack.append(name)
                i = end + 1
            else:
                i += 1
        return not stack
