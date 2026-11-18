# LeetCode 410. Split Array Largest Sum — Hard
# https://leetcode.com/problems/split-array-largest-sum/
# Submission 2198657516 — Accepted, Python3
#
# My thinking: the answer sits somewhere between the
# biggest single number and the total sum. I guess a
# limit and greedily cut a new subarray whenever the
# running sum would pass it — if I need more than k
# pieces, the limit is too small.

from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def pieces_needed(limit):
            pieces = 1
            running = 0
            for num in nums:
                if running + num > limit:
                    pieces += 1
                    running = num
                else:
                    running += num
            return pieces

        low, high = max(nums), sum(nums)
        while low < high:
            middle = (low + high) // 2
            if pieces_needed(middle) <= k:
                high = middle
            else:
                low = middle + 1
        return low
