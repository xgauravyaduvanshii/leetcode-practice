# LeetCode 2663. Lexicographically Smallest Beautiful String — Hard
# https://leetcode.com/problems/lexicographically-smallest-beautiful-string/
# Submission 2201866007 — Accepted, Python3
#
# My thinking: a string is beautiful
# exactly when no letter repeats its
# neighbour or the one before that, so
# I walk back from the end, lift the
# first letter I can, and fill the rest
# with the smallest letters that keep
# the rule — the first lift that works
# is the smallest larger string.

class Solution:
    def smallestBeautifulString(self, s: str, k: int) -> str:
        n = len(s)
        a = [ord(c) - ord("a") for c in s]
        for i in range(n - 1, -1, -1):
            for c in range(a[i] + 1, k):
                if i >= 1 and c == a[i - 1]:
                    continue
                if i >= 2 and c == a[i - 2]:
                    continue
                res = a[:i] + [c]
                for j in range(i + 1, n):
                    for d in range(k):
                        if d != res[-1] and (len(res) < 2 or d != res[-2]):
                            res.append(d)
                            break
                return "".join(chr(x + ord("a")) for x in res)
        return ""
