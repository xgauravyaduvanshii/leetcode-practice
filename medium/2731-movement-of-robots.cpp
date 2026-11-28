// LeetCode 2731. Movement of Robots — Medium
// https://leetcode.com/problems/movement-of-robots/
// Submission 2205217230 — Accepted, C++
//
// My thinking: same idea as the Python version — collisions
// are equivalent to passing through, so sort the final
// positions and sum pairwise distances; every term is reduced
// modulo 1e9+7 as it is added, so the 64-bit arithmetic never
// overflows.
class Solution {
public:
    int sumDistance(vector<int>& nums, string s, int d) {
        const long long MOD = 1000000007LL;
        int n = nums.size();
        vector<long long> pos(n);
        for (int i = 0; i < n; i++) {
            pos[i] = (long long)nums[i] + (s[i] == 'R' ? d : -d);
        }
        sort(pos.begin(), pos.end());
        long long ans = 0;
        for (int i = 0; i < n; i++) {
            long long p = ((pos[i] % MOD) + MOD) % MOD;
            long long c = (((2LL * i - n + 1) % MOD) + MOD) % MOD;
            ans = (ans + p * c) % MOD;
        }
        return (int)ans;
    }
};
