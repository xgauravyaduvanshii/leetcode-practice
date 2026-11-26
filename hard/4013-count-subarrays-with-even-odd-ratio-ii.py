# LeetCode 4013. Count Subarrays With Even Odd Ratio II — Hard
# https://leetcode.com/problems/count-subarrays-with-even-odd-ratio-ii/
# Submission 2203510157 — Accepted, Python3
from typing import List


class Solution:
    def countRatioSubarrays(self, nums: List[int], a: int, b: int) -> int:
        # My thinking: a subarray with x evens and y odds
        # is valid exactly when y > 0 and b*x <= a*y.
        # Give each element a score: +b for an even element,
        # -a for an odd one. Then a subarray's score is
        # b*x - a*y, so it is valid exactly when its score
        # is at most 0. An all-even subarray can never
        # qualify anyway (its score is positive), so the
        # y > 0 condition needs no separate check. With
        # prefix sums P, a subarray is valid exactly when
        # P[l] >= P[r] for l < r. Counting such pairs is a
        # classic inversion count: sweep the prefix sums
        # from left to right, keeping them in a Fenwick
        # tree over compressed coordinates, and for each
        # new prefix add how many earlier ones are at
        # least as large.
        prefs = [0]
        s = 0
        for x in nums:
            s += b if x % 2 == 0 else -a
            prefs.append(s)
        vals = sorted(set(prefs))
        rank = {v: i + 1 for i, v in enumerate(vals)}
        bit = [0] * (len(vals) + 2)

        def bit_add(i: int, d: int) -> None:
            while i < len(bit):
                bit[i] += d
                i += i & -i

        def bit_sum(i: int) -> int:
            total = 0
            while i:
                total += bit[i]
                i -= i & -i
            return total

        ans = 0
        seen = 0
        for p in prefs:
            i = rank[p]
            ans += seen - bit_sum(i - 1)
            bit_add(i, 1)
            seen += 1
        return ans
