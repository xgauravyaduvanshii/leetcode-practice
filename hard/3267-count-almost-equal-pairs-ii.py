# LeetCode 3267. Count Almost Equal Pairs II — Hard
# https://leetcode.com/problems/count-almost-equal-pairs-ii/
# Submission 2202169532 — Accepted, Python3
#
# My thinking: two numbers can only become
# equal if their non-zero digits match, so I
# group numbers by their sorted non-zero digits.
# Inside a group, every number reaches only a
# handful of values with at most two digit swaps
# (leading zeros allowed), so I generate those
# permutations and count the matching pairs,
# counting each pair once by value order.

from collections import Counter
from typing import List


class Solution:
    def countPairs(self, nums: List[int]) -> int:
        freq = Counter(nums)
        vals = list(freq)
        length = {v: len(str(v)) for v in vals}
        groups = {}
        for v in vals:
            sig = tuple(sorted(d for d in str(v) if d != '0'))
            groups.setdefault(sig, []).append(v)
        ans = sum(f * (f - 1) // 2 for f in freq.values())
        perms_by_len = {}

        def get_perms(L):
            if L in perms_by_len:
                return perms_by_len[L]
            swaps = [(i, j) for i in range(L) for j in range(i + 1, L)]
            choices = [(None, None)] + swaps
            perms = set()
            for a in choices:
                for b in choices:
                    p = list(range(L))
                    if a[0] is not None:
                        p[a[0]], p[a[1]] = p[a[1]], p[a[0]]
                    if b[0] is not None:
                        p[b[0]], p[b[1]] = p[b[1]], p[b[0]]
                    perms.add(tuple(p))
            perms_by_len[L] = list(perms)
            return perms_by_len[L]

        for group in groups.values():
            if len(group) < 2:
                continue
            group_set = set(group)
            for v in group:
                s = str(v)
                L = len(s)
                perms = get_perms(L)
                v2 = set()
                for perm in perms:
                    t = ''.join(map(s.__getitem__, perm))
                    v2.add(int(t))
                for w in v2 & group_set:
                    if w == v:
                        continue
                    if length[w] < L:
                        ans += freq[v] * freq[w]
                    elif length[w] == L and w > v:
                        ans += freq[v] * freq[w]
        return ans
