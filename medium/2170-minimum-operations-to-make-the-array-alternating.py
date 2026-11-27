# LeetCode 2170. Minimum Operations to Make the Array Alternating — Medium
# https://leetcode.com/problems/minimum-operations-to-make-the-array-alternating/
# Submission 2204485085 — Accepted, Python3
#
# My thinking: in an alternating array all even positions share one
# value and all odd positions share a different one, so I want to keep
# as many elements as possible. I count the most frequent value on the
# even positions and on the odd positions, try the top two of each side
# so the two chosen values differ, and the answer is the array length
# minus the most elements I can keep unchanged.
class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        from collections import Counter
        even = Counter(nums[0::2])
        odd = Counter(nums[1::2])
        even_top = even.most_common(2) + [(0, 0), (0, 0)]
        odd_top = odd.most_common(2) + [(0, 0), (0, 0)]
        best_keep = 0
        for v1, c1 in even_top[:2]:
            for v2, c2 in odd_top[:2]:
                if v1 != v2 and c1 + c2 > best_keep:
                    best_keep = c1 + c2
        return len(nums) - best_keep
