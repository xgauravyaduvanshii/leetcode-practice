class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        # My thinking: from each position, try every length
        # up to ten digits — no leading zero, and the number
        # must stay within k — then add the ways from where
        # that number ends.
        MOD = 10 ** 9 + 7
        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 1
        for i in range(n - 1, -1, -1):
            if s[i] == "0":
                continue
            num = 0
            for j in range(i, min(i + 10, n)):
                num = num * 10 + int(s[j])
                if num > k:
                    break
                dp[i] = (dp[i] + dp[j + 1]) % MOD
        return dp[0]
