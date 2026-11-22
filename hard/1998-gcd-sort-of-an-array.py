# LeetCode 1998. GCD Sort of an Array — Hard
# https://leetcode.com/problems/gcd-sort-of-an-array/
# Submission 2201299605 — Accepted, Python3
#
# My thinking: two spots can trade places exactly
# when a shared prime links them, so I join every
# index by its prime factors and check that each
# linked group already holds the right values.

from collections import defaultdict

class Solution:
    def gcdSort(self, nums: list[int]) -> bool:
        n = len(nums)
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb

        maxv = max(nums)
        spf = list(range(maxv + 1))
        for i in range(2, int(maxv ** 0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, maxv + 1, i):
                    if spf[j] == j:
                        spf[j] = i
        prime_to_first = {}
        for i, x in enumerate(nums):
            v = x
            primes = set()
            while v > 1:
                p = spf[v]
                primes.add(p)
                while v % p == 0:
                    v //= p
            for p in primes:
                if p in prime_to_first:
                    union(i, prime_to_first[p])
                else:
                    prime_to_first[p] = i
        groups = defaultdict(list)
        for i in range(n):
            groups[find(i)].append(i)
        srt = sorted(nums)
        for idxs in groups.values():
            if sorted(nums[i] for i in idxs) != sorted(srt[i] for i in idxs):
                return False
        return True
