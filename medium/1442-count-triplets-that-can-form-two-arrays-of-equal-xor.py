# LeetCode 1442. Count Triplets That Can Form Two Arrays of Equal XOR — Medium
# https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/
# Submission 2199852520 — Accepted, Python3
#
# My thinking: with prefix xors, two slices
# have equal xor exactly when the prefix before
# the first equals the prefix after the second.
# For each such pair, every middle split in
# between works, so I add the distance.

from typing import List


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] ^ arr[i]
        total = 0
        for i in range(n):
            for k in range(i + 1, n):
                if pref[i] == pref[k + 1]:
                    total += k - i
        return total
