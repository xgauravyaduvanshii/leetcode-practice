# LeetCode 393. UTF-8 Validation — Medium
# https://leetcode.com/problems/utf-8-validation/
# Submission 2198772807 — Accepted, Python3
#
# My thinking: a byte starting with 0 is a lone
# character, and a leading byte's pattern says how
# many continuation bytes must follow — each one has
# to start with 10. I count the expected
# continuations down and fail on any mismatch.

from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        remaining = 0
        for byte in data:
            if remaining == 0:
                if byte >> 5 == 0b110:
                    remaining = 1
                elif byte >> 4 == 0b1110:
                    remaining = 2
                elif byte >> 3 == 0b11110:
                    remaining = 3
                elif byte >> 7:
                    return False
            else:
                if byte >> 6 != 0b10:
                    return False
                remaining -= 1
        return remaining == 0
