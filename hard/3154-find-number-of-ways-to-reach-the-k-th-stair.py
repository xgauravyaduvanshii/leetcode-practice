# LeetCode 3154. Find Number of Ways to Reach the K-th Stair — Hard
# https://leetcode.com/problems/find-number-of-ways-to-reach-the-k-th-stair/
# Submission 2202043230 — Accepted, Python3
#
# My thinking: to reach stair k I must
# jump to some 2^x >= k, then step down
# y = 2^x - k times. The jumps and steps
# can interleave in C(x + 1, y) ways, and
# only finitely many x work — once y
# exceeds x + 1 there are no more. I sum
# the combinations over all valid x.

import math


class Solution:
    def waysToReachStair(self, k: int) -> int:
        ans = 0
        x = 0
        while True:
            y = (1 << x) - k
            if y < 0:
                x += 1
                continue
            if y > x + 1:
                break
            ans += math.comb(x + 1, y)
            x += 1
        return ans
