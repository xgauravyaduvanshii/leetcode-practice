# LeetCode 955. Delete Columns to Make Sorted II — Medium
# https://leetcode.com/problems/delete-columns-to-make-sorted-ii/
# Submission 2198976291 — Accepted, Python3
#
# My thinking: I keep each column unless it
# breaks the order of some pair that earlier
# columns have not already settled. Once a pair
# is strictly ordered by a kept column, later
# columns can never break it.

from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        width = len(strs[0])
        deletions = 0
        sorted_pairs = [False] * (n - 1)
        for col in range(width):
            bad = False
            for row in range(n - 1):
                if not sorted_pairs[row] and strs[row][col] > strs[row + 1][col]:
                    bad = True
                    break
            if bad:
                deletions += 1
                continue
            for row in range(n - 1):
                if strs[row][col] < strs[row + 1][col]:
                    sorted_pairs[row] = True
        return deletions
