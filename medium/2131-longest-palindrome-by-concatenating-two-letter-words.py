# LeetCode 2131. Longest Palindrome by Concatenating Two Letter Words — Medium
# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/
# Submission 2204468989 — Accepted, Python3
#
# My thinking: a palindrome is built from pairs of mirror words like
# "ab" with "ba", and each such pair adds four letters. Words with two
# equal letters can pair with themselves, and at most one leftover
# equal-letter word can sit in the center for two extra letters. So I
# count the words, add the mirrored pairs once each, and add the center
# only if some equal-letter word is left unpaired.
class Solution:
    def longestPalindrome(self, words: list[str]) -> int:
        from collections import Counter
        cnt = Counter(words)
        ans = 0
        center = False
        for w, c in cnt.items():
            if w[0] == w[1]:
                ans += (c // 2) * 4
                if c % 2:
                    center = True
            elif w[0] < w[1]:
                ans += min(c, cnt.get(w[::-1], 0)) * 4
        return ans + (2 if center else 0)
