// LeetCode 2280. Minimum Lines to Represent a Line Chart — Medium
// https://leetcode.com/problems/minimum-lines-to-represent-a-line-chart/
// Submission 2204634389 — Accepted, C#
//
// My thinking: same idea as the Python version — sort by day, then count
// slope changes by cross-multiplication. The coordinates are kept in
// longs so the products cannot overflow.
public class Solution {
    public int MinimumLines(int[][] stockPrices) {
        Array.Sort(stockPrices, (a, b) => a[0].CompareTo(b[0]));
        int n = stockPrices.Length;
        if (n <= 1) return 0;
        int ans = 1;
        for (int i = 2; i < n; i++) {
            long x1 = stockPrices[i - 2][0], y1 = stockPrices[i - 2][1];
            long x2 = stockPrices[i - 1][0], y2 = stockPrices[i - 1][1];
            long x3 = stockPrices[i][0], y3 = stockPrices[i][1];
            if ((y2 - y1) * (x3 - x2) != (y3 - y2) * (x2 - x1)) ans++;
        }
        return ans;
    }
}
