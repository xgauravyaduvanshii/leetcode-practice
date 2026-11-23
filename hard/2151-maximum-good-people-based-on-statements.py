# LeetCode 2151. Maximum Good People Based on Statements — Hard
# https://leetcode.com/problems/maximum-good-people-based-on-statements/
# Submission 2201590323 — Accepted, Python3
#
# My thinking: with fifteen people at most I
# can just try every possible set of good
# people — a set only stands if every good
# person's word about everyone else matches
# the set, and the biggest set that stands is
# the answer.

class Solution:
    def maximumGood(self, statements: list[list[int]]) -> int:
        n = len(statements)
        best = 0
        for mask in range(1 << n):
            good = [bool(mask >> i & 1) for i in range(n)]
            ok = True
            for i in range(n):
                if not good[i]:
                    continue
                for j in range(n):
                    if statements[i][j] == 1 and not good[j]:
                        ok = False
                        break
                    if statements[i][j] == 0 and good[j]:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                best = max(best, sum(good))
        return best
