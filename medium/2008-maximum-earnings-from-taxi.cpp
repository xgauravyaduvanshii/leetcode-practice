// LeetCode 2008. Maximum Earnings From Taxi — Medium
// https://leetcode.com/problems/maximum-earnings-from-taxi/
// Submission 2204133721 — Accepted, C++

// My thinking: a ride from start to end pays end - start + tip, and
// I can only carry one passenger at a time, so I pick a set of rides
// that never overlap. I sort the rides by their end point and keep a
// table dp where dp[i] is the best money I can earn by the time I reach
// point i. For each ride ending at end, taking it means I add its pay
// to the best I had at its start, and I keep whichever is better:
// taking it or skipping it. I also carry the best value forward from
// the previous point, so points with no ride ending there keep what I
// already earned. The answer is dp[n].
class Solution {
public:
    long long maxTaxiEarnings(int n, vector<vector<int>>& rides) {
        sort(rides.begin(), rides.end(),
             [](const vector<int>& a, const vector<int>& b) {
                 return a[1] < b[1];
             });
        vector<long long> dp(n + 1, 0);
        size_t rideIndex = 0;
        for (int point = 1; point <= n; ++point) {
            dp[point] = max(dp[point], dp[point - 1]);
            while (rideIndex < rides.size() && rides[rideIndex][1] == point) {
                int start = rides[rideIndex][0];
                int end = rides[rideIndex][1];
                int tip = rides[rideIndex][2];
                dp[end] = max(dp[end], dp[start] + end - start + tip);
                ++rideIndex;
            }
        }
        return dp[n];
    }
};
