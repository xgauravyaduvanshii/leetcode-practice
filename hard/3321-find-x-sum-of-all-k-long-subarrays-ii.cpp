// LeetCode 3321. Find X-Sum of All K-Long Subarrays II — Hard
// https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-ii/
// Submission 2202371618 — Accepted, C++
//
// My thinking: in each window I keep the x most frequent distinct values
// (ties broken by the bigger value) in a "top" set and the rest in a "rest"
// set, with the x-sum maintained incrementally. Both sets are ordered by
// (frequency, value), so the worst of top and the best of rest are found in
// O(log n). When a value's frequency changes I move it out of whichever set
// it is in, insert the fresh entry into rest, and rebalance — refill top
// from rest, swap whenever the best of rest beats the worst of top, and
// shrink top back to x.
class Solution {
public:
    vector<long long> findXSum(vector<int>& nums, int k, int x) {
        unordered_map<int, int> freq;
        unordered_map<int, int> loc;  // 0 = absent, 1 = top, 2 = rest
        set<pair<int, int>> top, rest;  // (frequency, value), ascending
        long long sum = 0;

        auto rebalance = [&]() {
            while ((int)top.size() < x && !rest.empty()) {
                auto it = prev(rest.end());
                top.insert(*it);
                sum += (long long)it->first * it->second;
                loc[it->second] = 1;
                rest.erase(it);
            }
            while (!top.empty() && !rest.empty() && *rest.rbegin() > *top.begin()) {
                auto hi = *rest.rbegin();
                auto lo = *top.begin();
                rest.erase(prev(rest.end()));
                top.erase(top.begin());
                top.insert(hi);
                rest.insert(lo);
                sum += (long long)hi.first * hi.second - (long long)lo.first * lo.second;
                loc[hi.second] = 1;
                loc[lo.second] = 2;
            }
            while ((int)top.size() > x) {
                auto lo = *top.begin();
                top.erase(top.begin());
                rest.insert(lo);
                sum -= (long long)lo.first * lo.second;
                loc[lo.second] = 2;
            }
        };

        auto change = [&](int v, int delta) {
            int old = freq.count(v) ? freq[v] : 0;
            if (loc.count(v) && loc[v] == 1) {
                top.erase({old, v});
                sum -= (long long)old * v;
            } else if (loc.count(v) && loc[v] == 2) {
                rest.erase({old, v});
            }
            int nw = old + delta;
            if (nw > 0) {
                freq[v] = nw;
                rest.insert({nw, v});
                loc[v] = 2;
            } else {
                freq.erase(v);
                loc.erase(v);
            }
            rebalance();
        };

        int n = nums.size();
        vector<long long> ans;
        for (int i = 0; i < n; i++) {
            change(nums[i], 1);
            if (i >= k) change(nums[i - k], -1);
            if (i >= k - 1) ans.push_back(sum);
        }
        return ans;
    }
};
