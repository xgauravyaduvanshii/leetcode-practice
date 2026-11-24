# LeetCode 3486. Longest Special Path II — Hard
# https://leetcode.com/problems/longest-special-path-ii/
# Submission 2202701903 — Accepted, Python3

from collections import defaultdict
from typing import List


class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        # My thinking: a special path is a downward path, so it is
        # a suffix of the root-to-current path. For the current
        # node I want the leftmost start that keeps the window
        # valid: no value three times, and at most one value twice.
        # For each value I keep its occurrence depths on the path.
        # Let b be the deepest third-from-last occurrence over all
        # values (the start must sit past it, or some value would
        # appear three times), and let a2 be the second largest
        # second-from-last occurrence (the start must sit past all
        # but the largest one, or two values would appear twice).
        # The window starts at max(b, a2) + 1. Both numbers only
        # ever grow while I walk down, so I save and restore them
        # (and the top-two second-from-last list) on the DFS stack
        # instead of maintaining a heap.
        n = len(nums)
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        occ = defaultdict(list)
        best_b = -1
        top = []
        best_len = 0
        best_nodes = 0
        path = []
        path_dist = []
        # (node, parent, dist, is_exit, saved_best_b, saved_top)
        stack = [(0, -1, 0, False, -1, None)]
        while stack:
            node, par, d, is_exit, saved_b, saved_top = stack.pop()
            if not is_exit:
                v = nums[node]
                saved_b = best_b
                saved_top = list(top)
                depth = len(path)
                occ[v].append(depth)
                lst = occ[v]
                if len(lst) >= 3 and lst[-3] > best_b:
                    best_b = lst[-3]
                if len(lst) >= 2:
                    na = lst[-2]
                    top = [(a, vv) for (a, vv) in top if vv != v]
                    top.append((na, v))
                    top.sort(reverse=True)
                    top = top[:2]
                path.append(node)
                path_dist.append(d)
                l2 = top[1][0] if len(top) >= 2 else -1
                l = max(best_b, l2) + 1
                length = d - path_dist[l]
                nodes_cnt = depth - l + 1
                if length > best_len or (length == best_len and nodes_cnt < best_nodes):
                    best_len, best_nodes = length, nodes_cnt
                stack.append((node, par, d, True, saved_b, saved_top))
                for nb, w in adj[node]:
                    if nb == par:
                        continue
                    stack.append((nb, node, d + w, False, -1, None))
            else:
                best_b = saved_b
                top = saved_top
                occ[nums[node]].pop()
                path.pop()
                path_dist.pop()
        return [best_len, best_nodes]
