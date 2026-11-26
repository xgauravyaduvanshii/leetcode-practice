// LeetCode 3841. Palindromic Path Queries in a Tree — Hard
// https://leetcode.com/problems/palindromic-path-queries-in-a-tree/
// Submission 2203286541 — Accepted, Java
import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Boolean> palindromePath(int n, int[][] edges, String s, String[] queries) {
        // My thinking: a string can be rearranged into a
        // palindrome exactly when at most one character occurs
        // an odd number of times, so a path is captured by the
        // 26-bit mask of which letters appear oddly often on
        // it. Root the tree and keep pref[x], the xor of the
        // letter bits from the root down to x: the mask of the
        // u-v path is pref[u] ^ pref[v] ^ bit(s[lca]), since
        // the lowest common ancestor is counted twice by the
        // two root masks and must be counted once. An update
        // at node u flips the bit of every root path through
        // u, which is exactly the subtree of u in Euler tour
        // order, so a Fenwick tree does range-xor-update and
        // point-query in log n, and binary lifting gives the
        // lowest common ancestor in log n.
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] e : edges) {
            adj.get(e[0]).add(e[1]);
            adj.get(e[1]).add(e[0]);
        }
        int LOG = 16;
        int[][] up = new int[LOG][n];
        int[] depth = new int[n];
        int[] tin = new int[n];
        int[] tout = new int[n];
        int[] parent = new int[n];
        parent[0] = 0;
        up[0][0] = 0;
        int timer = 0;
        int[] stack = new int[n];
        int[] nextChild = new int[n];
        int sp = 0;
        stack[sp++] = 0;
        tin[0] = timer++;
        while (sp > 0) {
            int u = stack[sp - 1];
            if (nextChild[u] < adj.get(u).size()) {
                int v = adj.get(u).get(nextChild[u]++);
                if (v == parent[u]) continue;
                parent[v] = u;
                depth[v] = depth[u] + 1;
                up[0][v] = u;
                tin[v] = timer++;
                stack[sp++] = v;
            } else {
                tout[u] = timer - 1;
                sp--;
            }
        }
        for (int j = 1; j < LOG; j++) {
            for (int v = 0; v < n; v++) {
                up[j][v] = up[j - 1][up[j - 1][v]];
            }
        }
        int[] bit = new int[n + 2];
        int[] cur = new int[n];
        for (int i = 0; i < n; i++) cur[i] = 1 << (s.charAt(i) - 'a');
        for (int v = 0; v < n; v++) {
            bitAdd(bit, n, tin[v], cur[v]);
            bitAdd(bit, n, tout[v] + 1, cur[v]);
        }
        List<Boolean> ans = new ArrayList<>();
        for (String q : queries) {
            String[] p = q.split(" ");
            if (p[0].equals("update")) {
                int u = Integer.parseInt(p[1]);
                int nw = 1 << (p[2].charAt(0) - 'a');
                if (cur[u] != nw) {
                    int d = cur[u] ^ nw;
                    cur[u] = nw;
                    bitAdd(bit, n, tin[u], d);
                    bitAdd(bit, n, tout[u] + 1, d);
                }
            } else {
                int u = Integer.parseInt(p[1]);
                int v = Integer.parseInt(p[2]);
                int w = lca(u, v, depth, up, LOG);
                int mask = bitSum(bit, tin[u]) ^ bitSum(bit, tin[v]) ^ cur[w];
                ans.add((mask & (mask - 1)) == 0);
            }
        }
        return ans;
    }

    private void bitAdd(int[] bit, int n, int idx, int val) {
        for (int i = idx + 1; i <= n; i += i & -i) {
            bit[i] ^= val;
        }
    }

    private int bitSum(int[] bit, int idx) {
        int res = 0;
        for (int i = idx + 1; i > 0; i -= i & -i) {
            res ^= bit[i];
        }
        return res;
    }

    private int lca(int a, int b, int[] depth, int[][] up, int LOG) {
        if (depth[a] < depth[b]) {
            int t = a;
            a = b;
            b = t;
        }
        int d = depth[a] - depth[b];
        for (int j = 0; j < LOG; j++) {
            if ((d & (1 << j)) != 0) a = up[j][a];
        }
        if (a == b) return a;
        for (int j = LOG - 1; j >= 0; j--) {
            if (up[j][a] != up[j][b]) {
                a = up[j][a];
                b = up[j][b];
            }
        }
        return up[0][a];
    }
}
