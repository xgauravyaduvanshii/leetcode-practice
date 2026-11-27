// LeetCode 1986. Minimum Number of Work Sessions to Finish the Tasks — Medium
// https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/
// Submission 2204105086 — Accepted, C++
//
// My thinking: there are at most 14 tasks, so I can try every subset
// of tasks with a bitmask. For each subset I remember the best way to
// finish exactly those tasks: the fewest sessions used, and, among
// those, the most time left in the current session. Starting from an
// empty subset with one open session, I add one task at a time: if it
// fits in the time left, it joins the current session, otherwise I
// open a new session for it. Comparing first on sessions and then on
// leftover time keeps the best state for every subset, and the state
// for the full set gives the minimum number of sessions.

class Solution {
public:
    int minSessions(vector<int>& tasks, int sessionTime) {
        int n = tasks.size();
        int full = (1 << n) - 1;
        const int INF = 1e9;
        // dp[mask] = {sessions used, time left in the current session}
        vector<pair<int, int>> dp(1 << n, {INF, 0});
        dp[0] = {1, sessionTime};
        for (int mask = 0; mask <= full; mask++) {
            int sessions = dp[mask].first;
            int left = dp[mask].second;
            if (sessions == INF) continue;
            for (int i = 0; i < n; i++) {
                if (mask & (1 << i)) continue;
                int nxt = mask | (1 << i);
                pair<int, int> cand;
                if (tasks[i] <= left) {
                    cand = {sessions, left - tasks[i]};
                } else {
                    cand = {sessions + 1, sessionTime - tasks[i]};
                }
                // Fewer sessions wins; tie-break on more time left.
                if (cand.first < dp[nxt].first ||
                    (cand.first == dp[nxt].first && cand.second > dp[nxt].second)) {
                    dp[nxt] = cand;
                }
            }
        }
        return dp[full].first;
    }
};
