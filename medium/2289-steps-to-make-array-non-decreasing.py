# LeetCode 2289. Steps to Make Array Non-decreasing — Medium
# https://leetcode.com/problems/steps-to-make-array-non-decreasing/
# Submission 2204647421 — Accepted, Python3
#
# My thinking: scan left to right with a stack of (value, steps) pairs
# for the elements still standing. For each new x, pop every stack top
# that is <= x — those elements are removed by x's arrival — and x needs
# one more step than the worst of them. If the stack is empty nothing
# blocks x, so it takes 0 steps. The answer is the most steps any
# element needs.
class Solution:
    def totalSteps(self, nums: list[int]) -> int:
        stack = []
        ans = 0
        for x in nums:
            cur = 1
            while stack and stack[-1][0] <= x:
                cur = max(cur, stack[-1][1] + 1)
                stack.pop()
            if not stack:
                cur = 0
            ans = max(ans, cur)
            stack.append((x, cur))
        return ans
