# LeetCode 46. Permutations — Medium
# https://leetcode.com/problems/permutations/
# Submission 2203823633 — Accepted, Python3
#
# My thinking: I build each permutation one slot at a time with
# backtracking, trying every number I have not used yet in the current
# slot and marking it used until I backtrack. When every slot is
# filled, the current arrangement is one complete permutation.

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans = []
        current = []
        used = [False] * len(nums)

        def backtrack() -> None:
            if len(current) == len(nums):
                ans.append(current[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                current.append(nums[i])
                backtrack()
                current.pop()
                used[i] = False

        backtrack()
        return ans
