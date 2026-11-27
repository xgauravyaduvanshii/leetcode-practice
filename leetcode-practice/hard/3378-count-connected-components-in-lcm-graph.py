# LeetCode 3378. Count Connected Components in LCM Graph — Hard
# https://leetcode.com/problems/count-connected-components-in-lcm-graph/
# Submission 2202491203 — Accepted 697/697, Python3
from typing import List


class Solution:
    def countComponents(self, nums: List[int], threshold: int) -> int:
        # My thinking: two numbers are joined exactly when they share a
        # common multiple no bigger than threshold, because then their lcm
        # divides that multiple and is at most threshold, and conversely
        # their lcm itself is such a multiple. So for every multiple m up
        # to threshold I union each number with the first divisor of m I
        # have seen. Numbers above threshold have no multiple in range and
        # stay alone.
        n = len(nums)
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb

        index = {}
        for i, x in enumerate(nums):
            if x <= threshold:
                index[x] = i
        first = [None] * (threshold + 1)
        for x, i in index.items():
            for m in range(x, threshold + 1, x):
                j = first[m]
                if j is None:
                    first[m] = i
                else:
                    union(i, j)
        alone = sum(1 for x in nums if x > threshold)
        roots = {find(i) for i, x in enumerate(nums) if x <= threshold}
        return alone + len(roots)
