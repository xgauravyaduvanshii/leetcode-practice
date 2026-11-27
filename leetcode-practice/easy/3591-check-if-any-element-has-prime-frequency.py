# 3591. Check if Any Element Has Prime Frequency (Easy)
# https://leetcode.com/problems/check-if-any-element-has-prime-frequency/
# Submission 2200032300 — Accepted, Python3
from collections import Counter
from typing import List


class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        # My thinking: count how often each number
        # appears. If any count is prime — 2, 3, 5, 7
        # and so on — the answer is yes.
        def is_prime(x: int) -> bool:
            if x < 2:
                return False
            for d in range(2, int(x ** 0.5) + 1):
                if x % d == 0:
                    return False
            return True

        return any(is_prime(c) for c in Counter(nums).values())
