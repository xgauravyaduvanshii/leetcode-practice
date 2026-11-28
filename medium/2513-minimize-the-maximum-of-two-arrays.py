# LeetCode 2513. Minimize the Maximum of Two Arrays — Medium
# https://leetcode.com/problems/minimize-the-maximum-of-two-arrays/
# Submission 2204979346 — Accepted, Python3
#
# My thinking: binary-search the answer x. In the first x numbers,
# those not divisible by divisor1 can go to array 1, those not
# divisible by divisor2 can go to array 2, and those divisible by
# neither can go to either. x works when all three counts cover
# what each array needs.
import math


class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        l = math.lcm(divisor1, divisor2)

        def feasible(x: int) -> bool:
            a = x - x // divisor1
            b = x - x // divisor2
            c = x - x // divisor1 - x // divisor2 + x // l
            return a >= uniqueCnt1 and b >= uniqueCnt2 and a + b - c >= uniqueCnt1 + uniqueCnt2

        lo, hi = 1, 2 * (uniqueCnt1 + uniqueCnt2)
        while lo < hi:
            mid = (lo + hi) // 2
            if feasible(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
