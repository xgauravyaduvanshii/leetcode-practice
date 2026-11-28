# LeetCode 2762. Continuous Subarrays — Medium
# https://leetcode.com/problems/continuous-subarrays/
# Submission 2205245655 — Accepted, Python3
#
# My thinking: a subarray is continuous when its max minus
# its min is at most 2. Slide a window with two monotone
# deques tracking the current max and min; when the spread
# exceeds 2, move the left end forward until it fits again.
# Every right end contributes (right - left + 1) valid
# subarrays ending there.
from collections import deque


class Solution:
    def continuousSubarrays(self, nums: list[int]) -> int:
        maxq, minq = deque(), deque()
        ans = 0
        left = 0
        for right, v in enumerate(nums):
            while maxq and nums[maxq[-1]] <= v:
                maxq.pop()
            maxq.append(right)
            while minq and nums[minq[-1]] >= v:
                minq.pop()
            minq.append(right)
            while nums[maxq[0]] - nums[minq[0]] > 2:
                if maxq[0] == left:
                    maxq.popleft()
                if minq[0] == left:
                    minq.popleft()
                left += 1
            ans += right - left + 1
        return ans
