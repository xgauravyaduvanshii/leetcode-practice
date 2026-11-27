# LeetCode 78. Subsets — Medium
# https://leetcode.com/problems/subsets/
# Submission 2203846191 — Accepted, Python3
#
# My thinking: I build every subset with backtracking, deciding for
# each number in turn whether to include it. At every step of the
# recursion the current selection is itself a valid subset, so I
# record it before branching further, which produces all 2^n subsets
# exactly once.

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans = []
        current = []

        def backtrack(start: int) -> None:
            ans.append(current[:])
            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(i + 1)
                current.pop()

        backtrack(0)
        return ans
