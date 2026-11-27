# LeetCode 3630. Partition Array for Maximum XOR and AND — Hard
# https://leetcode.com/problems/partition-array-for-maximum-xor-and-and/
# Submission 2202890818 — Accepted, Python3
from typing import List


class Solution:
    def maximizeXorAndXor(self, nums: List[int]) -> int:
        # My thinking: I fix the AND part B and split the rest S
        # between A and C. With X the xor of all of S, the best
        # split scores X plus twice the most I can pull out of the
        # bits where X is zero, and that best comes from a linear
        # basis of S: scanning bits from high to low, I take a
        # basis vector whenever it turns on a zero-bit of X. I try
        # every choice of B (at most 2^19 of them) and keep the
        # best total.
        n = len(nums)
        best = 0
        for maskB in range(1 << n):
            and_b = None
            xor_s = 0
            s_elems = []
            for i in range(n):
                if (maskB >> i) & 1:
                    and_b = nums[i] if and_b is None else (and_b & nums[i])
                else:
                    xor_s ^= nums[i]
                    s_elems.append(nums[i])
            if and_b is None:
                and_b = 0
            basis = [0] * 30
            for v in s_elems:
                x = v
                for b in range(29, -1, -1):
                    if (x >> b) & 1 == 0:
                        continue
                    if basis[b] == 0:
                        basis[b] = x
                        break
                    x ^= basis[b]
            a = 0
            for b in range(29, -1, -1):
                if ((xor_s >> b) & 1) == 0 and ((a >> b) & 1) == 0 and basis[b] != 0:
                    a ^= basis[b]
            xor_sum = xor_s + 2 * (a & ~xor_s)
            best = max(best, and_b + xor_sum)
        return best
