class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        # My thinking: count playlists by length and distinct songs
        # used — each new song adds n - j choices, each repeat adds
        # j - k choices.
        MOD = 10 ** 9 + 7
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, goal + 1):
            new = [0] * (n + 1)
            for j in range(1, min(i, n) + 1):
                new[j] = (new[j] + dp[j - 1] * (n - j + 1)) % MOD
                if j > k:
                    new[j] = (new[j] + dp[j] * (j - k)) % MOD
            dp = new
        return dp[n]
