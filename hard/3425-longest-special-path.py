# LeetCode 3425. Longest Special Path — Hard
# https://leetcode.com/problems/longest-special-path/
# Submission 2202522237 — Accepted 675/675, Python3
from typing import List


class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        # My thinking: on a root-to-leaf walk I keep the depth of
        # the last sighting of every value, so the earliest start
        # of a special path ending at the current node is just
        # past the deepest repeated value on that walk. The
        # length is the prefix-distance difference to that start,
        # and the node count is the depth difference — I keep the
        # longest length, breaking ties by the fewest nodes.
        # An iterative walk avoids recursion limits on deep trees.
        n = len(nums)
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        best_len = 0
        best_nodes = 1
        last = {}
        dist_at_depth = []

        def enter(u, depth, dist, limit):
            nonlocal best_len, best_nodes
            dist_at_depth.append(dist)
            old = last.get(nums[u])
            last[nums[u]] = depth
            length = dist - dist_at_depth[limit + 1]
            nodes = depth - limit
            if length > best_len or (length == best_len and nodes < best_nodes):
                best_len, best_nodes = length, nodes
            return old

        stack = [[0, -1, 0, 0, -1, 0, enter(0, 0, 0, -1)]]
        while stack:
            frame = stack[-1]
            u, parent, depth, dist, limit, ci, old = frame
            if ci < len(graph[u]):
                v, w = graph[u][ci]
                frame[5] += 1
                if v == parent:
                    continue
                nlimit = max(limit, last.get(nums[v], -1))
                stack.append([v, u, depth + 1, dist + w, nlimit, 0,
                              enter(v, depth + 1, dist + w, nlimit)])
            else:
                stack.pop()
                dist_at_depth.pop()
                if old is None:
                    del last[nums[u]]
                else:
                    last[nums[u]] = old
        return [best_len, best_nodes]
