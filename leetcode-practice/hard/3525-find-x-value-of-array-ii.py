# LeetCode 3525. Find X Value of Array II — Hard
# https://leetcode.com/problems/find-x-value-of-array-ii/
# Submission 2202801059 — Accepted, Python3
from typing import List


class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        # My thinking: for one query the answer is how many prefixes
        # of nums[start:] have product equal to x mod k. A segment
        # tree node stores exactly what is needed to answer that for
        # any segment: its total product, and how many of its prefixes
        # have each product mod k. Merging two neighbours is cheap:
        # the right half's prefixes all get multiplied by the left
        # half's total product, so its counts shift into new residue
        # buckets. A query is then one suffix-range merge, and a point
        # update rebuilds O(log n) nodes.
        n = len(nums)
        size = 1
        while size < n:
            size *= 2
        prod = [1] * (2 * size)
        dist = [[0] * k for _ in range(2 * size)]
        for i, v in enumerate(nums):
            prod[size + i] = v % k
            dist[size + i][v % k] = 1

        def combine(pi, di, pj, dj):
            p = (pi * pj) % k
            d = di[:]
            for q in range(k):
                if dj[q]:
                    d[(pi * q) % k] += dj[q]
            return p, d

        for i in range(size - 1, 0, -1):
            prod[i], dist[i] = combine(prod[2 * i], dist[2 * i], prod[2 * i + 1], dist[2 * i + 1])
        ans = []
        for idx, value, start, x in queries:
            i = size + idx
            prod[i] = value % k
            dist[i] = [0] * k
            dist[i][value % k] = 1
            i //= 2
            while i >= 1:
                prod[i], dist[i] = combine(prod[2 * i], dist[2 * i], prod[2 * i + 1], dist[2 * i + 1])
                i //= 2
            l = size + start
            r = size + n
            lp, ld = 1, [0] * k
            rp, rd = 1, [0] * k
            while l < r:
                if l & 1:
                    lp, ld = combine(lp, ld, prod[l], dist[l])
                    l += 1
                if r & 1:
                    r -= 1
                    rp, rd = combine(prod[r], dist[r], rp, rd)
                l //= 2
                r //= 2
            _, fd = combine(lp, ld, rp, rd)
            ans.append(fd[x])
        return ans
