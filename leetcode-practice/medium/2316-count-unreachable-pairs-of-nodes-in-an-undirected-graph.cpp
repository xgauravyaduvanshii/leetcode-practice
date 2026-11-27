// LeetCode 2316. Count Unreachable Pairs of Nodes in an Undirected Graph — Medium
// https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/
// Submission 2204680195 — Accepted, C++
//
// My thinking: same idea as the Python version — union-find for the
// components, then count cross-component pairs by multiplying each
// component's size by the nodes still unseen.
class Solution {
public:
    long long countPairs(int n, vector<vector<int>>& edges) {
        vector<int> parent(n);
        iota(parent.begin(), parent.end(), 0);
        function<int(int)> find = [&](int x) {
            while (parent[x] != x) {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            return x;
        };
        for (auto& e : edges) {
            int ra = find(e[0]), rb = find(e[1]);
            if (ra != rb) parent[ra] = rb;
        }
        unordered_map<int, long long> cnt;
        for (int i = 0; i < n; i++) cnt[find(i)]++;
        long long ans = 0, remaining = n;
        for (auto& [root, sz] : cnt) {
            remaining -= sz;
            ans += sz * remaining;
        }
        return ans;
    }
};
