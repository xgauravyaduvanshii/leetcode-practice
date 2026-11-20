#include <vector>
#include <deque>
#include <climits>
using namespace std;

class Solution {
public:
    int minCost(vector<vector<int>>& grid) {
        // My thinking: walking with the arrow is free, walking
        // against it costs one change — so a 0-1 breadth-first
        // search finds the cheapest route to the far corner.
        int rows = grid.size(), cols = grid[0].size();
        const int INF = INT_MAX;
        vector<vector<int>> dist(rows, vector<int>(cols, INF));
        dist[0][0] = 0;
        deque<pair<int, int>> q;
        q.push_front({0, 0});
        const int dirs[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        while (!q.empty()) {
            auto [r, c] = q.front();
            q.pop_front();
            for (int d = 0; d < 4; d++) {
                int nr = r + dirs[d][0], nc = c + dirs[d][1];
                if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) continue;
                int cost = dist[r][c] + (grid[r][c] == d + 1 ? 0 : 1);
                if (cost < dist[nr][nc]) {
                    dist[nr][nc] = cost;
                    if (grid[r][c] == d + 1) q.push_front({nr, nc});
                    else q.push_back({nr, nc});
                }
            }
        }
        return dist[rows - 1][cols - 1];
    }
};
