# LeetCode 139. Word Break — Medium
# https://leetcode.com/problems/word-break/
# Submission 2200953199 — Accepted, Python3
#
# My thinking: I mark every position I can reach, then
# from each reachable position I try every dictionary
# word that fits there and mark the position after it.

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        words = set(wordDict)
        n = len(s)
        reachable = [False] * (n + 1)
        reachable[0] = True
        for i in range(n):
            if not reachable[i]:
                continue
            for word in words:
                if s.startswith(word, i):
                    reachable[i + len(word)] = True
        return reachable[n]
