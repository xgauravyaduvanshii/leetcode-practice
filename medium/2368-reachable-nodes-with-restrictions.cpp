// LeetCode 2368. Reachable Nodes With Restrictions — Medium
// https://leetcode.com/problems/reachable-nodes-with-restrictions/
// Submission 2204752364 — Accepted, C++
//
// My thinking: same idea as the Python version — a stack walk from node
// 0 that never enters a restricted node or a visited one; the count of
// visited nodes is the answer.
class Solution {
public:
    int reachableNodes(int n, vector<vector<int>>& edges, vector<int>& restricted) {
        vector<vector<int>> adj(n);
        for (auto& e: edges) {
            adj[e[0]].push_back(e[1]);
            adj[e[1]].push_back(e[0]);
        }
        vector<char> banned(n, 0);
        for (int r: restricted) banned[r] = 1;
        vector<char> seen(n, 0);
        seen[0] = 1;
        vector<int> stack = {0};
        int count = 0;
        while (!stack.empty()) {
            int u = stack.back();
            stack.pop_back();
            count++;
            for (int v: adj[u]) {
                if (!seen[v] && !banned[v]) {
                    seen[v] = 1;
                    stack.push_back(v);
                }
            }
        }
        return count;
    }
};
