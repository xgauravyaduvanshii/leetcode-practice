# LeetCode 1702. Maximum Binary String After Change — Medium
# https://leetcode.com/problems/maximum-binary-string-after-change/
# Submission 2199915115 — Accepted, Python3
#
# My thinking: only the part from the first
# zero onward can change, and it can hold at
# most one zero. I put that single zero as
# far right as the zero count allows and fill
# the rest with ones.

class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        first_zero = binary.find("0")
        if first_zero == -1:
            return binary
        zeros = binary.count("0", first_zero)
        return "1" * (first_zero + zeros - 1) + "0" + "1" * (len(binary) - first_zero - zeros)
