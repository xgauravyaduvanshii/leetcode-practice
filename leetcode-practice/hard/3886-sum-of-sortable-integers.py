# LeetCode 3886. Sum of Sortable Integers — Hard
# https://leetcode.com/problems/sum-of-sortable-integers/
# Submission 2203345240 — Accepted, Python3
import random
from typing import List


class Solution:
    def sortableIntegers(self, nums: List[int]) -> int:
        # My thinking: sort the whole array once to get S. For
        # a divisor k, each block of length k must rotate into
        # the matching slice of S. A block rotates into sorted
        # order exactly when it has at most one cyclic descent:
        # count descents with a prefix sum, so each block costs
        # O(1), and when there is exactly one descent the wrap
        # from the last element back to the first must not
        # descend either. The block must also hold the same
        # multiset as its slice of S, checked with two prefix
        # sums of per-value random 64-bit hashes, again O(1)
        # per block. A block passing both tests rotates into
        # its sorted slice, and every divisor whose blocks all
        # pass adds k to the answer.
        n = len(nums)
        S = sorted(nums)
        desc = [0] * n
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                desc[i] = 1
        prefD = [0] * (n + 1)
        for i in range(n):
            prefD[i + 1] = prefD[i] + desc[i]
        rng = random.Random(1234567)
        r1 = {}
        r2 = {}
        for v in set(nums):
            r1[v] = rng.getrandbits(64)
            r2[v] = rng.getrandbits(64)

        def phash(arr, r):
            p = [0] * (n + 1)
            for i, x in enumerate(arr):
                p[i + 1] = p[i] + r[x]
            return p

        PN1, PS1 = phash(nums, r1), phash(S, r1)
        PN2, PS2 = phash(nums, r2), phash(S, r2)
        ans = 0
        for k in range(1, n + 1):
            if n % k:
                continue
            ok = True
            for b in range(0, n, k):
                d = prefD[b + k - 1] - prefD[b]
                if d > 1:
                    ok = False
                    break
                if d == 1 and nums[b + k - 1] > nums[b]:
                    ok = False
                    break
                if (PN1[b + k] - PN1[b] != PS1[b + k] - PS1[b]
                        or PN2[b + k] - PN2[b] != PS2[b + k] - PS2[b]):
                    ok = False
                    break
            if ok:
                ans += k
        return ans
