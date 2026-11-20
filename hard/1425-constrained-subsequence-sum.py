from collections import deque


class Solution:
    def constrainedSubsetSum(self, nums: list[int], k: int) -> int:
        # My thinking: each position either starts a fresh
        # subsequence or extends the best one ending within
        # the last k positions — a sliding window keeps that
        # best in reach.
        n = len(nums)
        dp = [0] * n
        best = float("-inf")
        window = deque()
        for i in range(n):
            while window and window[0] < i - k:
                window.popleft()
            prev = dp[window[0]] if window else 0
            dp[i] = nums[i] + max(0, prev)
            best = max(best, dp[i])
            while window and dp[window[-1]] <= dp[i]:
                window.pop()
            window.append(i)
        return best
