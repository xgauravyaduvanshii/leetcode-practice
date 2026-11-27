# LeetCode 2055. Plates Between Candles — Medium
# https://leetcode.com/problems/plates-between-candles/
# Submission 2204386391 — Accepted, Python3
#
# My thinking: for each query I need the plates strictly between the
# first candle at or after l and the last candle at or before r. I
# precompute a prefix count of plates and, for every position, the
# nearest candle on the left and on the right, so each query is
# answered in constant time from those tables.
class Solution:
    def platesBetweenCandles(self, s: str, queries: list[list[int]]) -> list[int]:
        n = len(s)
        pref = [0] * (n + 1)
        for i, ch in enumerate(s):
            pref[i + 1] = pref[i] + (ch == '*')
        left = [-1] * n
        last = -1
        for i, ch in enumerate(s):
            if ch == '|':
                last = i
            left[i] = last
        right = [-1] * n
        nxt = -1
        for i in range(n - 1, -1, -1):
            if s[i] == '|':
                nxt = i
            right[i] = nxt
        ans = []
        for l, r in queries:
            a = right[l]
            b = left[r]
            if a == -1 or b == -1 or a >= b:
                ans.append(0)
            else:
                ans.append(pref[b] - pref[a + 1])
        return ans
