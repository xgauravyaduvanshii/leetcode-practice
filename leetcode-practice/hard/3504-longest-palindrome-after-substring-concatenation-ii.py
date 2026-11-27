# LeetCode 3504. Longest Palindrome After Substring Concatenation II — Hard
# https://leetcode.com/problems/longest-palindrome-after-substring-concatenation-ii/
# Submission 2202752741 — Accepted, Python3
from typing import List


class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        # My thinking: a palindrome made from a substring of s plus a
        # substring of t is either wholly inside one string, or it
        # spans both. When it spans, the outer part is a substring of
        # s matched against the reverse of a substring of t, and the
        # inner part that is left over must itself be a palindrome. So
        # I precompute, for every pair of suffixes of s and reversed t,
        # how far they match, and for every position in s the longest
        # palindromic substring starting there. For a match of length L
        # starting at i, the best spanning palindrome is the longest
        # palindromic middle I can put after any of the first L matched
        # characters, which is a range maximum over 2*y + best-pal(y).
        # The mirror case, with the palindromic middle inside t, is the
        # same computation run on the two reversed strings.
        def pal_dp(u):
            n = len(u)
            pal = [[False] * n for _ in range(n)]
            for i in range(n):
                pal[i][i] = True
            for i in range(n - 1):
                pal[i][i + 1] = (u[i] == u[i + 1])
            for L in range(3, n + 1):
                for i in range(n - L + 1):
                    j = i + L - 1
                    pal[i][j] = (u[i] == u[j] and pal[i + 1][j - 1])
            return pal

        def longest_pal_sub(u):
            pal = pal_dp(u)
            best = 0
            for i in range(len(u)):
                for j in range(i, len(u)):
                    if pal[i][j]:
                        best = max(best, j - i + 1)
            return best

        def pal_start(u, pal):
            n = len(u)
            g = [0] * (n + 1)
            for y in range(n):
                best = 0
                for j in range(y, n):
                    if pal[y][j]:
                        best = max(best, j - y + 1)
                g[y] = best
            return g

        def lcp_table(a, b):
            na, nb = len(a), len(b)
            lcp = [[0] * (nb + 1) for _ in range(na + 1)]
            for i in range(na - 1, -1, -1):
                for j in range(nb - 1, -1, -1):
                    lcp[i][j] = lcp[i + 1][j + 1] + 1 if a[i] == b[j] else 0
            return lcp

        def sparse_max(arr):
            m = len(arr)
            LOG = [0] * (m + 1)
            for i in range(2, m + 1):
                LOG[i] = LOG[i // 2] + 1
            st = [arr[:]]
            j = 1
            while (1 << j) <= m:
                prev = st[-1]
                cur = [0] * (m - (1 << j) + 1)
                for i in range(len(cur)):
                    cur[i] = max(prev[i], prev[i + (1 << (j - 1))])
                st.append(cur)
                j += 1
            return st, LOG

        def spanning(a, b):
            na, nb = len(a), len(b)
            revb = b[::-1]
            pal_a = pal_dp(a)
            g = pal_start(a, pal_a)
            h = [2 * y + g[y] for y in range(na + 1)]
            st, LOG = sparse_max(h)
            lcp = lcp_table(a, revb)
            best = 0
            for i in range(na):
                for p in range(nb):
                    L = lcp[i][p]
                    if L == 0:
                        continue
                    lo = i + 1
                    hi = min(i + L, na)
                    if lo > hi:
                        continue
                    j = LOG[hi - lo + 1]
                    mx = max(st[j][lo], st[j][hi - (1 << j) + 1])
                    best = max(best, mx - 2 * i)
            return best

        ans = max(longest_pal_sub(s), longest_pal_sub(t))
        ans = max(ans, spanning(s, t))
        ans = max(ans, spanning(t[::-1], s[::-1]))
        return ans
