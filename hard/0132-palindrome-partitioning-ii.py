# LeetCode 132. Palindrome Partitioning II — Hard
# https://leetcode.com/problems/palindrome-partitioning-ii/
# Submission 2198387910 — Accepted, Python3
#
# My thinking: I first mark every substring that is
# a palindrome — a substring is one when its ends
# match and the inside is a palindrome too. Then I
# work out the fewest cuts for each prefix: no cut
# if the whole prefix is a palindrome, otherwise one
# cut after the best palindromic ending I can find.

class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        is_pal = [[False] * n for _ in range(n)]
        for end in range(n):
            for start in range(end + 1):
                if s[start] == s[end] and (end - start <= 1 or is_pal[start + 1][end - 1]):
                    is_pal[start][end] = True
        cuts = [0] * n
        for end in range(n):
            if is_pal[0][end]:
                cuts[end] = 0
            else:
                cuts[end] = min(cuts[start - 1] + 1 for start in range(1, end + 1) if is_pal[start][end])
        return cuts[-1]
