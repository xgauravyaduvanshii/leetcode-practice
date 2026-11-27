// LeetCode 3486. Longest Special Path II — Hard
// https://leetcode.com/problems/longest-special-path-ii/
// Submission 2202703842 — Accepted, C#
public class Solution {
    public int[] LongestSpecialPath(int[][] edges, int[] nums) {
        // My thinking: a special path is a downward path, so it is
        // a suffix of the root-to-current path. For the current
        // node I want the leftmost start that keeps the window
        // valid: no value three times, and at most one value twice.
        // For each value I keep its occurrence depths on the path.
        // Let b be the deepest third-from-last occurrence over all
        // values (the start must sit past it, or some value would
        // appear three times), and let a2 be the second largest
        // second-from-last occurrence (the start must sit past all
        // but the largest one, or two values would appear twice).
        // The window starts at max(b, a2) + 1. Both numbers only
        // ever grow while I walk down, so I save and restore them
        // (and the top-two second-from-last list) on the DFS stack
        // instead of maintaining a heap. The DFS is iterative
        // because the tree can be 50000 deep.
        int n = nums.Length;
        var adj = new List<(int to, int w)>[n];
        for (int i = 0; i < n; i++) adj[i] = new List<(int, int)>();
        foreach (var e in edges) {
            adj[e[0]].Add((e[1], e[2]));
            adj[e[1]].Add((e[0], e[2]));
        }
        var occ = new Dictionary<int, List<int>>();
        int bestB = -1;
        var top = new List<(int a, int v)>();
        long bestLen = 0;
        int bestNodes = 0;
        var path = new List<int>();
        var pathDist = new List<long>();
        // (node, parent, dist, isExit, savedBestB, savedTop)
        var stack = new Stack<(int node, int parent, long dist, bool isExit, int savedBestB, List<(int a, int v)> savedTop)>();
        stack.Push((0, -1, 0, false, -1, null));
        while (stack.Count > 0) {
            var (node, parent, d, isExit, savedBestB, savedTop) = stack.Pop();
            if (!isExit) {
                int v = nums[node];
                int savedB = bestB;
                var savedT = new List<(int a, int vv)>(top);
                int depth = path.Count;
                if (!occ.TryGetValue(v, out var lst)) { lst = new List<int>(); occ[v] = lst; }
                lst.Add(depth);
                if (lst.Count >= 3 && lst[lst.Count - 3] > bestB) bestB = lst[lst.Count - 3];
                if (lst.Count >= 2) {
                    int na = lst[lst.Count - 2];
                    top.RemoveAll(t => t.v == v);
                    top.Add((na, v));
                    top.Sort((x, y) => y.a.CompareTo(x.a));
                    if (top.Count > 2) top.RemoveRange(2, top.Count - 2);
                }
                path.Add(node);
                pathDist.Add(d);
                int l2 = top.Count >= 2 ? top[1].a : -1;
                int l = Math.Max(bestB, l2) + 1;
                long length = d - pathDist[l];
                int nodesCnt = depth - l + 1;
                if (length > bestLen || (length == bestLen && nodesCnt < bestNodes)) {
                    bestLen = length;
                    bestNodes = nodesCnt;
                }
                stack.Push((node, parent, d, true, savedB, savedT));
                foreach (var (nb, w) in adj[node]) {
                    if (nb == parent) continue;
                    stack.Push((nb, node, d + w, false, -1, null));
                }
            } else {
                bestB = savedBestB;
                top = savedTop;
                int v = nums[node];
                occ[v].RemoveAt(occ[v].Count - 1);
                path.RemoveAt(path.Count - 1);
                pathDist.RemoveAt(pathDist.Count - 1);
            }
        }
        return new int[] { (int)bestLen, bestNodes };
    }
}
