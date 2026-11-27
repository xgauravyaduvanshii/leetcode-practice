// LeetCode 2382. Maximum Segment Sum After Removals — Hard
// https://leetcode.com/problems/maximum-segment-sum-after-removals/
// Submission 2201708873 — Accepted, C++
//
// My thinking: taking pieces away is hard
// to track, so I put them back in reverse
// — each return joins its neighbours into
// one segment, and the biggest segment I
// have seen before the return is the
// answer for that removal.

#include <numeric>
#include <vector>
using namespace std;

class Solution {
public:
    vector<long long> maximumSegmentSum(vector<int>& nums, vector<int>& removeQueries) {
        int n = nums.size();
        vector<int> parent(n);
        iota(parent.begin(), parent.end(), 0);
        vector<long long> seg(n, 0);
        vector<char> active(n, 0);
        function<int(int)> find = [&](int x) {
            while (parent[x] != x) {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            return x;
        };
        auto unite = [&](int a, int b) {
            int ra = find(a), rb = find(b);
            if (ra == rb) return ra;
            parent[rb] = ra;
            seg[ra] += seg[rb];
            return ra;
        };
        vector<long long> ans(n, 0);
        long long best = 0;
        for (int i = n - 1; i >= 0; i--) {
            ans[i] = best;
            int idx = removeQueries[i];
            active[idx] = 1;
            seg[idx] = nums[idx];
            if (idx > 0 && active[idx - 1]) unite(idx, idx - 1);
            if (idx + 1 < n && active[idx + 1]) unite(idx, idx + 1);
            best = max(best, seg[find(idx)]);
        }
        return ans;
    }
};
