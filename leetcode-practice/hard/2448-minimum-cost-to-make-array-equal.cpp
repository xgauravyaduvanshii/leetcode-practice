// LeetCode 2448. Minimum Cost to Make Array Equal — Hard
// https://leetcode.com/problems/minimum-cost-to-make-array-equal/
// Submission 2201747599 — Accepted, C++
//
// My thinking: the cheapest target sits
// where the cost stops falling — the cost
// is convex, so I binary-search the point
// where making everything one bigger
// starts costing more than it saves.

#include <algorithm>
#include <cmath>
#include <vector>
using namespace std;

class Solution {
public:
    long long minCost(vector<int>& nums, vector<int>& cost) {
        int n = nums.size();
        vector<pair<int, int>> pairs;
        for (int i = 0; i < n; i++) pairs.push_back({nums[i], cost[i]});
        sort(pairs.begin(), pairs.end());
        auto total = [&](long long target) {
            long long s = 0;
            for (auto& [x, c] : pairs) s += llabs((long long)x - target) * c;
            return s;
        };
        long long lo = *min_element(nums.begin(), nums.end());
        long long hi = *max_element(nums.begin(), nums.end());
        while (lo < hi) {
            long long mid = (lo + hi) / 2;
            if (total(mid) <= total(mid + 1)) hi = mid;
            else lo = mid + 1;
        }
        return total(lo);
    }
};
