// LeetCode 2680. Maximum OR — Medium
// https://leetcode.com/problems/maximum-or/
// Submission 2205191381 — Accepted, C++
//
// My thinking: same idea as the Python version — all k doublings
// go on one element, so try each element boosted by k shifts and
// OR it with the prefix OR before it and the suffix OR after it.
class Solution {
public:
    long long maximumOr(vector<int>& nums, int k) {
        int n = nums.size();
        vector<long long> pre(n + 1, 0), suf(n + 1, 0);
        for (int i = 0; i < n; i++) pre[i + 1] = pre[i] | nums[i];
        for (int i = n - 1; i >= 0; i--) suf[i] = suf[i + 1] | nums[i];
        long long ans = 0;
        for (int i = 0; i < n; i++) {
            ans = max(ans, ((long long)nums[i] << k) | pre[i] | suf[i + 1]);
        }
        return ans;
    }
};
