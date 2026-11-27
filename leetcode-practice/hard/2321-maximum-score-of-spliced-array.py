# LeetCode 2321. Maximum Score Of Spliced Array — Hard
# https://leetcode.com/problems/maximum-score-of-spliced-array/
# Submission 2201675968 — Accepted, Python3
#
# My thinking: swapping one stretch adds
# the other array's gain and takes away
# mine, so I run Kadane on the difference
# both ways and keep whichever side ends
# up richer.

class Solution:
    def maximumsSplicedArray(self, nums1: list[int], nums2: list[int]) -> int:
        def max_gain(diff):
            best = 0
            cur = 0
            for d in diff:
                cur = max(0, cur + d)
                best = max(best, cur)
            return best

        sum1 = sum(nums1)
        sum2 = sum(nums2)
        diff1 = [b - a for a, b in zip(nums1, nums2)]
        diff2 = [a - b for a, b in zip(nums1, nums2)]
        return max(sum1 + max_gain(diff1), sum2 + max_gain(diff2))
