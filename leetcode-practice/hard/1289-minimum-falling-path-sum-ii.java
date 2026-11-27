class Solution {
    public int minFallingPathSum(int[][] grid) {
        // My thinking: each row only needs the previous row's
        // smallest and second-smallest sums — the next cell
        // takes the smallest unless it sits in the same column.
        int n = grid.length;
        int[] prev = grid[0].clone();
        for (int r = 1; r < n; r++) {
            int first = Integer.MAX_VALUE, second = Integer.MAX_VALUE, firstIdx = -1;
            for (int i = 0; i < n; i++) {
                if (prev[i] < first) {
                    second = first;
                    first = prev[i];
                    firstIdx = i;
                } else if (prev[i] < second) {
                    second = prev[i];
                }
            }
            int[] cur = new int[n];
            for (int c = 0; c < n; c++) {
                cur[c] = grid[r][c] + (c == firstIdx ? second : first);
            }
            prev = cur;
        }
        int best = Integer.MAX_VALUE;
        for (int v : prev) best = Math.min(best, v);
        return best;
    }
}
