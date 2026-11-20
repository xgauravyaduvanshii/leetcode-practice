# 507. Perfect Number (Easy)
# https://leetcode.com/problems/perfect-number/
# Submission 2199958640 — Accepted, Python3
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        # My thinking: a perfect number equals the sum of
        # its proper divisors. Divisors come in pairs, so
        # I only need to check up to the square root and
        # add both members of each pair I find.
        if num <= 1:
            return False
        total = 1
        i = 2
        while i * i <= num:
            if num % i == 0:
                total += i
                if i * i != num:
                    total += num // i
            i += 1
        return total == num
