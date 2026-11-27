# LeetCode 4051. Count Subarrays with Distant Sums — Hard
# https://leetcode.com/problems/count-subarrays-with-distant-sums/
# Submission 2203572937 — Accepted, Python3
from bisect import bisect_left, bisect_right


class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, delta):
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s


class Solution:
    def distantSubarrays(self, nums: list[int], goal: int, k: int) -> int:
        # My thinking: write the subarray sum as a difference
        # of prefix sums, sum(nums[i..j]) = pref[j+1] - pref[i].
        # A subarray is distant when its sum is at least k away
        # from goal, so for each right end j the earlier prefix
        # pref[i] must satisfy pref[i] <= pref[j+1] - goal - k
        # or pref[i] >= pref[j+1] - goal + k. Counting how many
        # earlier prefixes fall in those two ranges is a job
        # for a Fenwick tree over the coordinate-compressed
        # prefix sums, since the prefixes are not sorted and
        # can be as large as 1e14. Insert pref[0] first, then
        # for each j query both ranges and insert pref[j+1].
        # When k is 0 every subarray is distant, since an
        # absolute difference is always at least 0, so return
        # n*(n+1)/2 directly (the two ranges would otherwise
        # double-count pref[i] == pref[j+1] - goal).
        n = len(nums)
        if k == 0:
            return n * (n + 1) // 2
        pref = [0] * (n + 1)
        for i, x in enumerate(nums):
            pref[i + 1] = pref[i] + x
        vals = sorted(set(pref))
        ft = Fenwick(len(vals))

        def idx(v):
            return bisect_left(vals, v) + 1  # 1-based Fenwick index

        ft.add(idx(pref[0]), 1)
        ans = 0
        for j in range(n):
            cur = pref[j + 1]
            lo = cur - goal - k
            hi = cur - goal + k
            # prefixes <= lo: count of compressed values <= lo
            ans += ft.sum(bisect_right(vals, lo))
            # prefixes >= hi: total seen minus those < hi
            ans += (j + 1) - ft.sum(bisect_left(vals, hi))
            ft.add(idx(cur), 1)
        return ans
