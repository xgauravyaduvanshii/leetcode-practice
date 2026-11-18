# LeetCode 493. Reverse Pairs — Hard
# https://leetcode.com/problems/reverse-pairs/
# Submission 2198661236 — Accepted, Python3
#
# My thinking: I sort with merge sort, and while the
# two halves are sorted I count the cross pairs — for
# each number on the left, every number on the right
# smaller than half of it forms a pair, and because
# both halves are sorted that count only moves forward.

from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def count_and_sort(left, right):
            if right - left <= 1:
                return 0
            middle = (left + right) // 2
            count = count_and_sort(left, middle) + count_and_sort(middle, right)
            j = middle
            for i in range(left, middle):
                while j < right and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - middle
            nums[left:right] = sorted(nums[left:right])
            return count

        return count_and_sort(0, len(nums))
