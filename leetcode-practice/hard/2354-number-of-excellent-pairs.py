# LeetCode 2354. Number of Excellent Pairs — Hard
# https://leetcode.com/problems/number-of-excellent-pairs/
# Submission 2201695740 — Accepted, Python3
#
# My thinking: the bits of an OR plus the
# bits of an AND are just the bits of both
# numbers together — so a pair is excellent
# when the two popcounts add up to k, and
# I count ordered pairs by popcount.

class Solution:
    def countExcellentPairs(self, nums: list[int], k: int) -> int:
        freq = {}
        for x in set(nums):
            c = bin(x).count('1')
            freq[c] = freq.get(c, 0) + 1
        ans = 0
        for a, fa in freq.items():
            for b, fb in freq.items():
                if a + b >= k:
                    ans += fa * fb
        return ans
