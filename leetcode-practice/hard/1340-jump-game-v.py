class Solution:
    def maxJumps(self, arr: list[int], d: int) -> int:
        # My thinking: from each spot you can only jump over
        # smaller heights, so the longest walk from a spot is
        # one more than the best walk from anywhere you can
        # reach — work from the lowest spots upward.
        n = len(arr)
        dp = [1] * n
        order = sorted(range(n), key=lambda i: arr[i])
        for i in order:
            for step in range(1, d + 1):
                j = i + step
                if j >= n or arr[j] >= arr[i]:
                    break
                dp[i] = max(dp[i], dp[j] + 1)
            for step in range(1, d + 1):
                j = i - step
                if j < 0 or arr[j] >= arr[i]:
                    break
                dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
