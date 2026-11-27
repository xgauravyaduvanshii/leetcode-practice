# LeetCode 4068. Maximize Meeting Earnings with Idle Gaps — Hard
# https://leetcode.com/problems/maximize-meeting-earnings-with-idle-gaps/
# Submission 2203592517 — Accepted, Python3
import bisect


class Solution:
    def maxEarnings(self, meetings: list[list[int]]) -> int:
        # My thinking: sort by end time, so any meeting
        # that can come before meeting i is an earlier
        # index. Let dp[i] be the best total for a
        # schedule whose last meeting is i. Taking i
        # alone earns revenue[i]; extending a schedule
        # ending at j (end[j] <= start[i], half-open so
        # touching is allowed) adds revenue[i] plus the
        # idle gap start[i] - end[j]. That is revenue[i]
        # + start[i] + (dp[j] - end[j]), so for each i
        # we only need the best value of dp[j] - end[j]
        # over all eligible j. Because ends are sorted,
        # the eligible j are a prefix, found by binary
        # search, and their best dp[j] - end[j] is a
        # running prefix maximum. The answer is the
        # best dp over all i.
        ms = sorted(meetings, key=lambda m: m[1])
        n = len(ms)
        ends = [m[1] for m in ms]
        pref = [0] * n  # pref[i] = max(dp[j] - end[j]) for j <= i
        ans = 0
        for i, (s, e, r) in enumerate(ms):
            j = bisect.bisect_right(ends, s) - 1
            best = r
            if j >= 0:
                best = max(best, r + s + pref[j])
            val = best - e
            pref[i] = val if i == 0 else max(val, pref[i - 1])
            ans = max(ans, best)
        return ans
