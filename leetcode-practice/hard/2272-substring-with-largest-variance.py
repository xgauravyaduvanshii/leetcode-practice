# LeetCode 2272. Substring With Largest Variance — Hard
# https://leetcode.com/problems/substring-with-largest-variance/
# Submission 2201648457 — Accepted, Python3
#
# My thinking: for one ordered pair of
# letters the variance is just a signed
# running total, so I sweep every pair and
# keep the best stretch that holds at
# least one of the losing letter.

class Solution:
    def largestVariance(self, s: str) -> int:
        n = len(s)
        present = set(s)
        ans = 0
        for a in present:
            for b in present:
                if a == b:
                    continue
                pref = [0] * (n + 1)
                for i, c in enumerate(s):
                    d = 1 if c == a else (-1 if c == b else 0)
                    pref[i + 1] = pref[i] + d
                pref_min = [0] * (n + 1)
                pref_min[0] = pref[0]
                for k in range(1, n + 1):
                    pref_min[k] = pref_min[k - 1] if pref_min[k - 1] < pref[k] else pref[k]
                last_b = -1
                for i in range(1, n + 1):
                    if s[i - 1] == b:
                        last_b = i - 1
                    if last_b >= 0:
                        cand = pref[i] - pref_min[last_b]
                        if cand > ans:
                            ans = cand
        return ans
