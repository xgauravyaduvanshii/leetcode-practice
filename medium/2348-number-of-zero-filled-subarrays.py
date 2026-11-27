# LeetCode 2348. Number of Zero-Filled Subarrays — Medium
# https://leetcode.com/problems/number-of-zero-filled-subarrays/
# Submission 2204725765 — Accepted, Python3
#
# My thinking: a run of L consecutive zeros contains L*(L+1)/2 zero-filled
# subarrays, but I do not need the formula — I just grow the current run
# and add its length to the answer at each zero, since a run of length L
# ends exactly L new subarrays. A non-zero resets the run.
class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        ans = 0
        run = 0
        for x in nums:
            if x == 0:
                run += 1
                ans += run
            else:
                run = 0
        return ans
