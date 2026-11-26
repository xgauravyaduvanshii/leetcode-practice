# LeetCode 3943. Number of Pairs After Increment — Hard
# https://leetcode.com/problems/number-of-pairs-after-increment/
# Submission 2203440179 — Accepted, Python3
from collections import Counter
from typing import List


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        # My thinking: nums1 has at most 5 entries, so a type 2
        # query only needs the count of each of a few target
        # values in nums2 — but the range adds keep moving those
        # values. Split nums2 into blocks of about 350: each
        # block keeps a frequency map of its raw values plus a
        # lazy add shared by the whole block, so a range add
        # touches at most two partial blocks (rebuild their
        # maps) and just bumps the lazy tag of the full blocks
        # in between. A type 2 query then reads, for each value
        # in nums1, the block maps at (tot - value - lazy),
        # weighted by how many times that value occurs in
        # nums1 — pairs count per index, not per distinct value.
        counts1 = Counter(nums1)
        a = list(nums2)
        n = len(a)
        B = 350
        nb = (n + B - 1) // B
        lazy = [0] * nb
        cnt = [Counter(a[b * B:(b + 1) * B]) for b in range(nb)]

        def push(b: int) -> None:
            if lazy[b]:
                lz = lazy[b]
                for i in range(b * B, min((b + 1) * B, n)):
                    a[i] += lz
                lazy[b] = 0

        def rebuild(b: int) -> None:
            cnt[b] = Counter(a[b * B:(b + 1) * B])

        ans = []
        for q in queries:
            if q[0] == 1:
                _, x, y, val = q
                bl, br = x // B, y // B
                if bl == br:
                    push(bl)
                    for i in range(x, y + 1):
                        a[i] += val
                    rebuild(bl)
                else:
                    push(bl)
                    for i in range(x, (bl + 1) * B):
                        a[i] += val
                    rebuild(bl)
                    push(br)
                    for i in range(br * B, y + 1):
                        a[i] += val
                    rebuild(br)
                    for b in range(bl + 1, br):
                        lazy[b] += val
            else:
                tot = q[1]
                total = 0
                for v, mult in counts1.items():
                    need = tot - v
                    for b in range(nb):
                        total += mult * cnt[b].get(need - lazy[b], 0)
                ans.append(total)
        return ans
