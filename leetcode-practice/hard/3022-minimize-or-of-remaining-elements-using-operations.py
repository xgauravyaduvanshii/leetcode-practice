# LeetCode 3022. Minimize OR of Remaining Elements Using Operations — Hard
# https://leetcode.com/problems/minimize-or-of-remaining-elements-using-operations/
# Submission 2201898811 — Accepted, Python3
#
# My thinking: I try to switch each bit
# off, from the highest down, keeping a
# bit off only when the array can really
# be merged to avoid it. To test a set of
# allowed bits, I cut the array greedily:
# a piece ends as soon as the AND of its
# numbers uses only allowed bits, since
# AND can only clear bits. Merging the
# pieces takes one operation less than
# the number of numbers, so a test passes
# when the greedy cut leaves few enough
# pieces for the k operations allowed.
# A leftover tail just joins the last
# piece, which costs the same total.

from typing import List


class Solution:
    def minOrAfterOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ALL = (1 << 30) - 1
        ans = 0
        for x in nums:
            ans |= x

        def can(target: int) -> bool:
            # Can the array be merged (at most k ops) so every
            # remaining number uses only bits set in target?
            cur = ALL
            pieces = 0
            for x in nums:
                cur &= x
                if cur & ~target == 0:
                    pieces += 1
                    cur = ALL
            # No cut at all means the whole array keeps a bad bit.
            if pieces == 0:
                return False
            # Merging into `pieces` pieces costs n - pieces ops
            # (a leftover tail joins the last piece for free in
            # the count, since AND only clears bits).
            return n - pieces <= k

        for bit in range(29, -1, -1):
            if ans & (1 << bit):
                if can(ans & ~(1 << bit)):
                    ans &= ~(1 << bit)
        return ans
