// LeetCode 2050. Parallel Courses III — Hard
// https://leetcode.com/problems/parallel-courses-iii/
// Submission 2201562479 — Accepted, C#
//
// My thinking: a course can only start once its
// slowest prerequisite is done, so I walk the
// courses in prerequisite order and each one
// finishes at its own time plus the slowest
// prerequisite — the last finish is the answer.

public class Solution {
    public int MinimumTime(int n, int[][] relations, int[] time) {
        var graph = new List<int>[n + 1];
        for (int i = 1; i <= n; i++) graph[i] = new List<int>();
        var indeg = new int[n + 1];
        foreach (var rel in relations) {
            graph[rel[0]].Add(rel[1]);
            indeg[rel[1]]++;
        }
        var finish = new int[n + 1];
        var q = new Queue<int>();
        for (int i = 1; i <= n; i++) {
            if (indeg[i] == 0) {
                q.Enqueue(i);
                finish[i] = time[i - 1];
            }
        }
        while (q.Count > 0) {
            int u = q.Dequeue();
            foreach (int v in graph[u]) {
                finish[v] = Math.Max(finish[v], finish[u] + time[v - 1]);
                if (--indeg[v] == 0) q.Enqueue(v);
            }
        }
        return finish.Max();
    }
}
