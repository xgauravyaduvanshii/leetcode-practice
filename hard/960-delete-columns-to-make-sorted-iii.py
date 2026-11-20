class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        # My thinking: keep the longest chain of columns that is
        # already sorted in every row — everything else gets
        # deleted.
        m = len(strs[0])
        dp = [1] * m
        for i in range(m):
            for j in range(i):
                if all(strs[r][j] <= strs[r][i] for r in range(len(strs))):
                    dp[i] = max(dp[i], dp[j] + 1)
        return m - max(dp)
