# LeetCode 1018. Binary Prefix Divisible By 5 — Easy
# https://leetcode.com/problems/binary-prefix-divisible-by-5/
# Submission 2197551206 — Accepted, Python3
#
# My thinking: I build the binary number one bit at
# a time — each new bit doubles the value so far
# and adds the bit. I only need the remainder when
# divided by 5, so I keep just that and check
# whether it is zero after each bit.

class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        result = []
        current = 0
        for num in nums:
            current = (current * 2 + num) % 5
            result.append(current == 0)
        return result
