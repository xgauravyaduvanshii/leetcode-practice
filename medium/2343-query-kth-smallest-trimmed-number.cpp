// LeetCode 2343. Query Kth Smallest Trimmed Number — Medium
// https://leetcode.com/problems/query-kth-smallest-trimmed-number/
// Submission 2204719933 — Accepted, C++
//
// My thinking: same idea as the Python version — for each query sort the
// indices by the trimmed suffix, ties broken by the smaller index. The
// trimmed strings are precomputed once per query instead of being rebuilt
// inside the comparator (that version timed out), which keeps the sort fast.
class Solution {
public:
    vector<int> smallestTrimmedNumbers(vector<string>& nums, vector<vector<int>>& queries) {
        int n = nums.size();
        vector<int> ans;
        vector<int> idx(n);
        for (auto& q : queries) {
            int k = q[0], trim = q[1];
            vector<string> t(n);
            for (int i = 0; i < n; i++) t[i] = nums[i].substr(nums[i].size() - trim);
            iota(idx.begin(), idx.end(), 0);
            sort(idx.begin(), idx.end(), [&](int a, int b) {
                if (t[a] != t[b]) return t[a] < t[b];
                return a < b;
            });
            ans.push_back(idx[k - 1]);
        }
        return ans;
    }
};
