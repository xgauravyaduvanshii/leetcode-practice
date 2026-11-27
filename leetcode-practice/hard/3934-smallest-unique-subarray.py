# LeetCode 3934. Smallest Unique Subarray — Hard
# https://leetcode.com/problems/smallest-unique-subarray/
# Submission 2202901389 — Accepted, Python3
from typing import List


class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        # My thinking: a subarray is unique when no other subarray
        # has the same contents. If some length has a unique
        # subarray, every longer length does too, because I can
        # stretch a unique subarray by one element and it stays
        # unique. So the answer is the smallest length where a
        # unique subarray first appears, and I find that length
        # with binary search. To test one length fast, I give
        # every subarray of that length a rolling hash number,
        # then count how often each hash shows up: a hash seen
        # exactly once means a unique subarray of that length.
        n = len(nums)
        if n == 1:
            return 1

        import numpy as np

        hash_base = np.uint64(91138233)
        prefix_hash = np.zeros(n + 1, dtype=np.uint64)
        base_powers = np.zeros(n + 1, dtype=np.uint64)
        base_powers[0] = np.uint64(1)
        for index, number in enumerate(nums):
            prefix_hash[index + 1] = prefix_hash[index] * hash_base + np.uint64(number + 1007)
            base_powers[index + 1] = base_powers[index] * hash_base

        def has_unique_subarray(length):
            # rolling hash of every window of this length
            window_hashes = (
                prefix_hash[length:]
                - prefix_hash[: n - length + 1] * base_powers[length]
            )
            _, counts = np.unique(window_hashes, return_counts=True)
            return bool(np.any(counts == 1))

        shortest, longest, answer = 1, n, n
        while shortest <= longest:
            middle = (shortest + longest) // 2
            if has_unique_subarray(middle):
                answer = middle
                longest = middle - 1
            else:
                shortest = middle + 1
        return answer
