// LeetCode 4077. Minimize Inversions in a Prefix Tree — Hard
// https://leetcode.com/problems/minimize-inversions-in-a-prefix-tree/
// Submission 2203692675 — Accepted, C#
public class Solution {
    public int MinInversions(string[] words, int[] target) {
        // My thinking: build the prefix tree (trie) of all words.
        // The pre-order traversal is fixed except for the order of
        // each node's children, and each node can be ordered
        // independently — except a word that is a prefix of other
        // words is always visited before its whole subtree. Walking
        // the words in target order, each word's ancestors already
        // processed count as inversions against the still-unseen
        // words in earlier sibling subtrees, which gives a pairwise
        // cost between sibling children; a marked ancestor adds a
        // fixed inversion whenever a later word in target order
        // passes through it. Each node's children are then ordered
        // to minimise their pairwise cost — by direct comparison
        // for two children, or by a subset DP over child orderings
        // (at most 10 children, letters 'a' to 'j') otherwise.
        // Summing the fixed part and every node's best ordering
        // gives the minimum total inversions.
        int n = words.Length;
        var children = new List<Dictionary<char, int>>();
        var mark = new List<int>();
        children.Add(new Dictionary<char, int>());
        mark.Add(-1);
        var paths = new List<List<int>>();
        for (int idx = 0; idx < n; idx++) {
            int node = 0;
            var path = new List<int> { 0 };
            foreach (char ch in words[idx]) {
                if (!children[node].TryGetValue(ch, out int nxt)) {
                    nxt = children.Count;
                    children[node][ch] = nxt;
                    children.Add(new Dictionary<char, int>());
                    mark.Add(-1);
                }
                node = nxt;
                path.Add(node);
            }
            mark[node] = idx;
            paths.Add(path);
        }
        int m = children.Count;
        var childPos = new List<Dictionary<int, int>>();
        var counts = new List<int[]>();
        var costs = new List<long[][]>();
        for (int u = 0; u < m; u++) {
            var lst = new List<int>(children[u].Values);
            var pos = new Dictionary<int, int>();
            for (int i = 0; i < lst.Count; i++) pos[lst[i]] = i;
            childPos.Add(pos);
            int k = lst.Count;
            counts.Add(new int[k]);
            var cm = new long[k][];
            for (int i = 0; i < k; i++) cm[i] = new long[k];
            costs.Add(cm);
        }
        var processed = new bool[n];
        long fixedCost = 0;
        foreach (int idx in target) {
            var path = paths[idx];
            for (int j = 0; j < path.Count - 1; j++) {
                int u = path[j];
                int v = path[j + 1];
                int p = childPos[u][v];
                int[] cnt = counts[u];
                long[] row = costs[u][p];
                for (int q = 0; q < cnt.Length; q++) if (q != p) row[q] += cnt[q];
                int mu = mark[u];
                if (mu != -1 && !processed[mu]) fixedCost++;
            }
            for (int j = 0; j < path.Count - 1; j++) {
                int u = path[j];
                int v = path[j + 1];
                counts[u][childPos[u][v]]++;
            }
            processed[idx] = true;
        }
        long total = fixedCost;
        for (int u = 0; u < m; u++) {
            int k = childPos[u].Count;
            if (k <= 1) continue;
            long[][] cmat = costs[u];
            if (k == 2) { total += Math.Min(cmat[0][1], cmat[1][0]); continue; }
            int size = 1 << k;
            var add = new long[k][];
            for (int b = 0; b < k; b++) {
                add[b] = new long[size];
                for (int mask = 1; mask < size; mask++) {
                    int lsb = mask & -mask;
                    int bit = 0;
                    while ((1 << bit) != lsb) bit++;
                    add[b][mask] = add[b][mask ^ lsb] + cmat[bit][b];
                }
            }
            long INF = long.MaxValue / 4;
            var dp = new long[size];
            for (int i = 0; i < size; i++) dp[i] = INF;
            dp[0] = 0;
            for (int mask = 0; mask < size; mask++) {
                long cur = dp[mask];
                if (cur == INF) continue;
                for (int b = 0; b < k; b++) if ((mask & (1 << b)) == 0) {
                    int nm = mask | (1 << b);
                    long val = cur + add[b][mask];
                    if (val < dp[nm]) dp[nm] = val;
                }
            }
            total += dp[size - 1];
        }
        return (int)total;
    }
}
