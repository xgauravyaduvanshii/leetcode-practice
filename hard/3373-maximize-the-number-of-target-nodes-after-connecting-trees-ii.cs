// LeetCode 3373. Maximize the Number of Target Nodes After Connecting Trees II — Hard
// https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii/
// Submission 2202430805 -- Accepted, C#
public class Solution {
    public int[] MaxTargetNodes(int[][] edges1, int[][] edges2) {
        // My thinking: in a tree, two nodes are at even distance exactly
        // when they share a side of the bipartition, so I 2-colour both
        // trees. Connecting i to any node j of tree 2 adds the tree-2 nodes
        // of the opposite colour to j, which is most when j has the minority
        // colour — so tree 2 always contributes max(cnt2[0], cnt2[1]).
        // Tree 1 contributes the nodes sharing i's colour.
        int n = edges1.Length + 1;
        int m = edges2.Length + 1;
        var (colour1, cnt1) = ColourCounts(n, edges1);
        var (_, cnt2) = ColourCounts(m, edges2);
        int best2 = System.Math.Max(cnt2[0], cnt2[1]);
        int[] ans = new int[n];
        for (int i = 0; i < n; i++) {
            ans[i] = cnt1[colour1[i]] + best2;
        }
        return ans;
    }

    private (int[], int[]) ColourCounts(int n, int[][] edges) {
        var adj = new System.Collections.Generic.List<int>[n];
        for (int i = 0; i < n; i++) {
            adj[i] = new System.Collections.Generic.List<int>();
        }
        foreach (var e in edges) {
            adj[e[0]].Add(e[1]);
            adj[e[1]].Add(e[0]);
        }
        int[] colour = new int[n];
        for (int i = 0; i < n; i++) {
            colour[i] = -1;
        }
        colour[0] = 0;
        var stack = new System.Collections.Generic.Stack<int>();
        stack.Push(0);
        int[] cnt = new int[2];
        while (stack.Count > 0) {
            int u = stack.Pop();
            cnt[colour[u]]++;
            foreach (int v in adj[u]) {
                if (colour[v] == -1) {
                    colour[v] = colour[u] ^ 1;
                    stack.Push(v);
                }
            }
        }
        return (colour, cnt);
    }
}
