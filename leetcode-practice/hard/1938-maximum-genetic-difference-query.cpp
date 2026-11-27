// LeetCode 1938. Maximum Genetic Difference Query — Hard
// https://leetcode.com/problems/maximum-genetic-difference-query/
// Submission 2201254544 — Accepted, C++
//
// My thinking: I walk the family tree keeping a
// binary trie of the ancestors' values — at each
// node I read off the best xor from the trie, then
// add the node, visit its children, and take it
// back out again.

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    struct Node {
        int child[2];
        int cnt;
        Node() {
            child[0] = child[1] = -1;
            cnt = 0;
        }
    };
    vector<Node> trie;

    void addNum(int num, int delta) {
        int node = 0;
        trie[node].cnt += delta;
        for (int b = 29; b >= 0; --b) {
            int bit = (num >> b) & 1;
            if (trie[node].child[bit] == -1) {
                trie[node].child[bit] = (int)trie.size();
                trie.emplace_back();
            }
            node = trie[node].child[bit];
            trie[node].cnt += delta;
        }
    }

    int queryMaxXor(int num) {
        int node = 0;
        int res = 0;
        for (int b = 29; b >= 0; --b) {
            int bit = (num >> b) & 1;
            int want = 1 - bit;
            int nxt = trie[node].child[want];
            if (nxt != -1 && trie[nxt].cnt > 0) {
                res |= (1 << b);
                node = nxt;
            } else {
                node = trie[node].child[bit];
            }
        }
        return res;
    }

    vector<int> maxGeneticDifference(vector<int>& parents, vector<vector<int>>& queries) {
        int n = (int)parents.size();
        vector<vector<int>> children(n);
        int root = -1;
        for (int i = 0; i < n; ++i) {
            if (parents[i] == -1) root = i;
            else children[parents[i]].push_back(i);
        }
        vector<vector<pair<int,int>>> byNode(n);
        for (int i = 0; i < (int)queries.size(); ++i) {
            byNode[queries[i][0]].push_back({i, queries[i][1]});
        }
        vector<int> ans(queries.size(), 0);
        trie.reserve(1 << 18);
        trie.emplace_back();
        vector<pair<int,int>> stack;
        stack.push_back({root, 0});
        while (!stack.empty()) {
            auto [node, state] = stack.back();
            stack.pop_back();
            if (state == 0) {
                addNum(node, 1);
                for (auto [qi, val] : byNode[node]) ans[qi] = queryMaxXor(val);
                stack.push_back({node, 1});
                for (int i = (int)children[node].size() - 1; i >= 0; --i)
                    stack.push_back({children[node][i], 0});
            } else {
                addNum(node, -1);
            }
        }
        return ans;
    }
};
