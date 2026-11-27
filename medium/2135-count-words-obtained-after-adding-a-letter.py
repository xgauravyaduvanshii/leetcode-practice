# LeetCode 2135. Count Words Obtained After Adding a Letter — Medium
# https://leetcode.com/problems/count-words-obtained-after-adding-a-letter/
# Submission 2204470340 — Accepted, Python3
#
# My thinking: a target word counts if removing exactly one of its
# letters leaves a start word. Letter order does not matter, so I encode
# each word as a 26-bit mask of its letters and store the start masks in
# a set. For each target I try removing each set bit once and check
# whether the remaining mask is a start word.
class Solution:
    def wordCount(self, startWords: list[str], targetWords: list[str]) -> int:
        def mask(s):
            m = 0
            for ch in s:
                m |= 1 << (ord(ch) - 97)
            return m
        starts = {mask(w) for w in startWords}
        ans = 0
        for t in targetWords:
            m = mask(t)
            for i in range(26):
                if (m >> i) & 1 and (m ^ (1 << i)) in starts:
                    ans += 1
                    break
        return ans
