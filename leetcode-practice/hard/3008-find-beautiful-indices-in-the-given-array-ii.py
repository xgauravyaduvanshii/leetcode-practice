# LeetCode 3008. Find Beautiful Indices in the Given Array II — Hard
# https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-ii/
# Submission 2201881353 — Accepted, Python3
#
# My thinking: I find every place a
# and b occur with KMP, then for each
# occurrence of a I check by binary
# search whether an occurrence of b
# sits within k of it.

import bisect


class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> list[int]:
        def positions(text: str, pat: str) -> list[int]:
            # Prefix function, then one left-to-right scan.
            pi = [0] * len(pat)
            j = 0
            for i in range(1, len(pat)):
                while j > 0 and pat[i] != pat[j]:
                    j = pi[j - 1]
                if pat[i] == pat[j]:
                    j += 1
                pi[i] = j
            found = []
            j = 0
            for i, ch in enumerate(text):
                while j > 0 and ch != pat[j]:
                    j = pi[j - 1]
                if ch == pat[j]:
                    j += 1
                if j == len(pat):
                    found.append(i - len(pat) + 1)
                    j = pi[j - 1]
            return found

        a_pos = positions(s, a)
        b_pos = positions(s, b)
        ans = []
        for i in a_pos:
            t = bisect.bisect_left(b_pos, i - k)
            if t < len(b_pos) and b_pos[t] <= i + k:
                ans.append(i)
        return ans
