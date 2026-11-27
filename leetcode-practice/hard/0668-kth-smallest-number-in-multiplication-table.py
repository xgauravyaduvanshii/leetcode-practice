# LeetCode 668. Kth Smallest Number in Multiplication Table — Hard
# https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/
# Submission 2198666120 — Accepted, Python3
#
# My thinking: I binary search the answer itself. For
# any guess I count how many table entries are at most
# that big — row by row, the count is the guess divided
# by the row number, capped at the row length. If the
# count reaches k the guess is big enough.

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def count_upto(limit):
            total = 0
            for row in range(1, m + 1):
                total += min(limit // row, n)
            return total

        low, high = 1, m * n
        while low < high:
            middle = (low + high) // 2
            if count_upto(middle) >= k:
                high = middle
            else:
                low = middle + 1
        return low
