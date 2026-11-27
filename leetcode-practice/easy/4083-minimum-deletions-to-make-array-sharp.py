# 4083. Minimum Deletions to Make Array Sharp (Easy)
# https://leetcode.com/problems/minimum-deletions-to-make-array-sharp/
# Submission 2200103730 — Accepted, Python3
class Solution:
    def minDeletions(self, nums: list[int]) -> int:
        # My thinking: two neighbours are bad only
        # when they are equal, so I keep each number
        # that differs from the last one I kept and
        # drop the repeats. The drops are the answer.
        kept = 0
        last = None
        for x in nums:
            if x != last:
                kept += 1
                last = x
        return len(nums) - kept
