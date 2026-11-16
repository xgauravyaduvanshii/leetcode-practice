# LeetCode 1646. Get Maximum in Generated Array — Easy
# https://leetcode.com/problems/get-maximum-in-generated-array/
# Submission 2197591720 — Accepted, Python3
#
# My thinking: I build the array by the given rules
# — even indexes copy the value at half the index,
# odd indexes add two neighbours — and return the
# biggest value in it. n = 0 is a special case
# with just [0].

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        nums = [0] * (n + 1)
        nums[1] = 1
        for i in range(2, n + 1):
            if i % 2 == 0:
                nums[i] = nums[i // 2]
            else:
                nums[i] = nums[i // 2] + nums[i // 2 + 1]
        return max(nums)
