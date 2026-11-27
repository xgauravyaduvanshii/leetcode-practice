// LeetCode 1770. Maximum Score from Performing Multiplication Operations — Hard
// https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/
// Submission 2201154598 — Accepted, C++
//
// My thinking: after some operations I have taken
// a few numbers from the left and the rest from the
// right, so I only need to remember how many came
// from the left — each new multiplier can take the
// next number from either end.

#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maximumScore(vector<int>& nums, vector<int>& multipliers) {
        int n = nums.size(), m = multipliers.size();
        const int NEG = -1e9;
        vector<int> dp(m + 1, NEG), ndp(m + 1, NEG);
        dp[0] = 0;
        for (int op = 0; op < m; op++) {
            fill(ndp.begin(), ndp.end(), NEG);
            for (int left = 0; left <= op; left++) {
                if (dp[left] == NEG) continue;
                int right = op - left;
                ndp[left + 1] = max(ndp[left + 1], dp[left] + multipliers[op] * nums[left]);
                ndp[left] = max(ndp[left], dp[left] + multipliers[op] * nums[n - 1 - right]);
            }
            dp.swap(ndp);
        }
        return *max_element(dp.begin(), dp.end());
    }
};
