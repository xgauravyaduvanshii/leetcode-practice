# LeetCode 3256. Maximum Value Sum by Placing Three Rooks I — Hard
# https://leetcode.com/problems/maximum-value-sum-by-placing-three-rooks-i/
# Submission 2202148558 — Accepted, Python3
#
# My thinking: a rook's best cells are always
# among its row's top 3, since only two other
# rooks can block its columns. I keep each
# row's top 3, sort rows by their best cell,
# and try every triple of rows with distinct
# columns, pruning whenever the three row
# maxima can no longer beat the best sum.

from typing import List


class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        rows = []
        for row in board:
            idx = sorted(range(len(row)), key=lambda j: row[j], reverse=True)[:3]
            rows.append([(row[j], j) for j in idx])
        rows.sort(key=lambda r: r[0][0], reverse=True)
        m = len(rows)
        best = -10 ** 18
        for i in range(m - 2):
            ri = rows[i]
            if ri[0][0] + rows[i + 1][0][0] + rows[i + 2][0][0] <= best:
                break
            for j in range(i + 1, m - 1):
                rj = rows[j]
                if ri[0][0] + rj[0][0] + rows[j + 1][0][0] <= best:
                    break
                for k in range(j + 1, m):
                    rk = rows[k]
                    if ri[0][0] + rj[0][0] + rk[0][0] <= best:
                        break
                    for v1, c1 in ri:
                        for v2, c2 in rj:
                            if c1 == c2:
                                continue
                            s12 = v1 + v2
                            for v3, c3 in rk:
                                if c3 == c1 or c3 == c2:
                                    continue
                                s = s12 + v3
                                if s > best:
                                    best = s
        return best
