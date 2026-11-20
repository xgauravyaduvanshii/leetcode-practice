# LeetCode 1696. Jump Game VI — Medium
# https://leetcode.com/problems/jump-game-vi/
# Submission 2199914256 — Accepted, Python3
#
# My thinking: each position's best score is
# its value plus the best score from the k
# positions before it. A decreasing deque
# keeps that best in reach as I move forward.

from collections import deque
from typing import List


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        queue = deque([0])
        for i in range(1, n):
            while queue and queue[0] < i - k:
                queue.popleft()
            dp[i] = nums[i] + dp[queue[0]]
            while queue and dp[queue[-1]] <= dp[i]:
                queue.pop()
            queue.append(i)
        return dp[n - 1]
