# 278. First Bad Version (Easy)
# https://leetcode.com/problems/first-bad-version/
# Submission 2199957658 — Accepted, Python3
class Solution:
    def firstBadVersion(self, n: int) -> int:
        # My thinking: versions go good...good, then
        # bad...bad, so the first bad one is a boundary.
        # Binary search on that boundary: a bad middle
        # means the first bad version is at or before it,
        # a good middle means it lies after it.
        low, high = 1, n
        while low < high:
            mid = (low + high) // 2
            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1
        return low
