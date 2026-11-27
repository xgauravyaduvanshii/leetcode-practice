# LeetCode 3455. Shortest Matching Substring — Hard
# https://leetcode.com/problems/shortest-matching-substring/
# Submission 2202551549 — Accepted 795/795, Python3
from typing import List


class Solution:
    def shortestMatchingSubstring(self, s: str, p: str) -> int:
        # My thinking: the two stars split p into three literals
        # a, b, c, so a match is an a-occurrence followed by the
        # earliest later b-occurrence and then the earliest later
        # c-occurrence. I list every occurrence of each literal
        # with KMP (repeated str.find is too slow on long runs of
        # the same letter), then sweep the a-starts with two
        # pointers that only move forward, and keep the shortest
        # span from an a-start to the end of its c.
        n = len(s)

        def starts(pat: str) -> List[int]:
            if not pat:
                return list(range(n + 1))
            m = len(pat)
            lps = [0] * m
            length = 0
            i = 1
            while i < m:
                if pat[i] == pat[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                elif length:
                    length = lps[length - 1]
                else:
                    i += 1
            res = []
            i = 0
            j = 0
            while i < n:
                if s[i] == pat[j]:
                    i += 1
                    j += 1
                if j == m:
                    res.append(i - j)
                    j = lps[j - 1]
                elif i < n and s[i] != pat[j]:
                    if j:
                        j = lps[j - 1]
                    else:
                        i += 1
            return res

        a, b, c = p.split("*")
        A, B, C = starts(a), starts(b), starts(c)
        la, lb, lc = len(a), len(b), len(c)
        ans = n + 1
        j = 0
        k = 0
        for i in A:
            while j < len(B) and B[j] < i + la:
                j += 1
            if j == len(B):
                break
            while k < len(C) and C[k] < B[j] + lb:
                k += 1
            if k == len(C):
                break
            ans = min(ans, C[k] + lc - i)
        return -1 if ans > n else ans
