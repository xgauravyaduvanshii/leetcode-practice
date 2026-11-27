# LeetCode 316. Remove Duplicate Letters — Medium
# https://leetcode.com/problems/remove-duplicate-letters/
# Submission 2198743855 — Accepted, Python3
#
# My thinking: I build the answer left to right,
# keeping it as small as possible. A bigger letter
# already on the stack gets popped when a smaller
# one arrives — but only if that bigger letter still
# appears later in the string, so nothing is lost.

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last = {char: i for i, char in enumerate(s)}
        stack = []
        in_stack = set()
        for i, char in enumerate(s):
            if char in in_stack:
                continue
            while stack and char < stack[-1] and last[stack[-1]] > i:
                in_stack.remove(stack.pop())
            stack.append(char)
            in_stack.add(char)
        return "".join(stack)
