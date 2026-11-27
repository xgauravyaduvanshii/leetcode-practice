// LeetCode 2585. Number of Ways to Earn Points — Hard
// https://leetcode.com/problems/number-of-ways-to-earn-points/
// Submission 2201840290 — Accepted, C++
//
// My thinking: I count the ways to
// reach each total one question type at
// a time — for a type I try taking none
// of its questions, one, two, and so on
// up to however many it has, and the
// totals add up.

#include <vector>
using namespace std;

class Solution {
public:
    int waysToReachTarget(int target, vector<vector<int>>& types) {
        const int MOD = 1e9 + 7;
        vector<int> dp(target + 1, 0);
        dp[0] = 1;
        for (auto& tp : types) {
            int count = tp[0], marks = tp[1];
            vector<int> ndp(target + 1, 0);
            for (int s = 0; s <= target; s++) {
                if (dp[s] == 0) continue;
                for (int t = 0; t <= count; t++) {
                    int ns = s + t * marks;
                    if (ns > target) break;
                    ndp[ns] = (ndp[ns] + dp[s]) % MOD;
                }
            }
            dp.swap(ndp);
        }
        return dp[target];
    }
};
