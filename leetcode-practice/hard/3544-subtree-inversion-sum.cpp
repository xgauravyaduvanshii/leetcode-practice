// LeetCode 3544. Subtree Inversion Sum — Hard
// https://leetcode.com/problems/subtree-inversion-sum/
// Submission 2202822234 — Accepted, C++
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

class Solution {
public:
    int subtreeInversionSum(vector<vector<int>>& edges, vector<int>& nums, int k) {
        // My thinking: inverting a node flips the sign of its whole
        // subtree, so a node's final sign is the parity of the
        // inverted nodes on the path from the root to it. Two inverted
        // nodes on one root-to-leaf path must be at least k apart, so
        // for each node I keep the distance to the nearest inverted
        // ancestor (capped at k, where k means far enough or none)
        // and the parity of inverted ancestors. Not inverting passes
        // the distance down plus one; inverting is only allowed when
        // the distance is already k, resets it to 1 below, and flips
        // the parity. The children are independent once those two
        // numbers are fixed, so a bottom-up pass over the tree fills
        // the table.
        int n = nums.size();
        vector<vector<int>> children(n);
        vector<vector<int>> adj(n);
        for (auto& e : edges) {
            adj[e[0]].push_back(e[1]);
            adj[e[1]].push_back(e[0]);
        }
        vector<int> parent(n, -1), order;
        order.reserve(n);
        vector<int> stack = {0};
        parent[0] = -2;
        while (!stack.empty()) {
            int u = stack.back(); stack.pop_back();
            order.push_back(u);
            for (int v : adj[u]) if (parent[v] == -1) {
                parent[v] = u;
                children[u].push_back(v);
                stack.push_back(v);
            }
        }
        const long long NEG = LLONG_MIN / 4;
        vector<vector<array<long long, 2>>> f(n);
        for (int ui = n - 1; ui >= 0; ui--) {
            int u = order[ui];
            long long S[2][55] = {};
            for (int c : children[u]) {
                for (int d = 1; d <= k; d++) {
                    S[0][d] += f[c][d][0];
                    S[1][d] += f[c][d][1];
                }
            }
            f[u].assign(k + 1, {NEG, NEG});
            for (int d = 1; d <= k; d++) {
                for (int p = 0; p <= 1; p++) {
                    long long sign = (p == 0) ? 1 : -1;
                    long long best = (long long)nums[u] * sign + S[p][min(d + 1, k)];
                    if (d == k) {
                        best = max(best, (long long)nums[u] * (-sign) + S[1 - p][1]);
                    }
                    f[u][d][p] = best;
                }
            }
        }
        return (int)f[0][k][0];
    }
};
