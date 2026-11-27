# LeetCode 313. Super Ugly Number — Medium
# https://leetcode.com/problems/super-ugly-number/
# Submission 2198743227 — Accepted, Python3
#
# My thinking: like the plain ugly numbers, every
# super ugly number is an earlier one times a prime
# from the list. A heap keeps the next candidate for
# each prime, and I always take the smallest one —
# skipping duplicates — until I have n of them.

import heapq
from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly = [1]
        heap = [(prime, prime, 0) for prime in primes]
        heapq.heapify(heap)
        while len(ugly) < n:
            value, prime, index = heapq.heappop(heap)
            if value != ugly[-1]:
                ugly.append(value)
            heapq.heappush(heap, (prime * ugly[index + 1], prime, index + 1))
        return ugly[-1]
