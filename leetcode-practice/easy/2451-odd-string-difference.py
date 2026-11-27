# LeetCode 2451. Odd String Difference — Easy
# https://leetcode.com/problems/odd-string-difference/
# Submission 2197787702 — Accepted, Python3
#
# My thinking: each word has a pattern of differences
# between consecutive letters. All words share one
# pattern except one — I compare the first two
# words' patterns to find which is the odd one out.

class Solution:
    def oddString(self, words: list[str]) -> str:
        def diff(w):
            return tuple(ord(w[i + 1]) - ord(w[i]) for i in range(len(w) - 1))
        d0 = diff(words[0])
        d1 = diff(words[1])
        if d0 != d1:
            return words[0] if diff(words[2]) == d1 else words[1]
        for w in words[2:]:
            if diff(w) != d0:
                return w
        return ""
