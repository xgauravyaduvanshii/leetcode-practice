# LeetCode 2900. Longest Unequal Adjacent Groups Subsequence I — Easy
# https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/
# Submission 2198694380 — Accepted, Python3
#
# My thinking: the longest alternating subsequence is
# just greedy — I take the first word, then every word
# whose group differs from the last one I took. Any
# alternating subsequence has to skip same-group runs
# anyway, so this picks up as many as possible.

from typing import List


class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        picked = [words[0]]
        last_group = groups[0]
        for word, group in zip(words[1:], groups[1:]):
            if group != last_group:
                picked.append(word)
                last_group = group
        return picked
