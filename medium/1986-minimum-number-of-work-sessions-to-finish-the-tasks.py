# LeetCode 1986. Minimum Number of Work Sessions to Finish the Tasks — Medium
# https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/
# Submission 2204103404 — Accepted, Python3
#
# My thinking: there are at most 14 tasks, so I can try every subset
# of tasks with a bitmask. For each subset I remember the best way to
# finish exactly those tasks: the fewest sessions used, and, among
# those, the most time left in the current session. Starting from an
# empty subset with one open session, I add one task at a time: if it
# fits in the time left, it joins the current session, otherwise I
# open a new session for it. Comparing first on sessions and then on
# leftover time keeps the best state for every subset, and the state
# for the full set gives the minimum number of sessions.

class Solution:
    def minSessions(self, tasks: list[int], sessionTime: int) -> int:
        n = len(tasks)
        full = (1 << n) - 1
        # dp[mask] = (sessions used, time left in the current session)
        INF = float("inf")
        dp = [(INF, 0)] * (1 << n)
        dp[0] = (1, sessionTime)
        for mask in range(1 << n):
            sessions, left = dp[mask]
            if sessions == INF:
                continue
            for i in range(n):
                if mask & (1 << i):
                    continue
                nxt = mask | (1 << i)
                if tasks[i] <= left:
                    cand = (sessions, left - tasks[i])
                else:
                    cand = (sessions + 1, sessionTime - tasks[i])
                # Fewer sessions wins; tie-break on more time left.
                if cand[0] < dp[nxt][0] or (cand[0] == dp[nxt][0] and cand[1] > dp[nxt][1]):
                    dp[nxt] = cand
        return dp[full][0]
