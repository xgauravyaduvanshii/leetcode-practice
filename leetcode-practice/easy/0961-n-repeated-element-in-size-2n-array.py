# LeetCode 961. N-Repeated Element in Size 2N Array — Easy
# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/
# Submission 2197546161 — Accepted, Python3
#
# My thinking: one element appears N times in an
# array of 2N, so it has to show up again very
# quickly — the first number I see twice is the
# answer.

class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        return nums[0]
