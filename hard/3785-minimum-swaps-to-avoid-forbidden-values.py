# LeetCode 3785. Minimum Swaps to Avoid Forbidden Values — Hard
# https://leetcode.com/problems/minimum-swaps-to-avoid-forbidden-values/
# Submission 2203177702 — Accepted, Python3
from collections import Counter
from typing import List


class Solution:
    def minSwaps(self, nums: List[int], forbidden: List[int]) -> int:
        # My thinking: the multiset of values never changes, so
        # first check the rearrangement is even possible. All
        # copies of a value v must land on positions that do
        # not forbid v, so we need count(v) <= n - count of
        # positions forbidding v for every v; that one check
        # per value is also enough, because any two different
        # values together can use every position between them.
        # With that settled, look at the bad positions, where
        # nums[i] == forbidden[i]. Swapping two bad positions
        # holding different values fixes both at once, so
        # ceil(bad / 2) swaps suffice unless one value
        # dominates the bad spots: if maxBad copies of the same
        # value are bad, each of the extras beyond the other
        # bad spots needs its own swap with a good position,
        # which costs maxBad swaps. The answer is the larger
        # of the two counts.
        n = len(nums)
        total = Counter(nums)
        forbids = Counter(forbidden)
        for v, c in total.items():
            if c > n - forbids.get(v, 0):
                return -1
        bad = 0
        bad_count = Counter()
        for a, b in zip(nums, forbidden):
            if a == b:
                bad += 1
                bad_count[a] += 1
        if bad == 0:
            return 0
        return max((bad + 1) // 2, max(bad_count.values()))
