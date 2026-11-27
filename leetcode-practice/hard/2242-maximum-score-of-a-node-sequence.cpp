// LeetCode 2242. Maximum Score of a Node Sequence — Hard
// https://leetcode.com/problems/maximum-score-of-a-node-sequence/
// Submission 2201632064 — Accepted, C++
//
// My thinking: a four-node run is really a
// middle edge with its best neighbours on
// each side — I keep each node's three
// highest-scoring neighbours and try every
// pairing across every middle edge.

#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maximumScore(vector<int>& scores, vector<vector<int>>& edges) {
        int n = scores.size();
        vector<vector<int>> adj(n);
        for (auto& e : edges) {
            adj[e[0]].push_back(e[1]);
            adj[e[1]].push_back(e[0]);
        }
        vector<vector<int>> top(n);
        for (int u = 0; u < n; u++) {
            auto& neigh = adj[u];
            sort(neigh.begin(), neigh.end(), [&](int a, int b) {
                return scores[a] > scores[b];
            });
            if ((int)neigh.size() > 3) neigh.resize(3);
            top[u] = neigh;
        }
        int ans = -1;
        for (auto& e : edges) {
            int a = e[0], b = e[1];
            for (int x : top[a]) {
                if (x == b) continue;
                for (int y : top[b]) {
                    if (y == a || y == x) continue;
                    ans = max(ans, scores[x] + scores[a] + scores[b] + scores[y]);
                }
            }
        }
        return ans;
    }
};
