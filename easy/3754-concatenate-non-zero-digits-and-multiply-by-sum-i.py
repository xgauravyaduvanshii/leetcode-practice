# 3754. Concatenate Non-Zero Digits and Multiply by Sum I (Easy)
# https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/
# Submission 2200061697 — Accepted, Python3
class Solution:
    def sumAndMultiply(self, n: int) -> int:
        # My thinking: throw away the zeroes, read the
        # remaining digits as a new number, add its
        # digits up, and multiply the two.
        digits = [d for d in str(n) if d != "0"]
        x = int("".join(digits)) if digits else 0
        return x * sum(int(d) for d in str(x))
