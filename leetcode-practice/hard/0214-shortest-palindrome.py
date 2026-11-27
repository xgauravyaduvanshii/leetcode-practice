# LeetCode 214. Shortest Palindrome — Hard
# https://leetcode.com/problems/shortest-palindrome/
# Submission 2198394474 — Accepted, Python3
#
# My thinking: the front of the string is already a
# palindrome up to some point, and I only need to
# add the mirror of the rest in front. I find that
# longest palindromic prefix with a KMP prefix
# table on the string joined to its reverse — the
# table's last value tells me how much of the front
# already matches.

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        rev = s[::-1]
        combined = s + "#" + rev
        lps = [0] * len(combined)
        for i in range(1, len(combined)):
            j = lps[i - 1]
            while j > 0 and combined[i] != combined[j]:
                j = lps[j - 1]
            if combined[i] == combined[j]:
                j += 1
            lps[i] = j
        add = rev[:len(s) - lps[-1]]
        return add + s
