# LeetCode 2008. Maximum Earnings From Taxi — Medium
# https://leetcode.com/problems/maximum-earnings-from-taxi/
# Submission 2204132872 — Accepted, Python3
#
# My thinking: a ride from start to end pays end - start + tip, and
# I can only carry one passenger at a time, so I pick a set of rides
# that never overlap. I sort the rides by their end point and keep a
# table dp where dp[i] is the best money I can earn by the time I reach
# point i. For each ride ending at end, taking it means I add its pay
# to the best I had at its start, and I keep whichever is better:
# taking it or skipping it. I also carry the best value forward from
# the previous point, so points with no ride ending there keep what I
# already earned. The answer is dp[n].
class Solution:
    def maxTaxiEarnings(self, n: int, rides: list[list[int]]) -> int:
        rides.sort(key=lambda ride: ride[1])
        dp = [0] * (n + 1)
        ride_index = 0
        for point in range(1, n + 1):
            dp[point] = max(dp[point], dp[point - 1])
            while ride_index < len(rides) and rides[ride_index][1] == point:
                start, end, tip = rides[ride_index]
                dp[end] = max(dp[end], dp[start] + end - start + tip)
                ride_index += 1
        return dp[n]
