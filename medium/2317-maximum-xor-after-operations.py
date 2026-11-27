# LeetCode 2317. Maximum XOR After Operations — Medium
# https://leetcode.com/problems/maximum-xor-after-operations/
# Submission 2204682728 — Accepted, Python3
#
# My thinking: the allowed operation can clear a bit of one number, but
# it can never create a bit that no number has. So the best XOR value is
# simply the OR of all numbers — every bit that appears anywhere can be
# kept in the final XOR, and no other bit can.
class Solution:
    def maximumXOR(self, nums: list[int]) -> int:
        ans = 0
        for x in nums:
            ans |= x
        return ans
