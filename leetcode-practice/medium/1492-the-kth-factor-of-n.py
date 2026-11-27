# LeetCode 1492. The kth Factor of n — Medium
# https://leetcode.com/problems/the-kth-factor-of-n/
# Submission 2199863539 — Accepted, Python3
#
# My thinking: factors come in pairs around
# the square root. I collect both halves,
# sort them, and pick the kth — or -1 when
# there are fewer than k.

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                factors.append(i)
                if i * i != n:
                    factors.append(n // i)
        factors.sort()
        return factors[k - 1] if k <= len(factors) else -1
