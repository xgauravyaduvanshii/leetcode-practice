# LeetCode 321. Create Maximum Number — Hard
# https://leetcode.com/problems/create-maximum-number/
# Submission 2198405086 — Accepted, Python3
#
# My thinking: I decide how many digits come from
# each array, then take the biggest subsequence of
# that length from each — keeping order and dropping
# a smaller digit whenever a bigger one follows.
# The two subsequences are merged by always taking
# the one whose remaining tail is larger. I try
# every split of the count between the two arrays
# and keep the biggest result.

from typing import List


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def pick(nums: List[int], take: int) -> List[int]:
            drop = len(nums) - take
            stack = []
            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:take]

        def merge(a: List[int], b: List[int]) -> List[int]:
            merged = []
            while a or b:
                if a > b:
                    merged.append(a.pop(0))
                else:
                    merged.append(b.pop(0))
            return merged

        best = []
        for take1 in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            take2 = k - take1
            candidate = merge(pick(nums1, take1), pick(nums2, take2))
            best = max(best, candidate)
        return best
