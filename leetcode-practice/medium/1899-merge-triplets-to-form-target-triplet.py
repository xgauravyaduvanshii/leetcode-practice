# LeetCode 1899. Merge Triplets to Form Target Triplet — Medium
# https://leetcode.com/problems/merge-triplets-to-form-target-triplet/
# Submission 2201151538 — Accepted, Python3
#
# My thinking: a triplet can only help if none of
# its numbers overshoots the target, and I need at
# least one kept triplet matching the target in
# each of the three slots.

class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        good = [t for t in triplets if all(t[i] <= target[i] for i in range(3))]
        return all(any(t[i] == target[i] for t in good) for i in range(3))
