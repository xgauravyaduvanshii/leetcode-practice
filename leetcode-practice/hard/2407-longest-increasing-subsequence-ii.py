# LeetCode 2407. Longest Increasing Subsequence II — Hard
# https://leetcode.com/problems/longest-increasing-subsequence-ii/
# Submission 2201722078 — Accepted, Python3
#
# My thinking: each number extends the
# best run ending just below it — I keep
# those best runs in a segment tree and
# ask it for the best run in the window
# [value - k, value - 1] before I extend.

class Solution:
    def lengthOfLIS(self, nums: list[int], k: int) -> int:
        size = 1
        while size < max(nums) + 2:
            size *= 2
        tree = [0] * (2 * size)

        def query(lo, hi):
            lo += size
            hi += size
            best = 0
            while lo <= hi:
                if lo % 2 == 1:
                    best = max(best, tree[lo])
                    lo += 1
                if hi % 2 == 0:
                    best = max(best, tree[hi])
                    hi -= 1
                lo //= 2
                hi //= 2
            return best

        def update(pos, val):
            pos += size
            tree[pos] = max(tree[pos], val)
            pos //= 2
            while pos:
                tree[pos] = max(tree[2 * pos], tree[2 * pos + 1])
                pos //= 2

        ans = 0
        for x in nums:
            lo = max(1, x - k)
            best = query(lo, x - 1)
            length = best + 1
            ans = max(ans, length)
            update(x, length)
        return ans
