# LeetCode 3225. Maximum Score From Grid Operations — Hard
# https://leetcode.com/problems/maximum-score-from-grid-operations/
# Submission 2202103541 — Accepted, Python3
#
# My thinking: I process the columns left
# to right, keeping for each pair of
# consecutive heights the best score so
# far. A column's score is the sum of its
# top entries down to the taller of its
# neighbours, so each transition needs
# only prefix and suffix maxima over the
# previous height — that keeps the whole
# DP quadratic per column.

from typing import List


class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        col_pref = []
        for c in range(n):
            pref = [0] * (n + 1)
            s = 0
            for i in range(n):
                s += grid[i][c]
                pref[i + 1] = s
            col_pref.append(pref)
        zero_pref = [0] * (n + 1)
        NEG = -10 ** 18
        dp_cur = [[NEG] * (n + 1) for _ in range(n + 1)]
        dp_cur[0][0] = 0
        for c in range(n + 1):
            pref = zero_pref if c == 0 else col_pref[c - 1]
            hs = [0] if c == n else range(n + 1)
            dp_next = [[NEG] * (n + 1) for _ in range(n + 1)]
            for a in range(n + 1):
                row = dp_cur[a]
                pa = pref[a]
                pref_max = [NEG] * (n + 2)
                cur = NEG
                for b in range(n + 1):
                    if row[b] > cur:
                        cur = row[b]
                    pref_max[b + 1] = cur
                suff = [NEG] * (n + 2)
                cur = NEG
                for b in range(n, -1, -1):
                    vb = row[b]
                    if vb != NEG:
                        if b > a:
                            vb += pref[b] - pa
                        if vb > cur:
                            cur = vb
                    suff[b] = cur
                for h in hs:
                    cand1 = suff[h]
                    pm = pref_max[h]
                    if pm == NEG:
                        cand2 = NEG
                    elif h > a:
                        cand2 = pm + pref[h] - pa
                    else:
                        cand2 = pm
                    dp_next[h][a] = cand1 if cand1 > cand2 else cand2
            dp_cur = dp_next
        return max(dp_cur[0])
