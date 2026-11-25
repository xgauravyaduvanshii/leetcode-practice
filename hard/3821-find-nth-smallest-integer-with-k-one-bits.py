# LeetCode 3821. Find Nth Smallest Integer With K One Bits — Hard
# https://leetcode.com/problems/find-nth-smallest-integer-with-k-one-bits/
# Submission 2203195855 — Accepted, Python3
from math import comb


class Solution:
    def nthSmallest(self, n: int, k: int) -> int:
        # My thinking: decide the answer bit by bit from the
        # top (bit 49) down. With i lower bits still free and
        # k ones left to place, setting the current bit to 0
        # leaves exactly C(i, k) numbers; if n is larger than
        # that, the nth number must have this bit set, so I
        # set it, subtract C(i, k) from n and use up one of
        # the k ones. Otherwise the bit stays 0. Once all k
        # ones are placed the remaining bits are 0, and the
        # guarantee that the answer is below 2^50 means 50
        # bits are always enough.
        ans = 0
        for i in range(49, -1, -1):
            if k == 0:
                break
            if n > comb(i, k):
                n -= comb(i, k)
                ans |= 1 << i
                k -= 1
        return ans
