# LeetCode 2327. Number of People Aware of a Secret — Medium
# https://leetcode.com/problems/number-of-people-aware-of-a-secret/
# Submission 2204699097 — Accepted, Python3
#
# My thinking: dp[i] is how many people first learn the secret on day i.
# Someone who learned it on day j can share it from day j+delay until
# day j+forget-1, so dp[i] is the sum of dp over that sliding window,
# which a prefix sum gives in O(1). The answer is the people who learned
# it in the last `forget` days — those who have not forgotten it by day n.
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [0] * (n + 1)
        dp[1] = 1
        pref = [0] * (n + 1)
        pref[1] = 1
        for i in range(2, n + 1):
            lo = max(1, i - forget + 1)
            hi = i - delay
            if hi >= lo:
                dp[i] = (pref[hi] - pref[lo - 1]) % MOD
            pref[i] = (pref[i - 1] + dp[i]) % MOD
        return (pref[n] - pref[max(0, n - forget)]) % MOD
