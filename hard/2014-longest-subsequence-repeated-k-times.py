# LeetCode 2014. Longest Subsequence Repeated k Times — Hard
# https://leetcode.com/problems/longest-subsequence-repeated-k-times/
# Submission 2201313447 — Accepted, Python3
#
# My thinking: a letter can only appear if it
# shows up at least k times, and a prefix only
# counts if the whole thing repeated k times
# still fits — so I walk every prefix that fits
# and keep the longest, then the biggest.

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        n = len(s)
        nxt = [[-1] * 26 for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            nxt[i] = nxt[i + 1][:]
            nxt[i][ord(s[i]) - 97] = i

        def can(t):
            pos = 0
            for _ in range(k):
                for ch in t:
                    idx = nxt[pos][ord(ch) - 97]
                    if idx == -1:
                        return False
                    pos = idx + 1
            return True

        from collections import Counter
        cnt = Counter(s)
        chars = sorted([c for c, v in cnt.items() if v >= k], reverse=True)
        best = ""
        maxlen = n // k

        def dfs(t):
            nonlocal best
            if len(t) > len(best) or (len(t) == len(best) and t > best):
                best = t
            if len(t) == maxlen:
                return
            for c in chars:
                if can(t + c):
                    dfs(t + c)

        dfs("")
        return best
