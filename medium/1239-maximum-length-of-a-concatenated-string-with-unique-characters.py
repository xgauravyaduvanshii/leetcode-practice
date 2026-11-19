# LeetCode 1239. Maximum Length of a Concatenated String with Unique Characters — Medium
# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
# Submission 2199017508 — Accepted, Python3
#
# My thinking: each word becomes a bit mask of
# its letters, and words with a repeated letter
# are useless. I try every combination of
# masks that share no bits and keep the longest.

from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        masks = []
        for word in arr:
            mask = 0
            for ch in word:
                bit = 1 << (ord(ch) - 97)
                if mask & bit:
                    break
                mask |= bit
            else:
                masks.append(mask)
        best = 0

        def build(i, used):
            nonlocal best
            best = max(best, bin(used).count("1"))
            for j in range(i, len(masks)):
                if used & masks[j] == 0:
                    build(j + 1, used | masks[j])

        build(0, 0)
        return best
