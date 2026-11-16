# LeetCode 263. Ugly Number — Easy
# https://leetcode.com/problems/ugly-number/
# Submission 2197459331 — Accepted, Python3
#
# My thinking: an ugly number only has 2, 3 and 5 as
# prime factors. So I divide the number by 2, 3 and
# 5 as many times as I can. If what is left is 1,
# there was nothing else in it — it is ugly. Zero
# and negatives are not.

class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        for p in (2, 3, 5):
            while n % p == 0:
                n //= p
        return n == 1
