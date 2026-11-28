# LeetCode 2486. Append Characters to String to Make Subsequence — Medium
# https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/
# Submission 2204972521 — Accepted, Python3
#
# My thinking: walk through s matching the characters of t in
# order. Whatever prefix of t gets matched is already a subsequence;
# the rest of t has to be appended, so the answer is the number of
# unmatched characters.
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0
        for ch in s:
            if i < len(t) and ch == t[i]:
                i += 1
        return len(t) - i
