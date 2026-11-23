# LeetCode 2585. Number of Ways to Earn Points — Hard
# https://leetcode.com/problems/number-of-ways-to-earn-points/
# Submission 2201839061 — Accepted, Python3
#
# My thinking: I count the ways to
# reach each total one question type at
# a time — for a type I try taking none
# of its questions, one, two, and so on
# up to however many it has, and the
# totals add up.

class Solution:
    def waysToReachTarget(self, target: int, types: list[list[int]]) -> int:
        MOD = 10 ** 9 + 7
        dp = [0] * (target + 1)
        dp[0] = 1
        for count, marks in types:
            ndp = [0] * (target + 1)
            for s in range(target + 1):
                if dp[s] == 0:
                    continue
                for t in range(count + 1):
                    ns = s + t * marks
                    if ns > target:
                        break
                    ndp[ns] = (ndp[ns] + dp[s]) % MOD
            dp = ndp
        return dp[target]
