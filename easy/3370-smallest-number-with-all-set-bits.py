# 3370. Smallest Number With All Set Bits (Easy)
# https://leetcode.com/problems/smallest-number-with-all-set-bits/
# Submission 2200008441 — Accepted, Python3
class Solution:
    def smallestNumber(self, n: int) -> int:
        # My thinking: the answer has all its bits set,
        # so it looks like 1, 3, 7, 15, and so on — one
        # less than a power of two. I take the smallest
        # of those that is at least n.
        x = 1
        while x < n:
            x = x * 2 + 1
        return x
