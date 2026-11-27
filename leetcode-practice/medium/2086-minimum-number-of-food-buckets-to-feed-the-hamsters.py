# LeetCode 2086. Minimum Number of Food Buckets to Feed the Hamsters — Medium
# https://leetcode.com/problems/minimum-number-of-food-buckets-to-feed-the-hamsters/
# Submission 2204401156 — Accepted, Python3
#
# My thinking: I go left to right, and for each hamster I first check
# whether a bucket placed earlier already feeds it. If not, I prefer
# placing a bucket on the empty cell to its right, because that cell
# can also feed the next hamster; only if the right cell is blocked do
# I use the left one. If neither side has an empty cell, the hamster
# can never be fed and the answer is -1.
class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        n = len(hamsters)
        placed = [False] * n
        buckets = 0
        for i, ch in enumerate(hamsters):
            if ch != 'H':
                continue
            if i > 0 and placed[i - 1]:
                continue
            if i + 1 < n and hamsters[i + 1] == '.':
                placed[i + 1] = True
                buckets += 1
            elif i > 0 and hamsters[i - 1] == '.':
                placed[i - 1] = True
                buckets += 1
            else:
                return -1
        return buckets
