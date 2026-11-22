// LeetCode 1766. Tree of Coprimes — Hard
// https://leetcode.com/problems/tree-of-coprimes/
// Submission 2201152648 — Accepted, Java
//
// My thinking: walking down from the root, I keep
// for every value the deepest node on the path that
// carries it — a node's answer is the deepest such
// node whose value is coprime with its own, and I
// restore the old entry when I walk back up.

import java.util.*;

class Solution {
    public int[] getCoprimes(int[] nums, int[][] edges) {
        int n = nums.length;
        List<Integer>[] adj = new ArrayList[n];
        for (int i = 0; i < n; i++) adj[i] = new ArrayList<>();
        for (int[] e : edges) {
            adj[e[0]].add(e[1]);
            adj[e[1]].add(e[0]);
        }
        List<Integer>[] coprime = new ArrayList[51];
        for (int i = 1; i <= 50; i++) coprime[i] = new ArrayList<>();
        for (int a = 1; a <= 50; a++) {
            for (int b = 1; b <= 50; b++) {
                if (gcd(a, b) == 1) coprime[a].add(b);
            }
        }
        int[] ans = new int[n];
        Arrays.fill(ans, -1);
        int[][] deepest = new int[51][2];
        for (int i = 1; i <= 50; i++) {
            deepest[i][0] = -1;
            deepest[i][1] = -1;
        }
        Deque<int[]> stack = new ArrayDeque<>();
        stack.push(new int[]{0, -1, 0, 1, -1, -1});
        while (!stack.isEmpty()) {
            int[] cur = stack.pop();
            int u = cur[0], parent = cur[1], depth = cur[2];
            if (cur[3] == 1) {
                int bestDepth = -1, bestNode = -1;
                for (int v : coprime[nums[u]]) {
                    if (deepest[v][0] > bestDepth) {
                        bestDepth = deepest[v][0];
                        bestNode = deepest[v][1];
                    }
                }
                ans[u] = bestNode;
                int pd = deepest[nums[u]][0], pn = deepest[nums[u]][1];
                deepest[nums[u]][0] = depth;
                deepest[nums[u]][1] = u;
                stack.push(new int[]{u, parent, depth, 0, pd, pn});
                for (int w : adj[u]) {
                    if (w != parent) stack.push(new int[]{w, u, depth + 1, 1, -1, -1});
                }
            } else {
                deepest[nums[u]][0] = cur[4];
                deepest[nums[u]][1] = cur[5];
            }
        }
        return ans;
    }

    private int gcd(int a, int b) {
        return b == 0 ? a : gcd(a, b % a);
    }
}
