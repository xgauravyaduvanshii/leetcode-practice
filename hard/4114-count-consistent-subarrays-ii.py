# LeetCode 4114. Count Consistent Subarrays II — Hard
# https://leetcode.com/problems/count-consistent-subarrays-ii/
# Submission 2203740298 — Accepted, Python3


class Solution:
    def countConsistent(self, nums: list[int]) -> int:
        # My thinking: a subarray is consistent when its
        # bitwise AND equals its minimum. The AND of a
        # subarray is always <= every element, so it is
        # <= the minimum, and equality holds exactly when
        # the AND value itself occurs in the subarray.
        # For each right endpoint r, keep the distinct
        # ANDs of all subarrays ending at r (at most ~20
        # of them, since each AND step can only clear
        # bits) together with how many starts give each
        # AND. A subarray ending at r with AND x is
        # consistent exactly when its start is at or
        # before the most recent occurrence of x, so for
        # each AND group we count the starts in its
        # range that lie at or before that last
        # occurrence. Summing over all r counts every
        # consistent subarray once.
        ans = 0
        cur = []
        last = {}
        for r, v in enumerate(nums):
            nxt = [[v, 1]]
            for a, c in cur:
                na = a & v
                if na == nxt[-1][0]:
                    nxt[-1][1] += c
                else:
                    nxt.append([na, c])
            cur = nxt
            last[v] = r
            end = r
            for a, c in cur:
                s = end - c + 1
                lp = last.get(a, -1)
                if lp >= s:
                    ans += min(end, lp) - s + 1
                end = s - 1
        return ans
