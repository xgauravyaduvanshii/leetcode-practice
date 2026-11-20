# 4097. Minimum Value of Merged Integers (Easy)
# https://leetcode.com/problems/minimum-value-of-merged-integers/
# Submission 2200105031 — Accepted, Python3
class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        # My thinking: I glue each neighbouring pair
        # of numbers into one — the first one's digits
        # followed by the second's — and keep the
        # smallest result.
        return min(
            int(str(nums[i]) + str(nums[i + 1])) for i in range(0, len(nums), 2)
        )
