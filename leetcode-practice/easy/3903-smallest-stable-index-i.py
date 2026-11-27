# 3903. Smallest Stable Index I (Easy)
# https://leetcode.com/problems/smallest-stable-index-i/
# Submission 2200086382 — Accepted, Python3
class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        # My thinking: the instability at each spot is
        # the biggest number seen so far minus the
        # smallest number still ahead. I sweep once
        # from each side and take the first spot whose
        # score fits within k.
        n = len(nums)
        suffix_min = [0] * n
        cur = nums[-1]
        for i in range(n - 1, -1, -1):
            cur = min(cur, nums[i])
            suffix_min[i] = cur
        prefix_max = nums[0]
        for i in range(n):
            prefix_max = max(prefix_max, nums[i])
            if prefix_max - suffix_min[i] <= k:
                return i
        return -1
