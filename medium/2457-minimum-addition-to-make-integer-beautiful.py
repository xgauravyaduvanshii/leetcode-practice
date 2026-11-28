# LeetCode 2457. Minimum Addition to Make Integer Beautiful — Medium
# https://leetcode.com/problems/minimum-addition-to-make-integer-beautiful/
# Submission 2204954022 — Accepted, Python3
#
# My thinking: while the digit sum is over the target, round the
# number up to the next multiple of 10, then 100, then 1000, and so
# on — each rounding zeroes a low digit and adds the smallest amount
# that can fix the sum at that place. The first rounding that brings
# the digit sum down to the target is the minimum addition.
class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        def digit_sum(x: int) -> int:
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s

        x = 0
        p = 1
        while digit_sum(n + x) > target:
            cur = n + x
            add = (10 * p - cur % (10 * p)) % (10 * p)
            x += add
            p *= 10
        return x
