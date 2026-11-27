// LeetCode 3772. Maximum Subgraph Score in a Tree — Hard
// https://leetcode.com/problems/maximum-subgraph-score-in-a-tree/
// Submission 2203171837 — Accepted, Java
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] maxSubgraphScore(int n, int[][] edges, int[] good) {
        // My thinking: give each node the value +1 if good and
        // -1 if bad, so a subgraph's score is the sum of its
        // nodes' values. Root the tree anywhere and first work
        // bottom-up: down[u] is the best connected subgraph
        // containing u and staying inside u's subtree, which
        // takes u plus every child subtree whose down value is
        // positive. Then work top-down (rerooting): for a child
        // v of u, the best piece of the rest of the tree that
        // can hang off u is u's value plus the positive child
        // contributions except v's, plus u's own parent-side
        // piece when positive. The answer for u is its value
        // plus every positive contribution from all sides.
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] e : edges) {
            adj.get(e[0]).add(e[1]);
            adj.get(e[1]).add(e[0]);
        }
        int[] val = new int[n];
        for (int i = 0; i < n; i++) val[i] = good[i] == 1 ? 1 : -1;

        int[] parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = -1;
        parent[0] = -2;
        int[] order = new int[n];
        int m = 0;
        ArrayDeque<Integer> stack = new ArrayDeque<>();
        stack.push(0);
        while (!stack.isEmpty()) {
            int u = stack.pop();
            order[m++] = u;
            for (int w : adj.get(u)) {
                if (parent[w] == -1) {
                    parent[w] = u;
                    stack.push(w);
                }
            }
        }

        int[] down = val.clone();
        for (int i = n - 1; i >= 0; i--) {
            int u = order[i];
            for (int w : adj.get(u)) {
                if (parent[w] == u && down[w] > 0) down[u] += down[w];
            }
        }

        // up[u] is the value of the best connected piece that
        // contains u's parent but no node of u's subtree; it
        // is only ever added when positive, so it may be
        // negative here and that is fine.
        int[] up = new int[n];
        int[] ans = new int[n];
        for (int i = 0; i < n; i++) {
            int u = order[i];
            int total = val[u];
            if (up[u] > 0) total += up[u];
            List<Integer> children = new ArrayList<>();
            for (int w : adj.get(u)) {
                if (parent[w] == u) children.add(w);
            }
            int[] pos = new int[children.size()];
            int sumPos = 0;
            for (int j = 0; j < children.size(); j++) {
                pos[j] = Math.max(0, down[children.get(j)]);
                sumPos += pos[j];
            }
            total += sumPos;
            ans[u] = total;
            int rest = val[u] + Math.max(0, up[u]);
            for (int j = 0; j < children.size(); j++) {
                up[children.get(j)] = rest + (sumPos - pos[j]);
            }
        }
        return ans;
    }
}
