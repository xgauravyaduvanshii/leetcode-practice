#include <array>
#include <queue>
#include <vector>
using namespace std;

class Solution {
public:
    int shortestPath(vector<vector<int>>& grid, int k) {
        // My thinking: breadth-first search over (row, column,
        // obstacles used) — the first time we reach the target
        // is the shortest walk, and using fewer eliminations
        // to reach the same cell is never worse.
        int rows = grid.size(), cols = grid[0].size();
        if (rows == 1 && cols == 1) return 0;
        if (k >= rows + cols - 2) return rows + cols - 2;
        vector<vector<int>> best(rows, vector<int>(cols, -1));
        best[0][0] = 0;
        queue<array<int, 4>> q;
        q.push({0, 0, 0, 0});
        const int dirs[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (!q.empty()) {
            auto [r, c, used, steps] = q.front();
            q.pop();
            for (auto [dr, dc] : dirs) {
                int nr = r + dr, nc = c + dc;
                if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) continue;
                int newUsed = used + grid[nr][nc];
                if (newUsed > k) continue;
                if (best[nr][nc] != -1 && best[nr][nc] <= newUsed) continue;
                if (nr == rows - 1 && nc == cols - 1) return steps + 1;
                best[nr][nc] = newUsed;
                q.push({nr, nc, newUsed, steps + 1});
            }
        }
        return -1;
    }
};
