# LeetCode 2761. Prime Pairs With Target Sum — Medium
# https://leetcode.com/problems/prime-pairs-with-target-sum/
# Submission 2205242691 — Accepted, Python3
#
# My thinking: sieve up to n, then for every prime p up to
# n/2 check whether n-p is also prime. Scanning p in
# increasing order gives the pairs already sorted by x.
class Solution:
    def findPrimePairs(self, n: int) -> list[list[int]]:
        is_prime = [True] * (n + 1)
        if n >= 0:
            is_prime[0] = False
        if n >= 1:
            is_prime[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
        return [[p, n - p] for p in range(2, n // 2 + 1) if is_prime[p] and is_prime[n - p]]
