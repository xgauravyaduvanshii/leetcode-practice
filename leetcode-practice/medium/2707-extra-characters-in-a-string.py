# LeetCode 2707. Extra Characters in a String — Medium
# https://leetcode.com/problems/extra-characters-in-a-string/
# Submission 2197819693 — Accepted, Python3
#
# My thinking: I work backwards through the string.
# At each position I either leave the character as
# an extra one, or I match a dictionary word
# starting there and take the best result from
# after that word.

from typing import List


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            dp[i] = 1 + dp[i + 1]
            for w in dictionary:
                if s.startswith(w, i):
                    dp[i] = min(dp[i], dp[i + len(w)])
        return dp[0]
