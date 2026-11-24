# LeetCode 3312. Sorted GCD Pair Queries — Hard
# https://leetcode.com/problems/sorted-gcd-pair-queries/
# Submission 2202321203 — Accepted, Python3
import bisect
import math
from typing import List


class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        # My thinking: for each d I count how many numbers are divisible by d,
        # which gives the number of pairs whose gcd is a multiple of d. Working
        # down from the largest value and subtracting the counts of the larger
        # multiples of d leaves exactly the pairs whose gcd IS d. A prefix sum
        # over d then turns each query into a binary search for the smallest d
        # whose running pair count passes the query index.
        max_v = max(nums)
        freq = [0] * (max_v + 1)
        for v in nums:
            freq[v] += 1
        exact = [0] * (max_v + 1)
        for d in range(max_v, 0, -1):
            divisible = 0
            for mult in range(d, max_v + 1, d):
                divisible += freq[mult]
            pairs = divisible * (divisible - 1) // 2
            for mult in range(2 * d, max_v + 1, d):
                pairs -= exact[mult]
            exact[d] = pairs
        prefix = [0] * (max_v + 1)
        running = 0
        for d in range(1, max_v + 1):
            running += exact[d]
            prefix[d] = running
        return [bisect.bisect_left(prefix, q + 1, 1) for q in queries]
