// LeetCode 3883. Count Non Decreasing Arrays With Given Digit Sums — Hard
// https://leetcode.com/problems/count-non-decreasing-arrays-with-given-digit-sums/
// Submission 2203341836 — Accepted, C++
#include <vector>
using namespace std;

class Solution {
public:
    int countArrays(vector<int>& digitSum) {
        // My thinking: the value at each position is a number
        // from 0 to 5000 whose digit sum is fixed, so first
        // list, for every digit sum, the numbers that have it.
        // Then dp over the value axis: dp[v] is the number of
        // ways to fill the positions so far ending with value
        // v, which is the prefix sum of the previous dp over
        // all values up to v when v has the required digit
        // sum, and 0 otherwise. Prefix sums make each
        // position O(5000), and the answer is the sum of the
        // last dp, all modulo 1e9 + 7. A digit sum above 36
        // is impossible, since 4999 has the largest digit sum
        // in range, 36.
        const int MOD = 1000000007;
        const int MAXV = 5000;
        vector<int> ds(MAXV + 1, 0);
        for (int v = 1; v <= MAXV; ++v) ds[v] = ds[v / 10] + v % 10;
        vector<vector<int>> valid(51);
        for (int v = 0; v <= MAXV; ++v) valid[ds[v]].push_back(v);
        vector<int> prev(MAXV + 1, 0), cur(MAXV + 1, 0), pref(MAXV + 1, 0);
        for (int v : valid[digitSum[0]]) prev[v] = 1;
        for (size_t i = 1; i < digitSum.size(); ++i) {
            int s = digitSum[i];
            if (s > 36) return 0;
            long long run = 0;
            for (int v = 0; v <= MAXV; ++v) {
                run += prev[v];
                if (run >= MOD) run -= MOD;
                pref[v] = (int)run;
            }
            fill(cur.begin(), cur.end(), 0);
            for (int v : valid[s]) cur[v] = pref[v];
            prev.swap(cur);
        }
        long long ans = 0;
        for (int x : prev) {
            ans += x;
            if (ans >= MOD) ans -= MOD;
        }
        return (int)ans;
    }
};
