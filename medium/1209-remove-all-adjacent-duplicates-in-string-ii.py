# LeetCode 1209. Remove All Adjacent Duplicates in String II — Medium
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
# Submission 2199012703 — Accepted, Python3
#
# My thinking: I keep a stack of letter runs.
# Each new letter joins its run, and the run
# vanishes the moment it reaches k — which can
# merge the runs on either side of it.

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for ch in s:
            if stack and stack[-1][0] == ch:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([ch, 1])
        return "".join(ch * count for ch, count in stack)
