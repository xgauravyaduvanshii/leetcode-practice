# LeetCode 3470. Permutations IV — Hard
# https://leetcode.com/problems/permutations-iv/
# Submission 2202656154 — Accepted 999/999, Python3
#
# My thinking: an alternating permutation must alternate odd and even, so
# once I pick a number the parity of every later slot is forced. I build
# the answer left to right, trying candidates in increasing order; for a
# candidate I count how many completions it leaves, which is (remaining
# odds)! times (remaining evens)! when the remaining counts exactly fill
# the forced odd and even slots, and 0 otherwise. If k is larger than that
# count I skip the whole block, otherwise I take the candidate and move on.
# A candidate whose parity matches the previous pick is never tried.

from math import factorial
from typing import List


class Solution:
    def permute(self, n: int, k: int) -> List[int]:
        odds = list(range(1, n + 1, 2))
        evens = list(range(2, n + 1, 2))

        def completions(rem_o, rem_e, nxt):
            need_o = need_e = 0
            p = nxt
            for _ in range(len(rem_o) + len(rem_e)):
                if p == 1:
                    need_o += 1
                else:
                    need_e += 1
                p = 1 - p
            if len(rem_o) != need_o or len(rem_e) != need_e:
                return 0
            return factorial(len(rem_o)) * factorial(len(rem_e))

        res = []
        rem_o, rem_e = odds, evens
        prev = None
        for _ in range(n):
            cands = sorted(rem_o + rem_e)
            if prev is not None:
                cands = [c for c in cands if c % 2 != prev]
            for c in cands:
                if c % 2 == 1:
                    no = [x for x in rem_o if x != c]
                    ne = rem_e
                else:
                    no = rem_o
                    ne = [x for x in rem_e if x != c]
                cnt = completions(no, ne, 1 - (c % 2))
                if k > cnt:
                    k -= cnt
                else:
                    res.append(c)
                    rem_o, rem_e = no, ne
                    prev = c % 2
                    break
            else:
                return []
        return res
