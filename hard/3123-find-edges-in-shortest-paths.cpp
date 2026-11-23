// LeetCode 3123. Find Edges in Shortest Paths — Hard
// https://leetcode.com/problems/find-edges-in-shortest-paths/
// Submission 2202016147 — Accepted, C++
//
// My thinking: an edge lies on a
// shortest path exactly when going
// through it from 0 and then on to
// n - 1 costs the same as the shortest
// distance. I run Dijkstra from both
// ends once and test every edge against
// that sum.

class Solution {
public:
    vector<bool> findAnswer(int n, vector<vector<int>>& edges) {
        vector<vector<pair<int, long long>>> adj(n);
        for (auto &e : edges) {
            adj[e[0]].push_back({e[1], e[2]});
            adj[e[1]].push_back({e[0], e[2]});
        }
        auto dijkstra = [&](int src) {
            vector<long long> dist(n, (long long)4e18);
            dist[src] = 0;
            using pli = pair<long long, int>;
            priority_queue<pli, vector<pli>, greater<pli>> pq;
            pq.push({0, src});
            while (!pq.empty()) {
                auto [d, u] = pq.top();
                pq.pop();
                if (d != dist[u]) continue;
                for (auto [v, w] : adj[u]) {
                    if (dist[v] > d + w) {
                        dist[v] = d + w;
                        pq.push({dist[v], v});
                    }
                }
            }
            return dist;
        };
        auto d0 = dijkstra(0);
        auto d1 = dijkstra(n - 1);
        long long total = d0[n - 1];
        vector<bool> ans;
        ans.reserve(edges.size());
        for (auto &e : edges) {
            long long a = e[0], b = e[1], w = e[2];
            bool ok = (d0[a] + w + d1[b] == total) || (d0[b] + w + d1[a] == total);
            ans.push_back(ok);
        }
        return ans;
    }
};
