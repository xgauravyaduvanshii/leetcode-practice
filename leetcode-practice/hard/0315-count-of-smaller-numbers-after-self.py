# LeetCode 315. Count of Smaller Numbers After Self — Hard
# https://leetcode.com/problems/count-of-smaller-numbers-after-self/
# Submission 2198404151 — Accepted, Python3
#
# My thinking: I sort the numbers with merge sort
# while keeping each number's original position.
# When I merge, every number from the right half
# that is smaller than a number from the left half
# stood after it in the original array — so I add
# that count to the left number's answer. Each
# number is counted exactly once per merge level.

from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        counts = [0] * len(nums)
        indexed = list(enumerate(nums))

        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            merged = []
            j = 0
            for i in range(len(left)):
                while j < len(right) and right[j][1] < left[i][1]:
                    merged.append(right[j])
                    j += 1
                counts[left[i][0]] += j
                merged.append(left[i])
            merged.extend(right[j:])
            return merged

        merge_sort(indexed)
        return counts
