// LeetCode 3548. Equal Sum Grid Partition II — Hard
// https://leetcode.com/problems/equal-sum-grid-partition-ii/
// Submission 2202837168 — Accepted, C++
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    bool canPartitionGrid(vector<vector<int>>& grid) {
        // My thinking: a cut splits the grid into two rectangles. If
        // their sums already match, that cut works. Otherwise the
        // larger side must lose exactly the difference by dropping
        // one cell, and the rest of that side must stay connected.
        // A rectangle with both sides at least 2 stays connected
        // after any single cell is removed, so there I only need a
        // cell with the right value — I keep running frequency maps
        // while sweeping the cuts. A one-row or one-column side only
        // survives losing an end cell, so there I check just the two
        // ends. A single cell can never be dropped.
        int m = grid.size(), n = grid[0].size();
        long long total = 0;
        for (auto& r : grid) for (int v : r) total += v;
        vector<long long> pref(m + 1, 0);
        for (int i = 0; i < m; i++) {
            long long s = 0;
            for (int v : grid[i]) s += v;
            pref[i + 1] = pref[i] + s;
        }
        unordered_map<int, int> topFreq, botFreq;
        for (auto& r : grid) for (int v : r) botFreq[v]++;
        for (int i = 0; i < m - 1; i++) {
            for (int v : grid[i]) {
                topFreq[v]++;
                if (--botFreq[v] == 0) botFreq.erase(v);
            }
            long long sTop = pref[i + 1], sBot = total - sTop;
            if (sTop == sBot) return true;
            if (sTop > sBot) {
                if (removable(grid, 0, i, 0, n - 1, (int)(sTop - sBot), topFreq)) return true;
            } else {
                if (removable(grid, i + 1, m - 1, 0, n - 1, (int)(sBot - sTop), botFreq)) return true;
            }
        }
        vector<long long> prefc(n + 1, 0);
        for (int j = 0; j < n; j++) {
            long long s = 0;
            for (int i = 0; i < m; i++) s += grid[i][j];
            prefc[j + 1] = prefc[j] + s;
        }
        unordered_map<int, int> leftFreq, rightFreq;
        for (auto& r : grid) for (int v : r) rightFreq[v]++;
        for (int j = 0; j < n - 1; j++) {
            for (int i = 0; i < m; i++) {
                int v = grid[i][j];
                leftFreq[v]++;
                if (--rightFreq[v] == 0) rightFreq.erase(v);
            }
            long long sLeft = prefc[j + 1], sRight = total - sLeft;
            if (sLeft == sRight) return true;
            if (sLeft > sRight) {
                if (removable(grid, 0, m - 1, 0, j, (int)(sLeft - sRight), leftFreq)) return true;
            } else {
                if (removable(grid, 0, m - 1, j + 1, n - 1, (int)(sRight - sLeft), rightFreq)) return true;
            }
        }
        return false;
    }

private:
    static bool removable(vector<vector<int>>& grid, int r1, int r2, int c1, int c2,
                          int diff, unordered_map<int, int>& freq) {
        int h = r2 - r1 + 1, w = c2 - c1 + 1;
        if (h == 1 && w == 1) return false;
        if (h == 1) return grid[r1][c1] == diff || grid[r1][c2] == diff;
        if (w == 1) return grid[r1][c1] == diff || grid[r2][c1] == diff;
        auto it = freq.find(diff);
        return it != freq.end() && it->second > 0;
    }
};
