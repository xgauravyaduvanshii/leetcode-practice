// LeetCode 2552. Count Increasing Quadruplets — Hard
// https://leetcode.com/problems/count-increasing-quadruplets/
// Submission 2201820934 — Accepted, C++
//
// My thinking: I fix the middle pair
// and count what can go on either side
// of it — how many smaller numbers sit
// before the left one, and how many
// bigger numbers sit after the right
// one — then multiply and add them up.

#include <vector>
using namespace std;

class Solution {
public:
    long long countQuadruplets(vector<int>& nums) {
        int n = (int)nums.size();
        long long ans = 0;
        vector<int> freq(n + 2, 0), pref(n + 2, 0);
        for (int j = 0; j < n; j++) {
            for (int v = 1; v <= n; v++) pref[v] = pref[v - 1] + freq[v];
            int suf = 0;
            for (int k = n - 1; k > j; k--) {
                if (nums[k] < nums[j]) ans += (long long)pref[nums[k] - 1] * suf;
                if (nums[k] > nums[j]) suf++;
            }
            freq[nums[j]]++;
        }
        return ans;
    }
};
