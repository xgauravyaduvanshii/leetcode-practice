# LeetCode 3579. Minimum Steps to Convert String with Operations — Hard
# https://leetcode.com/problems/minimum-steps-to-convert-string-with-operations/
# Submission 2202860728 — Accepted, Python3


class Solution:
    def minOperations(self, word1: str, word2: str) -> int:
        # My thinking: I split the strings into blocks and price
        # each block on its own. Inside a block, a swap only helps
        # when it fixes both ends (a and b sitting in each other's
        # places), so the best I can do is pair up as many of those
        # as possible and replace the rest; a single reverse costs
        # one extra operation and is worth it only when the reversed
        # block is cheaper to finish. A DP over the split points
        # picks the cheapest blocks.
        n = len(word1)

        def cost_no_rev(S, T):
            m = 0
            cnt = [[0] * 26 for _ in range(26)]
            for a, b in zip(S, T):
                if a != b:
                    m += 1
                    cnt[ord(a) - 97][ord(b) - 97] += 1
            swaps = 0
            for a in range(26):
                for b in range(a + 1, 26):
                    swaps += min(cnt[a][b], cnt[b][a])
            return m - swaps

        def cost(l, r):
            S = word1[l:r + 1]
            T = word2[l:r + 1]
            best = cost_no_rev(S, T)
            best = min(best, 1 + cost_no_rev(S[::-1], T))
            return best

        dp = [10 ** 9] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            for j in range(i):
                dp[i] = min(dp[i], dp[j] + cost(j, i - 1))
        return dp[n]
