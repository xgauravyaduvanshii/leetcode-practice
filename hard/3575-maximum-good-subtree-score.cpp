// LeetCode 3575. Maximum Good Subtree Score — Hard
// https://leetcode.com/problems/maximum-good-subtree-score/
// Submission 2202855266 — Accepted, C++
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

class Solution {
public:
    int goodSubtreeSum(vector<int>& vals, vector<int>& par) {
        // My thinking: a value whose own decimal digits repeat can
        // never be picked, so it gets mask -1. Otherwise each node
        // carries a digit mask, and a good subset is a choice of
        // nodes whose masks are pairwise disjoint. I do a tree DP
        // keyed by mask: merge the children's tables (only disjoint
        // masks combine), then optionally add this node itself, and
        // the node's best is the largest entry in its table. The
        // answer is the sum of every node's best, modulo 1e9+7.
        const int MOD = 1000000007;
        int n = vals.size();
        vector<vector<int>> children(n);
        for (int i = 1; i < n; i++) children[par[i]].push_back(i);
        vector<int> masks(n);
        for (int i = 0; i < n; i++) masks[i] = digitMask(vals[i]);
        long long total = 0;
        dfs(0, children, vals, masks, total, MOD);
        return (int)(total % MOD);
    }

private:
    static int digitMask(int x) {
        int mask = 0;
        string s = to_string(x);
        for (char ch : s) {
            int d = ch - '0';
            if (mask & (1 << d)) return -1;
            mask |= 1 << d;
        }
        return mask;
    }

    unordered_map<int, long long> dfs(int u, vector<vector<int>>& children,
                                      vector<int>& vals, vector<int>& masks,
                                      long long& total, int MOD) {
        unordered_map<int, long long> dp;
        dp[0] = 0;
        for (int v : children[u]) {
            auto child = dfs(v, children, vals, masks, total, MOD);
            unordered_map<int, long long> nxt;
            for (auto& [m1, s1] : dp) {
                for (auto& [m2, s2] : child) {
                    if ((m1 & m2) == 0) {
                        int nm = m1 | m2;
                        auto it = nxt.find(nm);
                        if (it == nxt.end() || s1 + s2 > it->second) nxt[nm] = s1 + s2;
                    }
                }
            }
            dp = move(nxt);
        }
        int mu = masks[u];
        if (mu != -1) {
            unordered_map<int, long long> extra;
            for (auto& [m, s] : dp) {
                if ((m & mu) == 0) {
                    int nm = m | mu;
                    auto it = extra.find(nm);
                    if (it == extra.end() || s + vals[u] > it->second) extra[nm] = s + vals[u];
                }
            }
            for (auto& [nm, s] : extra) {
                auto it = dp.find(nm);
                if (it == dp.end() || s > it->second) dp[nm] = s;
            }
        }
        long long best = 0;
        for (auto& [m, s] : dp) best = max(best, s);
        total = (total + best) % MOD;
        return dp;
    }
};
