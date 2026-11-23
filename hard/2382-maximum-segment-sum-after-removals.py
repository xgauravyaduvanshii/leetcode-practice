# LeetCode 2382. Maximum Segment Sum After Removals — Hard
# https://leetcode.com/problems/maximum-segment-sum-after-removals/
# Submission 2201707935 — Accepted, Python3
#
# My thinking: taking pieces away is hard
# to track, so I put them back in reverse
# — each return joins its neighbours into
# one segment, and the biggest segment I
# have seen before the return is the
# answer for that removal.

class Solution:
    def maximumSegmentSum(self, nums: list[int], removeQueries: list[int]) -> list[int]:
        n = len(nums)
        parent = list(range(n))
        seg = [0] * n
        active = [False] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return ra
            parent[rb] = ra
            seg[ra] += seg[rb]
            return ra

        ans = [0] * n
        best = 0
        for i in range(n - 1, -1, -1):
            ans[i] = best
            idx = removeQueries[i]
            active[idx] = True
            seg[idx] = nums[idx]
            if idx > 0 and active[idx - 1]:
                union(idx, idx - 1)
            if idx + 1 < n and active[idx + 1]:
                union(idx, idx + 1)
            best = max(best, seg[find(idx)])
        return ans
