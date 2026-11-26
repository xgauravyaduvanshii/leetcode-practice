// LeetCode 3985. Palindromic Subarray Sum — Hard
// https://leetcode.com/problems/palindromic-subarray-sum/
// Submission 2203497909 — Accepted, C++
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    long long getSum(vector<int>& nums) {
        // My thinking: every number is positive, so for a
        // fixed centre a longer palindrome always has a
        // larger sum — the best palindrome at that centre
        // is the longest one. Manacher's algorithm finds
        // the longest odd and even palindrome at every
        // centre in linear time, and prefix sums give each
        // one's sum in O(1). A single element is always a
        // palindrome, so the answer is at least max(nums).
        // The sum can reach 10^5 * 10^9, so prefix sums
        // and the answer are long long.
        int n = (int)nums.size();
        vector<long long> pref(n + 1, 0);
        for (int i = 0; i < n; ++i) pref[i + 1] = pref[i] + nums[i];
        vector<int> d1(n, 0);
        int l = 0, r = -1;
        for (int i = 0; i < n; ++i) {
            int k = (i > r) ? 1 : min(d1[l + r - i], r - i + 1);
            while (i - k >= 0 && i + k < n && nums[i - k] == nums[i + k]) ++k;
            d1[i] = k;
            if (i + k - 1 > r) {
                l = i - k + 1;
                r = i + k - 1;
            }
        }
        vector<int> d2(n, 0);
        l = 0, r = -1;
        for (int i = 0; i < n; ++i) {
            int k = (i > r) ? 0 : min(d2[l + r - i + 1], r - i + 1);
            while (i - k - 1 >= 0 && i + k < n && nums[i - k - 1] == nums[i + k]) ++k;
            d2[i] = k;
            if (i + k - 1 > r) {
                l = i - k;
                r = i + k - 1;
            }
        }
        long long ans = *max_element(nums.begin(), nums.end());
        for (int i = 0; i < n; ++i) {
            if (d1[i] > 0) ans = max(ans, pref[i + d1[i]] - pref[i - d1[i] + 1]);
            if (d2[i] > 0) ans = max(ans, pref[i + d2[i]] - pref[i - d2[i]]);
        }
        return ans;
    }
};
