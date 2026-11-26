# LeetCode 47. Permutations II — Medium
# https://leetcode.com/problems/permutations-ii/
# Submission 2203825975 — Accepted, Python3
#
# My thinking: I sort the numbers first so equal values sit together,
# then build permutations with backtracking as in Permutations. The
# extra rule is the dedupe: at each level I skip a number when it
# equals the previous one and that previous one is not currently in
# use, because that arrangement was already covered by the earlier
# equal number.

class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
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
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                current.append(nums[i])
                backtrack()
                current.pop()
                used[i] = False

        backtrack()
        return ans
