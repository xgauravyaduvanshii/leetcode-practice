# LeetCode 3435. Frequencies of Shortest Supersequences — Hard
# https://leetcode.com/problems/frequencies-of-shortest-supersequences/
# Submission 2202530666 — Accepted 808/808, Python3
from functools import lru_cache
from typing import List


class Solution:
    def supersequences(self, words: List[str]) -> List[List[int]]:
        # My thinking: a shortest supersequence uses each letter
        # once, except some letters twice. Take the order of
        # first appearances: a letter must be doubled exactly
        # when some word points into it from a letter that first
        # appears later (or the word is a double like "aa").
        # So I pick the first-appearance order that doubles the
        # fewest letters — a DP over subsets of the at most 16
        # letters — then collect every doubled set any cheapest
        # order produces, and report each as a frequency array.
        letters = sorted({ch for w in words for ch in w})
        m = len(letters)
        idx = {ch: i for i, ch in enumerate(letters)}
        in_mask = [0] * m
        self_loop = [False] * m
        for w in words:
            a, b = idx[w[0]], idx[w[1]]
            if a == b:
                self_loop[a] = True
            else:
                in_mask[b] |= 1 << a
        full = (1 << m) - 1
        INF = 10 ** 9
        # h[S] = fewest doubled letters needed to place the set
        # S, given the letters outside S are already placed.
        h = [INF] * (1 << m)
        h[0] = 0
        for S in range(1, 1 << m):
            placed = full ^ S
            best = INF
            sub = S
            while sub:
                lsb = sub & -sub
                v = lsb.bit_length() - 1
                sub ^= lsb
                bad = 1 if (self_loop[v] or (in_mask[v] & ~placed) != 0) else 0
                best = min(best, bad + h[S ^ lsb])
            h[S] = best

        # g[S] = doubled-letter masks achievable by a cheapest
        # ordering of the set S.
        @lru_cache(maxsize=None)
        def g(S):
            if S == 0:
                return frozenset([0])
            placed = full ^ S
            out = set()
            sub = S
            while sub:
                lsb = sub & -sub
                v = lsb.bit_length() - 1
                sub ^= lsb
                bad = 1 if (self_loop[v] or (in_mask[v] & ~placed) != 0) else 0
                if bad + h[S ^ lsb] == h[S]:
                    for r in g(S ^ lsb):
                        out.add(r | (lsb if bad else 0))
            return frozenset(out)

        ans = []
        for rmask in g(full):
            freq = [0] * 26
            for i, ch in enumerate(letters):
                freq[ord(ch) - 97] = 2 if (rmask >> i) & 1 else 1
            ans.append(freq)
        return ans
