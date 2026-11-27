# LeetCode 2683. Neighboring Bitwise XOR — Medium
# https://leetcode.com/problems/neighboring-bitwise-xor/
# Submission 2197818112 — Accepted, Python3
#
# My thinking: xoring all the derived values cancels
# out every original element twice — except the
# wrap-around, which leaves the xor of the whole
# array. A valid original array exists exactly when
# that xor is 0.

from typing import List


class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        x = 0
        for v in derived:
            x ^= v
        return x == 0
