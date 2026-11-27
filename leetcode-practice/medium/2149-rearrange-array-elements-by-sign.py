# LeetCode 2149. Rearrange Array Elements by Sign — Medium
# https://leetcode.com/problems/rearrange-array-elements-by-sign/
# Submission 2197615570 — Accepted, Python3
#
# My thinking: I split the numbers into positives and
# negatives, keeping their original order in each
# group. Then I weave the two lists together —
# positive, negative, positive, negative — which
# also preserves the relative order inside each
# group.

class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        pos = [x for x in nums if x > 0]
        neg = [x for x in nums if x < 0]
        result = []
        for p, n in zip(pos, neg):
            result.append(p)
            result.append(n)
        return result
