# LeetCode 2564. Substring XOR Queries — Medium
# https://leetcode.com/problems/substring-xor-queries/
# Submission 2205070519 — Accepted, Python3
#
# My thinking: the target of a query is first XOR second, and any
# value that fits needs at most 30 bits, so only substrings up to
# length 30 can matter (except value 0, whose shortest form is a
# single '0'). Precompute the shortest, leftmost substring for
# every reachable value once, then answer each query from the map.
class Solution:
    def substringXorQueries(self, s: str, queries: list[list[int]]) -> list[list[int]]:
        n = len(s)
        best = {}
        for i, ch in enumerate(s):
            if ch == "0":
                best[0] = (1, i)
                break
        for i in range(n):
            if s[i] == "0":
                continue
            val = 0
            for j in range(i, min(n, i + 30)):
                val = val * 2 + (ord(s[j]) - 48)
                cand = (j - i + 1, i)
                if val not in best or cand < best[val]:
                    best[val] = cand
        ans = []
        for first, second in queries:
            t = first ^ second
            if t in best:
                length, start = best[t]
                ans.append([start, start + length - 1])
            else:
                ans.append([-1, -1])
        return ans
