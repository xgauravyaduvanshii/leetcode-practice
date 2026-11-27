// LeetCode 2285. Maximum Total Importance of Roads — Medium
// https://leetcode.com/problems/maximum-total-importance-of-roads/
// Submission 2204641923 — Accepted, Java
//
// My thinking: same idea as the Python version — count degrees, sort
// them, and assign the values 1..n in ascending order so the busiest
// cities get the biggest values. Longs are used because the total can
// exceed 32 bits.
class Solution {
    public long maximumImportance(int n, int[][] roads) {
        long[] deg = new long[n];
        for (int[] r : roads) {
            deg[r[0]]++;
            deg[r[1]]++;
        }
        Arrays.sort(deg);
        long ans = 0;
        for (int i = 0; i < n; i++) {
            ans += deg[i] * (i + 1);
        }
        return ans;
    }
}
