// LeetCode 2732. Find a Good Subset of the Matrix — Hard
// https://leetcode.com/problems/find-a-good-subset-of-the-matrix/
// Submission 2201877992 — Accepted, C++
//
// My thinking: a single row of all
// zeroes is already good on its own,
// and two rows that never share a 1 are
// good together — and if neither of
// those exists, no larger group can be
// good either, because every row would
// still clash with another.

#include <vector>
using namespace std;

class Solution {
public:
    vector<int> goodSubsetofBinaryMatrix(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        vector<long long> masks(m, 0);
        for (int i = 0; i < m; i++) {
            long long mask = 0;
            for (int j = 0; j < n; j++) {
                if (grid[i][j]) mask |= 1LL << j;
            }
            masks[i] = mask;
            if (mask == 0) return {i};
        }
        for (int i = 0; i < m; i++) {
            for (int j = i + 1; j < m; j++) {
                if ((masks[i] & masks[j]) == 0) return {i, j};
            }
        }
        return {};
    }
};
