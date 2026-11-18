# LeetCode 1031. Maximum Sum of Two Non-Overlapping Subarrays — Medium
# https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/
# Submission 2198989685 — Accepted, Python3
#
# My thinking: I try both orders — the first
# subarray before the second, and the other way
# round. In each order I sweep once, keeping the
# best first subarray seen so far and pairing it
# with each possible second one.

from typing import List


class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        def best(first, second):
            prefix = [0]
            for num in nums:
                prefix.append(prefix[-1] + num)
            best_first = 0
            result = 0
            for i in range(first, len(nums) - second + 1):
                best_first = max(best_first, prefix[i] - prefix[i - first])
                second_sum = prefix[i + second] - prefix[i]
                result = max(result, best_first + second_sum)
            return result

        return max(best(firstLen, secondLen), best(secondLen, firstLen))
