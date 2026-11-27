# LeetCode 3636. Threshold Majority Queries — Hard
# https://leetcode.com/problems/threshold-majority-queries/
# Submission 2202924307 — Accepted, Python3
from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def thresholdMajorityQueries(
        self, nums: List[int], queries: List[List[int]]
    ) -> List[int]:
        # My thinking: the answer to a query is the mode of the
        # range (highest frequency, smallest on a tie) as long as
        # its frequency reaches the threshold, else -1. A range
        # mode is always either the mode of the fully covered
        # middle blocks or one of the elements sitting in the two
        # partial edge blocks, so I precompute the mode of every
        # block pair once and then score only those few candidates
        # per query, counting each one exactly with binary search
        # on its sorted positions list.
        n = len(nums)
        pos = {}
        for i, v in enumerate(nums):
            pos.setdefault(v, []).append(i)

        # Split nums into blocks of about sqrt(n).
        B = max(1, int(n ** 0.5))
        nb = (n + B - 1) // B
        block_of = [i // B for i in range(n)]

        # mode_pair[i][j] = mode (smallest on ties) of blocks i..j.
        mode_pair = [[0] * nb for _ in range(nb)]
        for i in range(nb):
            freq = {}
            best_val = 0
            best_freq = 0
            for j in range(i, nb):
                for k in range(j * B, min((j + 1) * B, n)):
                    v = nums[k]
                    c = freq.get(v, 0) + 1
                    freq[v] = c
                    if c > best_freq or (c == best_freq and v < best_val):
                        best_freq = c
                        best_val = v
                mode_pair[i][j] = best_val

        ans = []
        for l, r, threshold in queries:
            bl, br = block_of[l], block_of[r]
            if bl == br:
                # Tiny range: count directly.
                freq = {}
                best_val = -1
                best_freq = 0
                for k in range(l, r + 1):
                    v = nums[k]
                    c = freq.get(v, 0) + 1
                    freq[v] = c
                    if c > best_freq or (c == best_freq and v < best_val):
                        best_freq = c
                        best_val = v
                ans.append(best_val if best_freq >= threshold else -1)
                continue

            candidates = set()
            if bl + 1 <= br - 1:
                candidates.add(mode_pair[bl + 1][br - 1])
            for k in range(l, (bl + 1) * B):
                candidates.add(nums[k])
            for k in range(br * B, r + 1):
                candidates.add(nums[k])

            best_val = -1
            best_freq = 0
            for v in candidates:
                p = pos[v]
                c = bisect_right(p, r) - bisect_left(p, l)
                if c > best_freq or (c == best_freq and v < best_val):
                    best_freq = c
                    best_val = v
            ans.append(best_val if best_freq >= threshold else -1)
        return ans
