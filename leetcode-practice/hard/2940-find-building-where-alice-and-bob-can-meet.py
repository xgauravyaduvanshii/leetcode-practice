# LeetCode 2940. Find Building Where Alice and Bob Can Meet — Hard
# https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/
# Submission 2200926930 — Accepted, Python3
#
# My thinking: for each query I need the leftmost building
# to the right of both people that is taller than both —
# so I keep the heights in a segment tree and walk down
# it to find that first taller building.

class Solution:
    def leftmostBuildingQueries(self, heights: list[int], queries: list[list[int]]) -> list[int]:
        n = len(heights)
        size = 1
        while size < n:
            size *= 2
        tree = [0] * (2 * size)
        for i, h in enumerate(heights):
            tree[size + i] = h
        for i in range(size - 1, 0, -1):
            tree[i] = max(tree[2 * i], tree[2 * i + 1])

        def first_greater(pos: int, h: int) -> int:
            def search(node: int, nl: int, nr: int) -> int:
                if nr <= pos + 1 or tree[node] <= h:
                    return -1
                if nl + 1 == nr:
                    return nl
                mid = (nl + nr) // 2
                left = search(2 * node, nl, mid)
                if left != -1:
                    return left
                return search(2 * node + 1, mid, nr)

            return search(1, 0, size)

        result = []
        for a, b in queries:
            if a == b:
                result.append(a)
                continue
            left, right = (a, b) if a < b else (b, a)
            if heights[left] < heights[right]:
                result.append(right)
                continue
            result.append(first_greater(right, max(heights[left], heights[right])))
        return result
