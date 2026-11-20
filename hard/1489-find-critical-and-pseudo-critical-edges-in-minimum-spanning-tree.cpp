#include <vector>
#include <algorithm>
#include <numeric>
#include <functional>
#include <climits>
using namespace std;

class Solution {
public:
    vector<vector<int>> findCriticalAndPseudoCriticalEdges(int n, vector<vector<int>>& edges) {
        // My thinking: an edge is critical if the cheapest
        // tree without it costs more — and pseudo-critical
        // if a cheapest tree can still be built with it in.
        int m = edges.size();
        vector<int> order(m);
        iota(order.begin(), order.end(), 0);
        sort(order.begin(), order.end(), [&](int a, int b) { return edges[a][2] < edges[b][2]; });
        auto mstWeight = [&](int skip, int force) -> int {
            vector<int> parent(n);
            iota(parent.begin(), parent.end(), 0);
            function<int(int)> find = [&](int x) {
                while (parent[x] != x) {
                    parent[x] = parent[parent[x]];
                    x = parent[x];
                }
                return x;
            };
            int total = 0, used = 0;
            if (force != -1) {
                int u = edges[force][0], v = edges[force][1], w = edges[force][2];
                int ru = find(u), rv = find(v);
                parent[ru] = rv;
                total += w;
                used++;
            }
            for (int i : order) {
                if (i == skip || i == force) continue;
                int u = edges[i][0], v = edges[i][1], w = edges[i][2];
                int ru = find(u), rv = find(v);
                if (ru != rv) {
                    parent[ru] = rv;
                    total += w;
                    used++;
                }
            }
            return used == n - 1 ? total : INT_MAX;
        };
        int base = mstWeight(-1, -1);
        vector<int> critical, pseudo;
        for (int i = 0; i < m; i++) {
            if (mstWeight(i, -1) > base) critical.push_back(i);
            else if (mstWeight(-1, i) == base) pseudo.push_back(i);
        }
        return {critical, pseudo};
    }
};
