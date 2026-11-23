# LeetCode 2122. Recover the Original Array — Hard
# https://leetcode.com/problems/recover-the-original-array/
# Submission 2201579611 — Accepted, Python3
#
# My thinking: the smallest number left must
# be some original minus k — a plus-k twin
# would leave its smaller minus-k partner
# behind — so I take the smallest, pair it
# with the number 2k above it, and keep going.

from collections import Counter


class Solution:
    def recoverArray(self, nums: list[int], k: int) -> list[int]:
        counts = Counter(nums)
        ans = []
        for x in sorted(counts):
            while counts[x] > 0:
                counts[x] -= 1
                counts[x + 2 * k] -= 1
                ans.append(x + k)
        return ans
