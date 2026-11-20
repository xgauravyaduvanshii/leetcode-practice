# 3318. Find X-Sum of All K-Long Subarrays I (Easy)
# https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/
# Submission 2200003358 — Accepted, Python3
from collections import Counter
from typing import List


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        # My thinking: slide the window along. Inside
        # each window I rank the numbers by how often
        # they appear — ties go to the bigger number —
        # then add up the top x numbers, each counted as
        # many times as it appears.
        answer = []
        for start in range(len(nums) - k + 1):
            counts = Counter(nums[start:start + k])
            ranked = sorted(counts.items(), key=lambda item: (-item[1], -item[0]))
            total = 0
            for value, count in ranked[:x]:
                total += value * count
            answer.append(total)
        return answer
