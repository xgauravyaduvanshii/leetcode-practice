# LeetCode 868. Binary Gap — Easy
# https://leetcode.com/problems/binary-gap/
# Submission 2197536777 — Accepted, Python3
#
# My thinking: I read the number bit by bit from the
# right, keeping track of where the last 1 was.
# Every time I meet another 1, the gap is the
# distance between the two positions — and I keep
# the biggest gap I have seen.

class Solution:
    def binaryGap(self, n: int) -> int:
        best = 0
        last = -1
        pos = 0
        while n > 0:
            if n & 1:
                if last != -1:
                    best = max(best, pos - last)
                last = pos
            n >>= 1
            pos += 1
        return best
