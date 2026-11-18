# LeetCode 670. Maximum Swap — Medium
# https://leetcode.com/problems/maximum-swap/
# Submission 2198906930 — Accepted, Python3
#
# My thinking: I scan the digits from the left and
# look for the biggest digit sitting anywhere to
# the right of each one. The first swap I can make
# — the leftmost digit with the largest digit
# after it — gives the biggest number.

class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        last = {int(d): i for i, d in enumerate(digits)}
        for i, d in enumerate(digits):
            for bigger in range(9, int(d), -1):
                if last.get(bigger, -1) > i:
                    j = last[bigger]
                    digits[i], digits[j] = digits[j], digits[i]
                    return int("".join(digits))
        return num
