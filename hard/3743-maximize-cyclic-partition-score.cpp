// LeetCode 3743. Maximize Cyclic Partition Score — Hard
// https://leetcode.com/problems/maximize-cyclic-partition-score/
// Submission 2203150148 — Accepted, C++
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    long long maximumScore(vector<int>& nums, int k) {
        // My thinking: a segment scores its max minus its min,
        // so the whole partition scores the sum of the picked
        // maxes minus the sum of the picked mins. I walk the
        // array once and pick some elements as a segment max
        // (+x) or a segment min (-x), skipping the rest. The
        // two picks of one segment sit side by side in the
        // cyclic order, so the running difference between max
        // picks and min picks only ever takes the values -1, 0
        // and 1 — I keep it as a balance of 0, 1 or 2. Because
        // the array is cyclic, the cut between the last and the
        // first element can fall inside a pair, so the balance
        // at the start of the scan can be 0, 1 or 2; I try all
        // three and require the balance to return to its
        // starting value at the end, which also forces the
        // numbers of max and min picks to match. The count c
        // of max picks is the number of segments used, capped
        // at k, and skipping a bad pair is always free, so the
        // best score over the three starts is the answer.
        const long long NEG = (long long)-4e18;
        long long best = 0;
        int n = (int)nums.size();
        for (int b0 = 0; b0 <= 2; b0++) {
            vector<vector<long long>> dp(k + 1, vector<long long>(3, NEG));
            dp[0][b0] = 0;
            for (int i = 0; i < n; i++) {
                vector<vector<long long>> ndp = dp;
                int x = nums[i];
                for (int c = 0; c <= min(k, i); c++) {
                    for (int b = 0; b < 3; b++) {
                        long long v = dp[c][b];
                        if (v == NEG) continue;
                        if (b < 2 && c < k) {
                            ndp[c + 1][b + 1] = max(ndp[c + 1][b + 1], v + x);
                        }
                        if (b > 0) {
                            ndp[c][b - 1] = max(ndp[c][b - 1], v - x);
                        }
                    }
                }
                dp = move(ndp);
            }
            for (int c = 0; c <= k; c++) {
                best = max(best, dp[c][b0]);
            }
        }
        return best;
    }
};
