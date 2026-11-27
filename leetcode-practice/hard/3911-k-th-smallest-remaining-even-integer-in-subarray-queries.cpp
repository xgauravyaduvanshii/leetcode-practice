// LeetCode 3911. K-th Smallest Remaining Even Integer in Subarray Queries — Hard
// https://leetcode.com/problems/k-th-smallest-remaining-even-integer-in-subarray-queries/
// Submission 2203390778 — Accepted, C++
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<int> kthRemainingInteger(vector<int>& nums, vector<vector<int>>& queries) {
        // My thinking: the positive evens are 2, 4, 6, ...
        // and a query deletes only the even values inside
        // nums[l..r]. Collect those evens once, sorted,
        // together with their positions. For a query let
        // c(m) be how many of the deleted evens are at most
        // 2m — an upper_bound over the slice of evens whose
        // positions fall in [l, r], minus the slice's left
        // offset, since upper_bound returns an insertion
        // position, not a count. The remaining evens up to
        // 2m number m - c(m), which never decreases as m
        // grows (c grows by at most 1 per step) and climbs
        // by steps of 0 or 1, so it hits k exactly at some
        // m. That m lies between k and k plus the number of
        // deleted evens, so binary search that range for
        // the smallest m with m - c(m) >= k; the answer is
        // 2m.
        vector<int> evenVals;
        vector<int> evenPos;
        for (int i = 0; i < (int)nums.size(); i++) {
            if (nums[i] % 2 == 0) {
                evenVals.push_back(nums[i]);
                evenPos.push_back(i);
            }
        }
        vector<int> ans;
        for (auto& q : queries) {
            int l = q[0], r = q[1];
            long long k = q[2];
            int lo = lower_bound(evenPos.begin(), evenPos.end(), l) - evenPos.begin();
            int hi = upper_bound(evenPos.begin(), evenPos.end(), r) - evenPos.begin();
            long long cnt = hi - lo;
            long long a = k, b = k + cnt;
            while (a < b) {
                long long mid = a + (b - a) / 2;
                long long removed = upper_bound(evenVals.begin() + lo, evenVals.begin() + hi, 2 * mid) - (evenVals.begin() + lo);
                if (mid - removed >= k) {
                    b = mid;
                } else {
                    a = mid + 1;
                }
            }
            ans.push_back((int)(2 * a));
        }
        return ans;
    }
};
