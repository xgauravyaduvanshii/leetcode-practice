class Solution:
    def maxSizeSlices(self, slices: list[int]) -> int:
        # My thinking: a circle breaks two ways — skip the
        # first slice or skip the last — and each straight
        # line is a take-it-or-leave-it table over how many
        # slices are taken.
        n = len(slices) // 3

        def best(arr):
            m = len(arr)
            dp = [[0] * (n + 1) for _ in range(m + 1)]
            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    dp[i][j] = dp[i - 1][j]
                    if i >= 2:
                        dp[i][j] = max(dp[i][j], dp[i - 2][j - 1] + arr[i - 1])
                    elif j == 1:
                        dp[i][j] = max(dp[i][j], arr[i - 1])
            return dp[m][n]

        return max(best(slices[1:]), best(slices[:-1]))
