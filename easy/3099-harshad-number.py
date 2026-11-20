# 3099. Harshad Number (Easy)
# https://leetcode.com/problems/harshad-number/
# Submission 2199975091 — Accepted, Python3
class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        # My thinking: add the digits of the number. If
        # the number divides evenly by that sum, it is a
        # Harshad number and the sum is the answer —
        # otherwise the answer is -1.
        digit_sum = sum(int(d) for d in str(x))
        return digit_sum if x % digit_sum == 0 else -1
