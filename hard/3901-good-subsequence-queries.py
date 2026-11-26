# LeetCode 3901. Good Subsequence Queries — Hard
# https://leetcode.com/problems/good-subsequence-queries/
# Submission 2203369148 — Accepted, Python3
from math import gcd
from typing import List


class Solution:
    def countGoodSubseq(self, nums: List[int], p: int, queries: List[List[int]]) -> int:
        # My thinking: a subsequence has gcd exactly p only
        # when every element is divisible by p, so divide
        # those elements by p and ask for gcd exactly 1.
        # Let m be how many elements are divisible by p.
        # When m < n, taking all of them is a good
        # subsequence exactly when their gcd is 1, and no
        # subsequence can have gcd 1 when that gcd is above
        # 1, since the gcd of any subset is a multiple of
        # the gcd of the whole divisible set. When m == n
        # the full array is too long, so we need a proper
        # subsequence with gcd 1 — one exists exactly when
        # some leave-one-out gcd is 1. That fails for every
        # element only when each element is the unique one
        # not divisible by some prime: for a prime q dividing
        # all but one element, that element is "covered".
        # So keep, for every prime q, how many divisible
        # elements it divides (updated from the prime
        # factors of the old and new value only), plus the
        # set of primes dividing all but one element with
        # their unique uncovered index — found with a
        # segment-tree search, since a prime divides a
        # segment's gcd exactly when it divides every
        # element of the segment. The segment tree also
        # carries the gcd of all divisible values (0 stands
        # for not divisible). A query is good when that gcd
        # is 1 and either m < n or not every index is
        # covered.
        n = len(nums)
        max_v = 50000
        spf = list(range(max_v + 1))
        for i in range(2, int(max_v ** 0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, max_v + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        def prime_factors(x):
            out = []
            while x > 1:
                q = spf[x]
                out.append(q)
                while x % q == 0:
                    x //= q
            return out

        a = [x // p if x % p == 0 else 0 for x in nums]
        m = sum(1 for v in a if v > 0)
        size = 1
        while size < n:
            size *= 2
        tree = [0] * (2 * size)
        for i, v in enumerate(a):
            tree[size + i] = v
        for i in range(size - 1, 0, -1):
            tree[i] = gcd(tree[2 * i], tree[2 * i + 1])

        def point_update(i, v):
            j = size + i
            tree[j] = v
            j //= 2
            while j:
                tree[j] = gcd(tree[2 * j], tree[2 * j + 1])
                j //= 2

        def find_not_div(q):
            # First index whose value is not divisible by q;
            # -1 when every value is divisible by q. Only
            # called while all values are divisible by p.
            if tree[1] % q == 0:
                return -1
            j = 1
            while j < size:
                j *= 2
                if tree[j] % q == 0:
                    j += 1
            idx = j - size
            return idx if idx < n else -1

        # e[q]: how many divisible elements are divisible by q.
        e = [0] * (max_v + 1)
        for v in a:
            if v > 0:
                for q in prime_factors(v):
                    e[q] += 1
        # u[q]: the unique index not divisible by q, for each
        # prime q dividing all but one element (m == n only).
        # freqd[idx]: how many such primes cover idx.
        u = {}
        freqd = {}

        def rebuild():
            u.clear()
            freqd.clear()
            # A prime dividing all but one element must divide
            # a[0] or a[1]: its unique non-multiple is a single
            # index, so it divides at least one of the first
            # two elements. Those prime factors are the only
            # candidates for the covered set.
            cands = set(prime_factors(a[0])) | set(prime_factors(a[1]))
            for q in cands:
                if e[q] == n - 1:
                    idx = find_not_div(q)
                    u[q] = idx
                    freqd[idx] = freqd.get(idx, 0) + 1

        def enter(q, idx):
            u[q] = idx
            freqd[idx] = freqd.get(idx, 0) + 1

        def leave(q):
            idx = u.pop(q)
            freqd[idx] -= 1
            if freqd[idx] == 0:
                del freqd[idx]

        if m == n:
            rebuild()

        ans = 0
        for ind, val in queries:
            old = a[ind]
            new = val // p if val % p == 0 else 0
            if old != new:
                old_div = old > 0
                new_div = new > 0
                point_update(ind, new)
                a[ind] = new
                if old_div and not new_div:
                    m -= 1
                    for q in prime_factors(old):
                        e[q] -= 1
                    if m + 1 == n:
                        u.clear()
                        freqd.clear()
                elif new_div and not old_div:
                    m += 1
                    for q in prime_factors(new):
                        e[q] += 1
                    if m == n:
                        rebuild()
                else:
                    old_primes = set(prime_factors(old))
                    new_primes = set(prime_factors(new))
                    if m == n:
                        for q in old_primes - new_primes:
                            if e[q] == n:
                                enter(q, ind)
                            elif e[q] == n - 1:
                                leave(q)
                            e[q] -= 1
                        for q in new_primes - old_primes:
                            if e[q] == n - 1:
                                leave(q)
                            elif e[q] == n - 2:
                                enter(q, find_not_div(q))
                            e[q] += 1
                    else:
                        for q in old_primes - new_primes:
                            e[q] -= 1
                        for q in new_primes - old_primes:
                            e[q] += 1
            if m > 0 and tree[1] == 1 and (m < n or len(freqd) < n):
                ans += 1
        return ans
