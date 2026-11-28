# LeetCode 2527. Find Xor-Beauty of Array — Medium
# https://leetcode.com/problems/find-xor-beauty-of-array/
# Submission 2205050331 — Accepted, Python3
#
# My thinking: expanding the definition, every element except the
# XOR of all of them cancels out in pairs. So the xor-beauty is
# simply the XOR of the whole array.
class Solution:
    def xorBeauty(self, nums: list[int]) -> int:
        ans = 0
        for x in nums:
            ans ^= x
        return ans
