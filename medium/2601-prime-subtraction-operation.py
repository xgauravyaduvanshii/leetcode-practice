# LeetCode 2601. Prime Subtraction Operation — Medium
# https://leetcode.com/problems/prime-subtraction-operation/
# Submission 2205097605 — Accepted, Python3
#
# My thinking: each index may be operated on at most once, so
# work right to left and keep every element as large as
# possible while staying below its right neighbour. When
# nums[i] >= nums[i+1], subtract the smallest prime larger
# than nums[i] - nums[i+1] — that is the smallest cut that
# gets below the neighbour. If no such prime exists, or it
# is not smaller than nums[i] itself, the array cannot be fixed.
import bisect


def _primes_upto(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i:n + 1:i] = [False] * ((n - i * i) // i + 1)
    return [i for i, is_p in enumerate(sieve) if is_p]


class Solution:
    def primeSubOperation(self, nums: list[int]) -> bool:
        primes = _primes_upto(1000)
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                continue
            j = bisect.bisect_right(primes, nums[i] - nums[i + 1])
            if j == len(primes) or primes[j] >= nums[i]:
                return False
            nums[i] -= primes[j]
        return True
