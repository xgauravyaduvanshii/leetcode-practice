# 3536. Maximum Product of Two Digits (Easy)
# https://leetcode.com/problems/maximum-product-of-two-digits/
# Submission 2200026573 — Accepted, Python3
class Solution:
    def maxProduct(self, n: int) -> int:
        # My thinking: the biggest product comes from
        # the two biggest digits, so I pick the two
        # largest digits and multiply them.
        digits = sorted((int(d) for d in str(n)), reverse=True)
        return digits[0] * digits[1]
