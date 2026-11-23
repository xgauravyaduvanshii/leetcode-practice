# LeetCode 2569. Handling Sum Queries After Update — Hard
# https://leetcode.com/problems/handling-sum-queries-after-update/
# Submission 2201823328 — Accepted, Python3
#
# My thinking: the second array only
# ever grows by the number of ones times
# p, so I keep its running total beside
# me and spend my effort on the first
# array — a lazy segment tree that flips
# whole ranges and always knows how many
# ones are standing.

class Solution:
    def handleQuery(self, nums1: list[int], nums2: list[int], queries: list[list[int]]) -> list[int]:
        n = len(nums1)
        size = 1
        while size < n:
            size *= 2
        tree = [0] * (2 * size)
        lazy = [False] * (2 * size)
        for i, v in enumerate(nums1):
            tree[size + i] = v
        for i in range(size - 1, 0, -1):
            tree[i] = tree[2 * i] + tree[2 * i + 1]

        def apply(node, length):
            tree[node] = length - tree[node]
            lazy[node] = not lazy[node]

        def push(node, length):
            if lazy[node] and length > 1:
                half = length // 2
                apply(2 * node, half)
                apply(2 * node + 1, half)
                lazy[node] = False

        def flip(node, nl, nr, l, r):
            if r < nl or nr < l:
                return
            if l <= nl and nr <= r:
                apply(node, nr - nl + 1)
                return
            push(node, nr - nl + 1)
            mid = (nl + nr) // 2
            flip(2 * node, nl, mid, l, r)
            flip(2 * node + 1, mid + 1, nr, l, r)
            tree[node] = tree[2 * node] + tree[2 * node + 1]

        total2 = sum(nums2)
        ans = []
        for q in queries:
            if q[0] == 1:
                flip(1, 0, size - 1, q[1], q[2])
            elif q[0] == 2:
                total2 += tree[1] * q[1]
            else:
                ans.append(total2)
        return ans
