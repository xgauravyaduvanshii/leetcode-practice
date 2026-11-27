# LeetCode 2121. Intervals Between Identical Elements — Medium
# https://leetcode.com/problems/intervals-between-identical-elements/
# Submission 2204407103 — Accepted, Python3
#
# My thinking: I group the positions of each value. Inside one group,
# the total distance for a position is the sum of distances to the
# positions on its left plus the distances to those on its right.
# With a running prefix sum I compute both sides in one pass: the left
# part is position * count-so-far - prefix, the right part comes from
# the group total minus what was already counted.
class Solution:
    def getDistances(self, arr: list[int]) -> list[int]:
        from collections import defaultdict
        pos = defaultdict(list)
        for i, v in enumerate(arr):
            pos[v].append(i)
        ans = [0] * len(arr)
        for idxs in pos.values():
            total = sum(idxs)
            prefix = 0
            m = len(idxs)
            for j, p in enumerate(idxs):
                left = p * j - prefix
                right = (total - prefix - p) - p * (m - 1 - j)
                ans[p] = left + right
                prefix += p
        return ans
