# LeetCode 1048. Longest String Chain — Medium
# https://leetcode.com/problems/longest-string-chain/
# Submission 2198993241 — Accepted, Python3
#
# My thinking: I sort the words by length, then
# for each word I try deleting one letter in
# every spot. If the shorter word already has a
# chain, this word extends it by one.

from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        best = {}
        longest = 1
        for word in words:
            chain = 1
            for i in range(len(word)):
                shorter = word[:i] + word[i + 1:]
                if shorter in best:
                    chain = max(chain, best[shorter] + 1)
            best[word] = chain
            longest = max(longest, chain)
        return longest
