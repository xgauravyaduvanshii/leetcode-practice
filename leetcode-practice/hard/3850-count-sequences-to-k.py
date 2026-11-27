# LeetCode 3850. Count Sequences to K — Hard
# https://leetcode.com/problems/count-sequences-to-k/
# Submission 2203293164 — Accepted, Python3
from collections import defaultdict
from typing import List


class Solution:
    def countSequences(self, nums: List[int], k: int) -> int:
        # My thinking: multiplying or dividing by nums[i] only
        # moves the exponents of 2, 3 and 5 in the value, since
        # every nums[i] is at most 6, so the final value is k
        # exactly when the three exponent sums match the
        # exponents of k — and if k has any other prime factor
        # the answer is 0 at once. Each element contributes
        # its exponent vector, its negation, or nothing, so I
        # split the array in half, enumerate all 3^10 choices
        # per half into maps from exponent triple to count, and
        # pair a triple from the first half with the matching
        # complement from the second.
        primes = (2, 3, 5)
        target = []
        for p in primes:
            e = 0
            while k % p == 0:
                k //= p
                e += 1
            target.append(e)
        if k != 1:
            return 0
        exps = []
        for v in nums:
            es = []
            for p in primes:
                e = 0
                while v % p == 0:
                    v //= p
                    e += 1
                es.append(e)
            exps.append(tuple(es))

        def half(es):
            counts = defaultdict(int)

            def rec(i, acc):
                if i == len(es):
                    counts[acc] += 1
                    return
                a = es[i]
                rec(i + 1, acc)
                rec(i + 1, tuple(x + y for x, y in zip(acc, a)))
                rec(i + 1, tuple(x - y for x, y in zip(acc, a)))

            rec(0, (0, 0, 0))
            return counts

        mid = len(exps) // 2
        first = half(exps[:mid])
        second = half(exps[mid:])
        target = tuple(target)
        ans = 0
        for acc, c in first.items():
            need = tuple(t - a for t, a in zip(target, acc))
            ans += c * second.get(need, 0)
        return ans
