// LeetCode 48. Rotate Image — Medium
// https://leetcode.com/problems/rotate-image/
// Submission 2203829127 — Accepted, Java

// My thinking: rotating the square 90 degrees clockwise is the same as
// flipping it over its main diagonal and then reversing each row. Both
// steps work in place, so I only swap elements and never allocate a
// second matrix.
class Solution {
    public void rotate(int[][] matrix) {
        int n = matrix.length;
        for (int r = 0; r < n; r++) {
            for (int c = r + 1; c < n; c++) {
                int tmp = matrix[r][c];
                matrix[r][c] = matrix[c][r];
                matrix[c][r] = tmp;
            }
        }
        for (int[] row : matrix) {
            int left = 0, right = n - 1;
            while (left < right) {
                int tmp = row[left];
                row[left] = row[right];
                row[right] = tmp;
                left++;
                right--;
            }
        }
    }
}
