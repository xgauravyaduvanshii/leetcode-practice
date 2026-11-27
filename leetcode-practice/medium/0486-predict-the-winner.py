# LeetCode 486. Predict the Winner — Medium
# https://leetcode.com/problems/predict-the-winner/
# Submission 2198823264 — Accepted, Python3
#
# My thinking: the only thing that matters is the
# score difference the current player can force. For
# any stretch of the array that is the best of
# taking the left end or the right end, minus
# whatever the opponent then forces on the rest.

from typing import List


class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = nums[:]
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i] = max(nums[i] - dp[i + 1], nums[j] - dp[i])
        return dp[0] >= 0
