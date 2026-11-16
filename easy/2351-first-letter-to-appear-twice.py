# LeetCode 2351. First Letter to Appear Twice — Easy
# https://leetcode.com/problems/first-letter-to-appear-twice/
# Submission 2197624449 — Accepted, Python3
#
# My thinking: I walk through the letters and keep
# the ones I have already seen. The first letter I
# meet a second time is the answer.

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = set()
        for ch in s:
            if ch in seen:
                return ch
            seen.add(ch)
        return ""
