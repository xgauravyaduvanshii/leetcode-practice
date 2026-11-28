# LeetCode 2718. Sum of Matrix After Queries — Medium
# https://leetcode.com/problems/sum-of-matrix-after-queries/
# Submission 2205210694 — Accepted, Python3
#
# My thinking: later queries overwrite earlier ones, so replay
# the queries backwards and count each row or column only the
# first time it appears — that is its final value. A row set at
# that point covers the columns not yet set in the reverse pass,
# and vice versa for a column.
class Solution:
    def matrixSumQueries(self, n: int, queries: list[list[int]]) -> int:
        rows, cols = set(), set()
        ans = 0
        for typ, idx, val in reversed(queries):
            if typ == 0:
                if idx not in rows:
                    rows.add(idx)
                    ans += val * (n - len(cols))
            else:
                if idx not in cols:
                    cols.add(idx)
                    ans += val * (n - len(rows))
        return ans
