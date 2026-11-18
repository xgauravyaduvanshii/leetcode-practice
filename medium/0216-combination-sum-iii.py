# LeetCode 216. Combination Sum III — Medium
# https://leetcode.com/problems/combination-sum-iii/
# Submission 2198457141 — Accepted, Python3
#
# My thinking: I build the combinations one number
# at a time, always moving to a bigger digit so no
# combination is ever repeated in another order. I
# stop a branch as soon as the numbers run out or
# the sum is already too big, and I save the
# combination when exactly k numbers add up to n.

from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        answer = []

        def backtrack(start: int, remaining_k: int, remaining_n: int, combo: List[int]) -> None:
            if remaining_k == 0 and remaining_n == 0:
                answer.append(list(combo))
                return
            if remaining_k == 0 or remaining_n <= 0:
                return
            for num in range(start, 10):
                combo.append(num)
                backtrack(num + 1, remaining_k - 1, remaining_n - num, combo)
                combo.pop()

        backtrack(1, k, n, [])
        return answer
