# 3726. Remove Zeros in Decimal Representation (Easy)
# https://leetcode.com/problems/remove-zeros-in-decimal-representation/
# Submission 2200055997 — Accepted, Python3
class Solution:
    def removeZeros(self, n: int) -> int:
        # My thinking: drop every zero digit from the
        # number and read what is left as a number
        # again.
        return int(str(n).replace("0", ""))
