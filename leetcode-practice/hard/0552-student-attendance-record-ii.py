# LeetCode 552. Student Attendance Record II — Hard
# https://leetcode.com/problems/student-attendance-record-ii/
# Submission 2198663243 — Accepted, Python3
#
# My thinking: the only things that matter are how
# many absences I have used and how many lates are
# trailing right now. Each day I can add a present
# (late streak resets), an absent (only if none used),
# or a late (only if fewer than two in a row), and I
# carry the counts forward day by day.

class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        # dp[absences][trailing lates] = ways so far
        dp = [[0] * 3 for _ in range(2)]
        dp[0][0] = 1
        for _ in range(n):
            nxt = [[0] * 3 for _ in range(2)]
            for absences in range(2):
                for lates in range(3):
                    ways = dp[absences][lates]
                    if not ways:
                        continue
                    nxt[absences][0] = (nxt[absences][0] + ways) % MOD
                    if absences == 0:
                        nxt[1][0] = (nxt[1][0] + ways) % MOD
                    if lates < 2:
                        nxt[absences][lates + 1] = (nxt[absences][lates + 1] + ways) % MOD
            dp = nxt
        return sum(sum(row) for row in dp) % MOD
