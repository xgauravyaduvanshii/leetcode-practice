// LeetCode 2478. Number of Beautiful Partitions — Hard
// https://leetcode.com/problems/number-of-beautiful-partitions/
// Submission 2201772054 — Accepted, C++
//
// My thinking: a beautiful piece must
// start on a prime digit and end on a
// non-prime one, so for each end I only
// need the running total of ways to reach
// the prime starts that are far enough
// back — I keep that total as a prefix
// sum and sweep it across the pieces.

#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int beautifulPartitions(string s, int k, int minLength) {
        const int MOD = 1000000007;
        int n = (int)s.size();
        auto isPrime = [](char c) { return c == '2' || c == '3' || c == '5' || c == '7'; };
        vector<vector<int>> dp(n + 1, vector<int>(k + 1, 0));
        dp[0][0] = 1;
        for (int j = 1; j <= k; j++) {
            long long pref = 0;
            for (int i = 1; i <= n; i++) {
                int a = i - minLength;
                if (a >= 0 && isPrime(s[a])) {
                    pref = (pref + dp[a][j - 1]) % MOD;
                }
                if (!isPrime(s[i - 1])) {
                    dp[i][j] = (int)pref;
                }
            }
        }
        return dp[n][k];
    }
};
