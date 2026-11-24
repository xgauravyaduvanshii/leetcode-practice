// LeetCode 3515. Shortest Path in a Weighted Tree — Hard
// https://leetcode.com/problems/shortest-path-in-a-weighted-tree/
// Submission 2202789731 — Accepted, Java
import java.util.*;

class Solution {
    public int[] treeQueries(int n, int[][] edges, int[][] queries) {
        // My thinking: in a tree the distance from the root to any node
        // is just the sum of the edge weights on the root-to-node path.
        // Updating one edge only changes the distance of the nodes in
        // that edge's subtree (the deeper endpoint's side), so I turn
        // each edge update into a range add over the subtree (Euler
        // tour times give every subtree a contiguous interval) and
        // answer a query by adding the accumulated delta to the
        // node's initial root distance. A Fenwick tree does the range
        // add / point query in O(log n).
        List<int[]>[] adj = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++) adj[i] = new ArrayList<>();
        for (int[] e : edges) {
            adj[e[0]].add(new int[]{e[1], e[2]});
            adj[e[1]].add(new int[]{e[0], e[2]});
        }
        int[] tin = new int[n + 1];
        int[] tout = new int[n + 1];
        int[] parent = new int[n + 1];
        int[] dist0 = new int[n + 1];
        int timer = 0;
        Deque<int[]> stack = new ArrayDeque<>();
        stack.push(new int[]{1, 0, 0});
        while (!stack.isEmpty()) {
            int[] cur = stack.pop();
            int node = cur[0], par = cur[1], state = cur[2];
            if (state == 0) {
                tin[node] = ++timer;
                parent[node] = par;
                stack.push(new int[]{node, par, 1});
                for (int[] nb : adj[node]) {
                    if (nb[0] == par) continue;
                    dist0[nb[0]] = dist0[node] + nb[1];
                    stack.push(new int[]{nb[0], node, 0});
                }
            } else {
                tout[node] = timer;
            }
        }
        int size = n + 2;
        int[] bit = new int[size + 2];
        Map<Integer, Integer> curW = new HashMap<>();
        for (int[] e : edges) {
            int child = parent[e[1]] == e[0] ? e[1] : e[0];
            curW.put(child, e[2]);
        }
        List<Integer> ans = new ArrayList<>();
        for (int[] q : queries) {
            if (q[0] == 1) {
                int u = q[1], v = q[2], w = q[3];
                int child = parent[v] == u ? v : u;
                int delta = w - curW.get(child);
                curW.put(child, w);
                bitAdd(bit, size, tin[child], delta);
                bitAdd(bit, size, tout[child] + 1, -delta);
            } else {
                int x = q[1];
                ans.add(dist0[x] + bitSum(bit, tin[x]));
            }
        }
        return ans.stream().mapToInt(Integer::intValue).toArray();
    }

    private void bitAdd(int[] bit, int size, int i, int delta) {
        while (i <= size) {
            bit[i] += delta;
            i += i & -i;
        }
    }

    private int bitSum(int[] bit, int i) {
        int s = 0;
        while (i > 0) {
            s += bit[i];
            i -= i & -i;
        }
        return s;
    }
}
