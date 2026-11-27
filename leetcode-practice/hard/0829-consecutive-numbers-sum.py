# LeetCode 829. Consecutive Numbers Sum — Hard
# https://leetcode.com/problems/consecutive-numbers-sum/
# Submission 2198680363 — Accepted, Python3
#
# My thinking: writing n as a sum of k consecutive
# numbers works exactly when k divides n with the
# right parity — and that turns out to match the odd
# divisors of n one-to-one. So I strip the factors of
# two and count the divisors of what is left.

class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        count = 0
        while n % 2 == 0:
            n //= 2
        divisor = 1
        while divisor * divisor <= n:
            if n % divisor == 0:
                count += 1
                if divisor * divisor != n:
                    count += 1
            divisor += 2
        return count
