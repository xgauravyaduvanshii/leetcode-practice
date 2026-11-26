# LeetCode 3981. Count Distinct Ways to Form Target from Two Strings — Hard
# https://leetcode.com/problems/count-distinct-ways-to-form-target-from-two-strings/
# Submission 2203495386 — Accepted, Python3


class Solution:
    def interleaveCharacters(self, word1: str, word2: str, target: str) -> int:
        # My thinking: work backwards through the target.
        # f(i, j, t) is the number of ways to form
        # target[t:] using word1[i:] and word2[j:]; its
        # first character comes from word1 at some position
        # p >= i or from word2 at some position q >= j,
        # and suffix sums over p and q make each level
        # O(n^2). The empty suffix has one way. This counts
        # every way, including ones that use only one word,
        # so subtract the plain subsequence counts of the
        # target in each word alone; the two subtracted sets
        # are disjoint. Everything is modulo 10^9 + 7.
        MOD = 10 ** 9 + 7
        n1, n2, m = len(word1), len(word2), len(target)
        nxt = [[1] * (n2 + 1) for _ in range(n1 + 1)]
        for t in range(m - 1, -1, -1):
            ch = target[t]
            s1 = [[0] * (n2 + 1) for _ in range(n1 + 2)]
            s2 = [[0] * (n2 + 2) for _ in range(n1 + 1)]
            for i in range(n1, -1, -1):
                for j in range(n2 + 1):
                    if i < n1 and word1[i] == ch:
                        s1[i][j] = (s1[i + 1][j] + nxt[i + 1][j]) % MOD
                    else:
                        s1[i][j] = s1[i + 1][j]
            for i in range(n1 + 1):
                for j in range(n2, -1, -1):
                    if j < n2 and word2[j] == ch:
                        s2[i][j] = (s2[i][j + 1] + nxt[i][j + 1]) % MOD
                    else:
                        s2[i][j] = s2[i][j + 1]
            nxt = [[(s1[i][j] + s2[i][j]) % MOD for j in range(n2 + 1)] for i in range(n1 + 1)]
        total = nxt[0][0]

        def subseq_count(w: str) -> int:
            dp = [0] * (m + 1)
            dp[0] = 1
            for ch in w:
                for t in range(m, 0, -1):
                    if ch == target[t - 1]:
                        dp[t] = (dp[t] + dp[t - 1]) % MOD
            return dp[m]

        return (total - subseq_count(word1) - subseq_count(word2)) % MOD
