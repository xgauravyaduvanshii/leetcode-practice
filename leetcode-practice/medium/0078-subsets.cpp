// LeetCode 78. Subsets — Medium
// https://leetcode.com/problems/subsets/
// Submission 2203847046 — Accepted, C++

// My thinking: I build every subset with backtracking, deciding for
// each number in turn whether to include it. At every step of the
// recursion the current selection is itself a valid subset, so I
// record it before branching further, which produces all 2^n subsets
// exactly once.
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> ans;
        vector<int> current;
        backtrack(nums, 0, current, ans);
        return ans;
    }

    void backtrack(vector<int>& nums, int start, vector<int>& current,
                   vector<vector<int>>& ans) {
        ans.push_back(current);
        for (int i = start; i < (int)nums.size(); i++) {
            current.push_back(nums[i]);
            backtrack(nums, i + 1, current, ans);
            current.pop_back();
        }
    }
};
