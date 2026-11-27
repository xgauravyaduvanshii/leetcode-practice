# LeetCode 140. Word Break II — Hard
# https://leetcode.com/problems/word-break-ii/
# Submission 2198389375 — Accepted, Python3
#
# My thinking: I build sentences from each starting
# position. I try every word that fits at that spot,
# then ask the same question for what is left after
# it, and join the word to each of those endings.
# I remember the sentences for positions I have
# already solved so the same tail is never rebuilt.

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        memo = {}

        def build(start: int) -> List[str]:
            if start in memo:
                return memo[start]
            if start == len(s):
                return [""]
            sentences = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in words:
                    for rest in build(end):
                        sentences.append(word + (" " + rest if rest else ""))
            memo[start] = sentences
            return sentences

        return build(0)
