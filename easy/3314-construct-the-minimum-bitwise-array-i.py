# 3314. Construct the Minimum Bitwise Array I (Easy)
# https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/
# Submission 2200003072 — Accepted, Python3
from typing import List


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        # My thinking: for each number I try candidates
        # from zero upward and keep the first one whose
        # OR with the next number gives the target. If
        # the target is even, no candidate can work,
        # because the OR would always be odd.
        answer = []
        for num in nums:
            if num % 2 == 0:
                answer.append(-1)
                continue
            for x in range(num):
                if x | (x + 1) == num:
                    answer.append(x)
                    break
            else:
                answer.append(-1)
        return answer
