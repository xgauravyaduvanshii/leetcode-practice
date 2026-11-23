// LeetCode 2509. Cycle Length Queries in a Tree — Hard
// https://leetcode.com/problems/cycle-length-queries-in-a-tree/
// Submission 2201791018 — Accepted, Java
//
// My thinking: in this tree a node's
// parent is just half its number, so I
// lift the deeper of the two up until
// they meet at the same depth, then lift
// them together until they meet — the
// steps up plus the new edge between
// them is the cycle.

class Solution {
    public int[] cycleLengthQueries(int n, int[][] queries) {
        int[] ans = new int[queries.length];
        for (int q = 0; q < queries.length; q++) {
            int a = queries[q][0], b = queries[q][1];
            int da = depth(a), db = depth(b);
            int steps = 0;
            while (da > db) { a /= 2; da--; steps++; }
            while (db > da) { b /= 2; db--; steps++; }
            while (a != b) { a /= 2; b /= 2; steps += 2; }
            ans[q] = steps + 1;
        }
        return ans;
    }

    private int depth(int x) {
        int d = 0;
        while (x > 1) { x /= 2; d++; }
        return d;
    }
}
