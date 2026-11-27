# LeetCode 2120. Execution of All Suffix Instructions Staying in a Grid — Medium
# https://leetcode.com/problems/execution-of-all-suffix-instructions-staying-in-a-grid/
# Submission 2204406158 — Accepted, Python3
#
# My thinking: for each starting position in the instruction string I
# just simulate the suffix step by step from the start cell, counting
# moves until one would leave the grid. The count for that suffix is
# how many instructions executed before the first illegal move.
class Solution:
    def executeInstructions(self, n: int, startPos: list[int], s: str) -> list[int]:
        ans = []
        for i in range(len(s)):
            r, c = startPos
            cnt = 0
            for ch in s[i:]:
                nr = r + (1 if ch == 'D' else -1 if ch == 'U' else 0)
                nc = c + (1 if ch == 'R' else -1 if ch == 'L' else 0)
                if not (0 <= nr < n and 0 <= nc < n):
                    break
                r, c = nr, nc
                cnt += 1
            ans.append(cnt)
        return ans
