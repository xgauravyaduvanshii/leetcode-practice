# LeetCode 1047. Remove All Adjacent Duplicates In String — Easy
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
# Submission 2197554427 — Accepted, Python3
#
# My thinking: I build the answer one letter at a
# time on a stack. If the new letter matches the
# top of the stack, the two cancel out and I pop
# it — that can expose a new pair underneath. If
# it does not match, I push it on. What is left in
# the stack is the answer.

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for ch in s:
            if stack and stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)
