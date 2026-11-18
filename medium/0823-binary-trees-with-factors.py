# LeetCode 823. Binary Trees With Factors — Medium
# https://leetcode.com/problems/binary-trees-with-factors/
# Submission 2198948163 — Accepted, Python3
#
# My thinking: each value can be a single node,
# or a root whose children multiply to it. I go
# through the values smallest first, so when I
# reach a value its factors' counts are already
# known.

from typing import List


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        mod = 10 ** 9 + 7
        arr.sort()
        counts = {num: 1 for num in arr}
        for i, num in enumerate(arr):
            for j in range(i):
                if num % arr[j] == 0 and num // arr[j] in counts:
                    counts[num] = (counts[num] + counts[arr[j]] * counts[num // arr[j]]) % mod
        return sum(counts.values()) % mod
