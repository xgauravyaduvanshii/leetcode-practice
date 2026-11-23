# LeetCode 2565. Subsequence With the Minimum Score — Hard
# https://leetcode.com/problems/subsequence-with-the-minimum-score/
# Submission 2201822377 — Accepted, Python3
#
# My thinking: I keep a prefix of t and
# a suffix of t, and the part I cut out
# is whatever sits between them — I
# learn how far each prefix reaches into
# s and where each suffix must start,
# then slide the cut until the two ends
# just meet.

class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        INF = float("inf")
        # pref[i]: index in s just after matching t[:i]; INF if impossible
        pref = [INF] * (m + 1)
        pref[0] = 0
        p = 0
        for i in range(m):
            while p < n and s[p] != t[i]:
                p += 1
            if p == n:
                break
            p += 1
            pref[i + 1] = p
        # suff[i]: index in s where the match of t[i:] starts; -1 if impossible
        suff = [-1] * (m + 1)
        suff[m] = n
        p = n - 1
        for i in range(m - 1, -1, -1):
            while p >= 0 and s[p] != t[i]:
                p -= 1
            if p < 0:
                break
            suff[i] = p
            p -= 1
        if pref[m] <= n:
            return 0
        ans = m
        # remove t[l..r]; keep t[:l] and t[r+1:]; need pref[l] <= suff[r+1]
        r = -1
        for l in range(m + 1):
            if pref[l] == INF:
                break
            if r < l - 1:
                r = l - 1
            while r + 1 < m and suff[r + 1] < pref[l]:
                r += 1
            ans = min(ans, r - l + 1)
        return ans
