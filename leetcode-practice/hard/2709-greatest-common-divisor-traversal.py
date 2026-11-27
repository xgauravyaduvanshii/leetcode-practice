# LeetCode 2709. Greatest Common Divisor Traversal — Hard
# https://leetcode.com/problems/greatest-common-divisor-traversal/
# Submission 2201872136 — Accepted, Python3
#
# My thinking: two numbers can meet
# only through a prime they share, so
# I tie every number to its primes and
# let the primes tie the numbers to
# each other — if every number ends up
# in one family, the whole array is
# connected. A 1 has no prime, so it
# stands alone.

class Solution:
    def canTraverseAllPairs(self, nums: list[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        if any(x == 1 for x in nums):
            return False
        mx = max(nums)
        spf = list(range(mx + 1))
        for i in range(2, int(mx ** 0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, mx + 1, i):
                    if spf[j] == j:
                        spf[j] = i
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

        first = {}
        for i, x in enumerate(nums):
            primes = set()
            while x > 1:
                p = spf[x]
                primes.add(p)
                while x % p == 0:
                    x //= p
            for p in primes:
                if p in first:
                    union(i, first[p])
                else:
                    first[p] = i
        root = find(0)
        return all(find(i) == root for i in range(n))
