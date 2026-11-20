# 3285. Find Indices of Stable Mountains (Easy)
# https://leetcode.com/problems/find-indices-of-stable-mountains/
# Submission 2200001540 — Accepted, Python3
from typing import List


class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        # My thinking: a mountain is stable when the one
        # before it rises above the threshold. I check
        # every mountain after the first and keep the
        # ones whose neighbour is tall enough.
        return [i for i in range(1, len(height)) if height[i - 1] > threshold]
