# LeetCode 719. Find K-th Smallest Pair Distance — Hard
# https://leetcode.com/problems/find-k-th-smallest-pair-distance/
# Submission 2198668906 — Accepted, Python3
#
# My thinking: after sorting, I binary search the
# answer itself. For any guess I count the pairs no
# farther apart than that — a sliding window does it
# in one pass. If the count reaches k the guess is
# big enough.

from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()

        def count_upto(limit):
            total = 0
            left = 0
            for right in range(len(nums)):
                while nums[right] - nums[left] > limit:
                    left += 1
                total += right - left
            return total

        low, high = 0, nums[-1] - nums[0]
        while low < high:
            middle = (low + high) // 2
            if count_upto(middle) >= k:
                high = middle
            else:
                low = middle + 1
        return low
