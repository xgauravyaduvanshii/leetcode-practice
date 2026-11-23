# LeetCode 2484. Count Palindromic Subsequences — Hard
# https://leetcode.com/problems/count-palindromic-subsequences/
# Submission 2201775485 — Accepted, Python3
#
# My thinking: a length-5 palindrome reads
# a b c b a, so for each middle digit I
# count how many (a, b) pairs sit to its
# left and how many (b, a) pairs sit to
# its right — with only ten digits there
# are just a hundred pairs to track, and
# I sweep both sides once to learn them.

class Solution:
    def countPalindromes(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        n = len(s)
        digits = [int(ch) for ch in s]
        # suffix pair counts: suf[i][b][a] = number of (b, a) pairs in s[i:]
        suf = [[[0] * 10 for _ in range(10)] for _ in range(n + 1)]
        cnt = [0] * 10
        for i in range(n - 1, -1, -1):
            for b in range(10):
                for a in range(10):
                    suf[i][b][a] = suf[i + 1][b][a]
            d = digits[i]
            for a in range(10):
                suf[i][d][a] += cnt[a]
            cnt[d] += 1
        ans = 0
        left = [[0] * 10 for _ in range(10)]
        seen = [0] * 10
        for i in range(n):
            if i + 1 < n:
                right = suf[i + 1]
                for a in range(10):
                    for b in range(10):
                        ans = (ans + left[a][b] * right[b][a]) % MOD
            d = digits[i]
            for a in range(10):
                left[a][d] += seen[a]
            seen[d] += 1
        return ans
