# LeetCode 3953. Maximum Score with Co-Prime Element — Hard
# https://leetcode.com/problems/maximum-score-with-co-prime-element/
# Submission 2203450868 — Accepted, Python3
from typing import List


class Solution:
    def maxScore(self, nums: List[int], maxVal: int) -> int:
        # My thinking: pick the selected value v and one index
        # to hold it. Every other element sharing a factor with
        # v must be changed, and changing it to 1 always works,
        # so the cost is fixed by v: if v already sits in the
        # array we keep that copy (cost = bad(v) - 1, the copy
        # itself being counted as bad when v > 1); if v is absent
        # we change some bad element into v instead (cost =
        # bad(v)), or pay 1 with no bad element at all. The
        # selected value may also be an untouched element larger
        # than maxVal — only changed values must fit under
        # maxVal. bad(v) is n minus the count of elements
        # co-prime to v, and that count comes from Mobius
        # inversion over v's divisors: sum mu(d) * (multiples
        # of d in nums), computed for all v at once with a
        # sieve over multiples.
        n = len(nums)
        maxN = max(nums) if nums else 0
        lim = max(maxVal, maxN)
        freq = [0] * (lim + 1)
        for v in nums:
            freq[v] += 1
        cntMult = [0] * (lim + 1)
        for d in range(1, lim + 1):
            s = 0
            for mult in range(d, lim + 1, d):
                s += freq[mult]
            cntMult[d] = s
        mu = [0] * (lim + 1)
        mu[1] = 1
        primes = []
        is_comp = [False] * (lim + 1)
        for i in range(2, lim + 1):
            if not is_comp[i]:
                primes.append(i)
                mu[i] = -1
            for p in primes:
                if i * p > lim:
                    break
                is_comp[i * p] = True
                if i % p == 0:
                    mu[i * p] = 0
                    break
                mu[i * p] = -mu[i]
        coprime = [0] * (lim + 1)
        for d in range(1, lim + 1):
            if mu[d] == 0 or cntMult[d] == 0:
                continue
            md = mu[d]
            for m in range(d, lim + 1, d):
                coprime[m] += md * cntMult[d]
        ans = 0
        for v in range(1, maxVal + 1):
            bad = n - coprime[v]
            if v == 1:
                score = 1 if freq[1] > 0 else 0
            elif freq[v] > 0:
                score = v - bad + 1
            else:
                score = v - bad if bad > 0 else v - 1
            if score > ans:
                ans = score
        for v in set(nums):
            if v <= maxVal or v == 1:
                continue
            bad = n - coprime[v]
            score = v - bad + 1
            if score > ans:
                ans = score
        return ans
