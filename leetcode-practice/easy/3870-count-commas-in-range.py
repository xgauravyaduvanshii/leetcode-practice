# 3870. Count Commas in Range (Easy)
# https://leetcode.com/problems/count-commas-in-range/
# Submission 2200083125 — Accepted, Python3
class Solution:
    def countCommas(self, n: int) -> int:
        # My thinking: a number with d digits carries
        # a comma after every three digits from the
        # right — so I add up each digit-length block
        # separately.
        total = 0
        start = 1
        digits = 1
        while start <= n:
            end = min(n, 10 ** digits - 1)
            total += (end - start + 1) * ((digits - 1) // 3)
            start = 10 ** digits
            digits += 1
        return total
