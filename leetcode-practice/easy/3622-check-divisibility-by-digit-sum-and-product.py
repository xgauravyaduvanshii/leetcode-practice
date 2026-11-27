# 3622. Check Divisibility by Digit Sum and Product (Easy)
# https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/
# Submission 2200033340 — Accepted, Python3
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        # My thinking: add up the digits and multiply
        # them too, then see whether the number divides
        # cleanly by the sum of those two.
        digits = [int(d) for d in str(n)]
        total = sum(digits)
        product = 1
        for d in digits:
            product *= d
        return n % (total + product) == 0
