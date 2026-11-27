// LeetCode 3027. Find the Number of Ways to Place People II — Hard
// https://leetcode.com/problems/find-the-number-of-ways-to-place-people-ii/
// Submission 2201902350 — Accepted, Java
//
// My thinking: I sort the points by x
// rising, and for equal x by y falling,
// so Alice comes before every possible
// Bob to her right. For one Alice, I
// walk rightwards keeping the highest y
// seen so far below her: a Bob counts
// exactly when his y is a new high,
// because any lower Bob would have that
// higher point sitting inside his fence.

import java.util.Arrays;

class Solution {
    public int numberOfPairs(int[][] points) {
        Arrays.sort(points, (a, b) -> a[0] != b[0]
                ? Integer.compare(a[0], b[0])
                : Integer.compare(b[1], a[1]));
        int n = points.length;
        int ans = 0;
        for (int i = 0; i < n; i++) {
            int yi = points[i][1];
            int highest = Integer.MIN_VALUE;
            for (int j = i + 1; j < n; j++) {
                int yj = points[j][1];
                if (yj > yi) {
                    continue;
                }
                if (yj > highest) {
                    ans++;
                    highest = yj;
                }
            }
        }
        return ans;
    }
}
