# 3712. Sum of Elements With Frequency Divisible by K (Easy)
# https://leetcode.com/problems/sum-of-elements-with-frequency-divisible-by-k/
# Submission 2200045654 — Accepted, Python3
from collections import Counter
from typing import List


class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        # My thinking: count how often each number
        # appears. A number counts toward the sum when
        # its count divides cleanly by k — and every
        # copy of it counts.
        counts = Counter(nums)
        return sum(num for num in nums if counts[num] % k == 0)
