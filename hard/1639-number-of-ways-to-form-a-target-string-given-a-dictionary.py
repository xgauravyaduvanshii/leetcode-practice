class Solution:
    def numWays(self, words: list[str], target: str) -> int:
        # My thinking: a column can only give one letter, so
        # walk the columns left to right and grow the ways to
        # build more and more of the target.
        MOD = 10 ** 9 + 7
        m = len(words[0])
        freq = [[0] * 26 for _ in range(m)]
        for w in words:
            for i, c in enumerate(w):
                freq[i][ord(c) - 97] += 1
        dp = [0] * (len(target) + 1)
        dp[0] = 1
        for i in range(m):
            for j in range(len(target) - 1, -1, -1):
                dp[j + 1] = (dp[j + 1] + dp[j] * freq[i][ord(target[j]) - 97]) % MOD
        return dp[len(target)]
