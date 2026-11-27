# LeetCode 4081. Prime Subset Selection II — Hard
# https://leetcode.com/problems/prime-subset-selection-ii/
# Submission 2203695607 — Accepted, Python3


class Solution:
    def maxPrimeSubset(self, n: int, s: int) -> list[int]:
        # My thinking: first sieve out all primes up to n.
        # Then it is a subset-sum problem over those primes:
        # we want the largest sum <= s that a subset of the
        # primes can reach, and among the subsets reaching
        # that sum, the one with the fewest primes. dp[i][t]
        # = the smallest number of primes among primes[i:]
        # whose sum is exactly t (INF if impossible). Fill
        # it backwards: for each prime p, either skip it or
        # take it (cost 1 + the best for t - p). The best
        # sum is the largest t <= s with dp[0][t] finite.
        # Then walk the primes in increasing order and take
        # a prime whenever the remaining sum can still be
        # reached with one fewer prime, which rebuilds a
        # smallest subset with that sum.
        is_prime = [True] * (n + 1)
        is_prime[0] = False
        is_prime[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
        primes = [i for i in range(2, n + 1) if is_prime[i]]
        m = len(primes)
        INF = 10 ** 9
        dp = [[INF] * (s + 1) for _ in range(m + 1)]
        dp[m][0] = 0
        for i in range(m - 1, -1, -1):
            p = primes[i]
            row = dp[i]
            nxt = dp[i + 1]
            for t in range(s + 1):
                best = nxt[t]
                if t >= p and nxt[t - p] + 1 < best:
                    best = nxt[t - p] + 1
                row[t] = best
        best_sum = -1
        for t in range(s, 0, -1):
            if dp[0][t] < INF:
                best_sum = t
                break
        if best_sum == -1:
            return []
        ans = []
        rem = best_sum
        need = dp[0][best_sum]
        for i in range(m):
            if need == 0:
                break
            p = primes[i]
            if p <= rem and dp[i + 1][rem - p] == need - 1:
                ans.append(p)
                rem -= p
                need -= 1
        return ans
