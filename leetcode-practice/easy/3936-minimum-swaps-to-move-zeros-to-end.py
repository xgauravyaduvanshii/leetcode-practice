# 3936. Minimum Swaps to Move Zeros to End (Easy)
# https://leetcode.com/problems/minimum-swaps-to-move-zeros-to-end/
# Submission 2200089006 — Accepted, Python3
class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        # My thinking: the non-zero numbers will fill
        # the front of the array. Every zero sitting in
        # that front stretch needs exactly one swap
        # with a non-zero from the back.
        m = sum(1 for x in nums if x != 0)
        return sum(1 for x in nums[:m] if x == 0)
