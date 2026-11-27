# 2643. Row With Maximum Ones (Easy)
# https://leetcode.com/problems/row-with-maximum-ones/
# Submission 2199969342 — Accepted, Python3
from typing import List


class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        # My thinking: count the ones in each row and
        # keep the best row seen. A tie keeps the earlier
        # row, so I only replace the best when a row has
        # strictly more ones.
        best_row = 0
        best_count = -1
        for i, row in enumerate(mat):
            count = sum(row)
            if count > best_count:
                best_count = count
                best_row = i
        return [best_row, best_count]
