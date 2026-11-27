# LeetCode 1974. Minimum Time to Type Word Using Special Typewriter — Easy
# https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter/
# Submission 2197606864 — Accepted, Python3
#
# My thinking: the typewriter pointer starts at 'a'.
# For each letter, I move the pointer the short way
# round the circle — the smaller of the clockwise
# and counter-clockwise distance — and each letter
# costs 1 more second to type.

class Solution:
    def minTimeToType(self, word: str) -> int:
        time = 0
        cur = 'a'
        for ch in word:
            diff = abs(ord(ch) - ord(cur))
            time += min(diff, 26 - diff) + 1
            cur = ch
        return time
