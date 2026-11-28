# LeetCode 2616. Minimize the Maximum Difference of Pairs — Medium
# https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/
# Submission 2205105978 — Accepted, Python3
#
# My thinking: sort, then binary-search the answer. For a
# candidate max difference d, greedily pair neighbours whose
# gap is at most d — pairing the leftmost fitting neighbour
# first never hurts, so if even that greedy count is below p,
# d is too small.
class Solution:
    def minimizeMax(self, nums: list[int], p: int) -> int:
        nums.sort()

        def can(d):
            cnt = 0
            i = 0
            while i + 1 < len(nums):
                if nums[i + 1] - nums[i] <= d:
                    cnt += 1
                    i += 2
                else:
                    i += 1
            return cnt >= p

        lo, hi = 0, nums[-1] - nums[0]
        while lo < hi:
            mid = (lo + hi) // 2
            if can(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
