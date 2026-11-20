# LeetCode 1806. Minimum Number of Operations to Reinitialize a Permutation — Medium
# https://leetcode.com/problems/minimum-number-of-operations-to-reinitialize-a-permutation/
# Submission 2199939850 — Accepted, Python3
#
# My thinking: the shuffle is fixed — even
# spots take from the first half, odd spots
# from the second. I just apply it until the
# permutation comes back to the start and
# count the steps.

class Solution:
    def reinitializePermutation(self, n: int) -> int:
        perm = list(range(n))
        steps = 0
        while True:
            steps += 1
            new = [0] * n
            for i in range(n):
                if i % 2 == 0:
                    new[i] = perm[i // 2]
                else:
                    new[i] = perm[n // 2 + (i - 1) // 2]
            perm = new
            if perm == list(range(n)):
                return steps
