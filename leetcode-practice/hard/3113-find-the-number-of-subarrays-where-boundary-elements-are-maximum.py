# LeetCode 3113. Find the Number of Subarrays Where Boundary Elements Are Maximum — Hard
# https://leetcode.com/problems/find-the-number-of-subarrays-where-boundary-elements-are-maximum/
# Submission 2202001098 — Accepted, Python3
#
# My thinking: I sweep the numbers with
# a decreasing stack that remembers, for
# each distinct value, how many equal
# values in a row sit on top. A new
# number pops everything smaller, then
# either extends the run of equals —
# every subarray ending here whose
# boundary is that value counts — or
# starts a new run with just itself.

from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        stack = []
        ans = 0
        for x in nums:
            while stack and stack[-1][0] < x:
                stack.pop()
            if stack and stack[-1][0] == x:
                ans += stack[-1][1] + 1
                stack[-1][1] += 1
            else:
                ans += 1
                stack.append([x, 1])
        return ans
