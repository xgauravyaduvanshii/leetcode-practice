# LeetCode 2333. Minimum Sum of Squared Difference — Medium
# https://leetcode.com/problems/minimum-sum-of-squared-difference/
# Submission 2204708352 — Accepted, Python3
#
# My thinking: only the absolute differences between the two arrays
# matter, and I have k total operations to shrink them. Binary-search
# the smallest cap t such that pulling every difference above t down to
# t costs at most k operations. Differences below t stay as they are;
# with the leftover operations I pull some of the t's down to t-1. The
# answer is the sum of squares of the final differences.
class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        k = k1 + k2
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        if sum(diffs) <= k:
            return 0
        lo, hi = 0, max(diffs)
        while lo < hi:
            mid = (lo + hi) // 2
            if sum(max(0, d - mid) for d in diffs) <= k:
                hi = mid
            else:
                lo = mid + 1
        t = lo
        cost = sum(max(0, d - t) for d in diffs)
        leftover = k - cost
        ans = 0
        m = 0
        for d in diffs:
            if d < t:
                ans += d * d
            else:
                m += 1
        ans += (m - leftover) * t * t + leftover * (t - 1) * (t - 1)
        return ans
