# LeetCode 1782. Count Pairs Of Nodes — Hard
# https://leetcode.com/problems/count-pairs-of-nodes/
# Submission 2201161211 — Accepted, Python3
#
# My thinking: I sort the degrees and count pairs
# whose degrees add up past the query with two
# pointers, then I take back the pairs joined by an
# edge, where the shared edge was counted twice.

from collections import Counter

class Solution:
    def countPairs(self, n: int, edges: list[list[int]], queries: list[int]) -> list[int]:
        deg = [0] * (n + 1)
        shared = Counter()
        for u, v in edges:
            deg[u] += 1
            deg[v] += 1
            shared[(min(u, v), max(u, v))] += 1
        degs = sorted(deg[1:])
        ans = []
        for q in queries:
            cnt = 0
            left, right = 0, n - 1
            while left < right:
                if degs[left] + degs[right] > q:
                    cnt += right - left
                    right -= 1
                else:
                    left += 1
            for (u, v), c in shared.items():
                if deg[u] + deg[v] > q and deg[u] + deg[v] - c <= q:
                    cnt -= 1
            ans.append(cnt)
        return ans
