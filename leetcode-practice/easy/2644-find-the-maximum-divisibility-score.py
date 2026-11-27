# 2644. Find the Maximum Divisibility Score (Easy)
# https://leetcode.com/problems/find-the-maximum-divisibility-score/
# Submission 2199969596 — Accepted, Python3
from typing import List


class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        # My thinking: score every divisor by how many
        # numbers it divides. The best score wins, and
        # a tie goes to the smaller divisor — so I only
        # replace the answer when a score is strictly
        # better.
        best_divisor = divisors[0]
        best_score = -1
        for d in divisors:
            score = sum(1 for num in nums if num % d == 0)
            if score > best_score:
                best_score = score
                best_divisor = d
        return best_divisor
