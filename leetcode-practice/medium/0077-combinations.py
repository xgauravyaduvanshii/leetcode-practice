# LeetCode 77. Combinations — Medium
# https://leetcode.com/problems/combinations/
# Submission 2200893113 — Accepted, Python3
#
# My thinking: I build each combination in increasing
# order, one number at a time, and stop a branch early
# when too few numbers are left to fill the combination.

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []

        def backtrack(start: int, current: list[int]) -> None:
            if len(current) == k:
                result.append(current.copy())
                return
            for num in range(start, n + 1):
                if n - num + 1 < k - len(current):
                    break
                current.append(num)
                backtrack(num + 1, current)
                current.pop()

        backtrack(1, [])
        return result
