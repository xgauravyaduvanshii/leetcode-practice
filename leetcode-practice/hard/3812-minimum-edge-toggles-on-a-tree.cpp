// LeetCode 3812. Minimum Edge Toggles on a Tree — Hard
// https://leetcode.com/problems/minimum-edge-toggles-on-a-tree/
// Submission 2203190973 — Accepted, C++
#include <algorithm>
#include <string>
#include <tuple>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> minimumFlips(int n, vector<vector<int>>& edges, string start, string target) {
        // My thinking: toggling an edge flips both of its ends,
        // so a node ends up flipped exactly when an odd number
        // of its incident edges are toggled. On a tree the
        // choice is forced from the leaves up: a leaf that
        // still mismatches its target can only be fixed by
        // toggling the edge to its parent, and that toggle
        // flips the parent's remaining need as well. So I
        // root the tree at 0 and walk it in postorder; each
        // node reports whether the edge to its parent must be
        // toggled, which is its own mismatch xored with the
        // toggles already chosen on the edges to its children.
        // The root has no parent edge, so if it still needs a
        // flip the transformation is impossible. The forced
        // choices are the unique minimum-length solution, and
        // sorting the chosen indices gives the required order.
        // I use an explicit stack because a chain of 10^5
        // nodes would overflow the call stack.
        vector<vector<pair<int, int>>> g(n);
        for (int i = 0; i < n - 1; ++i) {
            int a = edges[i][0], b = edges[i][1];
            g[a].push_back({b, i});
            g[b].push_back({a, i});
        }
        vector<int> ans;
        vector<char> need(n, 0);
        vector<tuple<int, int, int>> st;
        st.push_back({0, -1, 0});
        while (!st.empty()) {
            auto [a, fa, state] = st.back();
            st.pop_back();
            if (state == 0) {
                st.push_back({a, fa, 1});
                for (auto [b, i] : g[a]) {
                    if (b != fa) st.push_back({b, a, 0});
                }
            } else {
                bool rev = start[a] != target[a];
                for (auto [b, i] : g[a]) {
                    if (b != fa && need[b]) {
                        ans.push_back(i);
                        rev = !rev;
                    }
                }
                need[a] = rev;
            }
        }
        if (need[0]) return {-1};
        sort(ans.begin(), ans.end());
        return ans;
    }
};
