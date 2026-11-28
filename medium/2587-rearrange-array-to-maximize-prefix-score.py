# LeetCode 2587. Rearrange Array to Maximize Prefix Score — Medium
# https://leetcode.com/problems/rearrange-array-to-maximize-prefix-score/
# Submission 2205087661 — Accepted, Python3
#
# My thinking: put the largest numbers first — that keeps every
# prefix sum as high as possible for as long as possible. The
# score is the longest leading run whose running total stays
# positive.
class Solution:
    def maxScore(self, nums: list[int]) -> int:
        nums.sort(reverse=True)
        score = 0
        total = 0
        for x in nums:
            total += x
            if total <= 0:
                break
            score += 1
        return score
