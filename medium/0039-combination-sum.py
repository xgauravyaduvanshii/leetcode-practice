# LeetCode 39. Combination Sum — Medium
# https://leetcode.com/problems/combination-sum/
# Submission 2203819544 — Accepted, Python3
#
# My thinking: I build combinations with backtracking, always moving
# forward through the candidates so the same set is never built twice
# in a different order. At each step I either take the current number
# again (it can be reused) or move on to the next one; when the
# remaining target hits zero I have a valid combination, and when it
# goes below zero that branch is dead.

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        ans = []
        combo = []

        def backtrack(start: int, remaining: int) -> None:
            if remaining == 0:
                ans.append(combo[:])
                return
            if remaining < 0:
                return
            for i in range(start, len(candidates)):
                combo.append(candidates[i])
                backtrack(i, remaining - candidates[i])
                combo.pop()

        backtrack(0, target)
        return ans
