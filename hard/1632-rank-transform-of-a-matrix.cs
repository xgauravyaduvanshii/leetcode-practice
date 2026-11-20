using System;
using System.Collections.Generic;

public class Solution {
    public int[][] MatrixRankTransform(int[][] matrix) {
        // My thinking: ranks grow with the values — so handle
        // each value on its own, join equal cells that share a
        // row or column, and give the whole group one rank.
        int m = matrix.Length, n = matrix[0].Length;
        var cells = new SortedDictionary<int, List<(int, int)>>();
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++) {
                if (!cells.ContainsKey(matrix[i][j])) cells[matrix[i][j]] = new List<(int, int)>();
                cells[matrix[i][j]].Add((i, j));
            }
        int[][] ans = new int[m][];
        for (int i = 0; i < m; i++) ans[i] = new int[n];
        int[] rowMax = new int[m], colMax = new int[n];
        foreach (var kv in cells) {
            var group = kv.Value;
            var parent = new Dictionary<string, string>();
            Func<string, string> find = null;
            find = x => {
                while (parent[x] != x) { parent[x] = parent[parent[x]]; x = parent[x]; }
                return x;
            };
            foreach (var (i, j) in group) {
                parent["r" + i] = "r" + i;
                parent["c" + j] = "c" + j;
            }
            foreach (var (i, j) in group) {
                string ri = find("r" + i), ci = find("c" + j);
                if (ri != ci) parent[ri] = ci;
            }
            var comps = new Dictionary<string, List<(int, int)>>();
            foreach (var (i, j) in group) {
                string r = find("r" + i);
                if (!comps.ContainsKey(r)) comps[r] = new List<(int, int)>();
                comps[r].Add((i, j));
            }
            foreach (var comp in comps.Values) {
                int rank = 1;
                foreach (var (i, j) in comp) rank = Math.Max(rank, Math.Max(rowMax[i] + 1, colMax[j] + 1));
                foreach (var (i, j) in comp) {
                    ans[i][j] = rank;
                    rowMax[i] = rank;
                    colMax[j] = rank;
                }
            }
        }
        return ans;
    }
}
