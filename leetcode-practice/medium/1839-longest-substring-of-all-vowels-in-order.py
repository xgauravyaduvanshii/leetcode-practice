# LeetCode 1839. Longest Substring Of All Vowels in Order — Medium
# https://leetcode.com/problems/longest-substring-of-all-vowels-in-order/
# Submission 2199946110 — Accepted, Python3
#
# My thinking: a beautiful substring only
# uses vowels in the order a, e, i, o, u. I
# walk the word keeping the current run's
# length and how many different vowels it has
# seen, and restart whenever the order breaks.

class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        vowels = "aeiou"
        best = 0
        current = 1
        distinct = 1
        for i in range(1, len(word)):
            if word[i] >= word[i - 1] and word[i] in vowels and word[i - 1] in vowels:
                current += 1
                if word[i] != word[i - 1]:
                    distinct += 1
            else:
                current = 1
                distinct = 1
            if distinct == 5:
                best = max(best, current)
        return best
