# LeetCode 3115. Maximum Prime Difference — Medium
# https://leetcode.com/problems/maximum-prime-difference/
# Submission 2200956367 — Accepted, Python3
#
# My thinking: the answer is just the distance between
# the first and the last prime in the array, so I find
# both ends and subtract.

class Solution:
    def maximumPrimeDifference(self, nums: list[int]) -> int:
        def is_prime(x: int) -> bool:
            if x < 2:
                return False
            d = 2
            while d * d <= x:
                if x % d == 0:
                    return False
                d += 1
            return True

        first = next(i for i, x in enumerate(nums) if is_prime(x))
        last = max(i for i, x in enumerate(nums) if is_prime(x))
        return last - first
