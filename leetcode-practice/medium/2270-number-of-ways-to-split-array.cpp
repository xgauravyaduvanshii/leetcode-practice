// LeetCode 2270. Number of Ways to Split Array — Medium
// https://leetcode.com/problems/number-of-ways-to-split-array/
// Submission 2204610790 — Accepted, C++
//
// My thinking: same idea as the Python version — one pass with a running
// left sum, counting splits where left >= total - left. The sums are kept
// in a 64-bit integer because they can overflow 32 bits.
class Solution {
public:
    int waysToSplitArray(vector<int>& nums) {
        long long total = 0;
        for (int x : nums) total += x;
        long long left = 0;
        int ans = 0;
        for (int i = 0; i + 1 < (int)nums.size(); i++) {
            left += nums[i];
            if (left >= total - left) ans++;
        }
        return ans;
    }
};
