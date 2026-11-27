// LeetCode 1719. Number Of Ways To Reconstruct A Tree — Hard
// https://leetcode.com/problems/number-of-ways-to-reconstruct-a-tree/
// Submission 2201113812 — Accepted, C#
//
// My thinking: a subtree's root must touch every node
// in it, so I peel such a root off, split what is left
// into its connected parts, and repeat — if some part
// has no such root, no tree fits; if any part ever has
// two of them, the top of that part can flip, so there
// are two trees.

using System;
using System.Collections.Generic;

public class Solution {
    private Dictionary<int, HashSet<int>> adj;

    public int CheckWays(int[][] pairs) {
        adj = new Dictionary<int, HashSet<int>>();
        foreach (var p in pairs) {
            if (!adj.ContainsKey(p[0])) adj[p[0]] = new HashSet<int>();
            if (!adj.ContainsKey(p[1])) adj[p[1]] = new HashSet<int>();
            adj[p[0]].Add(p[1]);
            adj[p[1]].Add(p[0]);
        }
        var nodes = new HashSet<int>(adj.Keys);
        bool? result = Rec(nodes);
        if (result == null) return 0;
        return result.Value ? 2 : 1;
    }

    // True if this part is ambiguous, null if no tree fits it.
    private bool? Rec(HashSet<int> S) {
        if (S.Count == 1) return false;
        var cands = new List<int>();
        foreach (int x in S) {
            int inside = 0;
            foreach (int y in adj[x]) {
                if (S.Contains(y)) inside++;
            }
            if (inside == S.Count - 1) cands.Add(x);
        }
        if (cands.Count == 0) return null;
        bool ambiguous = cands.Count > 1;
        int r = cands[0];
        var rest = new HashSet<int>(S);
        rest.Remove(r);
        var seen = new HashSet<int>();
        foreach (int start in rest) {
            if (seen.Contains(start)) continue;
            var stack = new Stack<int>();
            var comp = new HashSet<int>();
            stack.Push(start);
            seen.Add(start);
            while (stack.Count > 0) {
                int u = stack.Pop();
                comp.Add(u);
                foreach (int v in adj[u]) {
                    if (rest.Contains(v) && !seen.Contains(v)) {
                        seen.Add(v);
                        stack.Push(v);
                    }
                }
            }
            bool? sub = Rec(comp);
            if (sub == null) return null;
            ambiguous = ambiguous || sub.Value;
        }
        return ambiguous;
    }
}
