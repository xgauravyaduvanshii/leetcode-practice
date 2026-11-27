# LeetCode 3547. Maximum Sum of Edge Values in a Graph — Hard
# https://leetcode.com/problems/maximum-sum-of-edge-values-in-a-graph/
# Submission 2202832593 — Accepted, Python3
from typing import List


class Solution:
    def maxScore(self, n: int, edges: List[List[int]]) -> int:
        # My thinking: every node has degree at most 2 and the graph
        # is connected, so it is a path (n - 1 edges) or a cycle
        # (n edges). A big number earns most when it sits next to
        # other big numbers, so I lay the values out as the odds
        # increasing and then the evens decreasing — the largest
        # values end up side by side in the middle. For a cycle I
        # add the wrap-around edge between the two ends.
        odds = [x for x in range(1, n + 1) if x % 2 == 1]
        evens = [x for x in range(1, n + 1) if x % 2 == 0]
        arr = odds + evens[::-1]
        total = 0
        for i in range(n - 1):
            total += arr[i] * arr[i + 1]
        if len(edges) == n:
            total += arr[-1] * arr[0]
        return total
