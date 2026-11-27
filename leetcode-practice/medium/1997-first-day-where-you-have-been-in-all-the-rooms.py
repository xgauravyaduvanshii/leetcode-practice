# LeetCode 1997. First Day Where You Have Been in All the Rooms — Medium
# https://leetcode.com/problems/first-day-where-you-have-been-in-all-the-rooms/
# Submission 2204360285 — Accepted, Python3
#
# My thinking: let dp[i] be the first day I reach room i. To get from
# room i-1 to room i I must first reach i-1 (dp[i-1] days), then I am
# sent back to nextVisit[i-1] on the odd visit, so I need
# dp[i-1] - dp[nextVisit[i-1]] more days to climb back to i-1, plus
# one day for the even visit that finally moves me to i, plus one more
# day to actually arrive. That gives dp[i] = 2*dp[i-1] -
# dp[nextVisit[i-1]] + 2, all modulo 1e9+7.
class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(nextVisit)
        dp = [0] * n
        for i in range(1, n): dp[i] = (2 * dp[i - 1] - dp[nextVisit[i - 1]] + 2) % MOD
        return dp[-1]
