# LeetCode 40. Combination Sum II — Medium
# https://leetcode.com/problems/combination-sum-ii/
# Submission 2203821776 — Accepted, Python3
#
# My thinking: like Combination Sum, I build combinations with
# backtracking, but each candidate may be used only once, so after
# taking a number I move to the next index. I sort first and skip a
# candidate when it equals the previous one at the same level, which
# keeps duplicate combinations out of the answer.

class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        ans = []
        combo = []

        def backtrack(start: int, remaining: int) -> None:
            if remaining == 0:
                ans.append(combo[:])
                return
            if remaining < 0:
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                combo.append(candidates[i])
                backtrack(i + 1, remaining - candidates[i])
                combo.pop()

        backtrack(0, target)
        return ans
