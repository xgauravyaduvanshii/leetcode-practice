class Solution {
    private int MOD = 1000000007;
    private int[][] apples;
    private int[][][] memo;
    private int rows, cols;

    public int ways(String[] pizza, int k) {
        // My thinking: from each corner, every cut either
        // peels off a strip with an apple in it or keeps the
        // rest for the remaining cuts — a table of apple
        // counts tells which cuts are legal.
        rows = pizza.length;
        cols = pizza[0].length();
        apples = new int[rows + 1][cols + 1];
        for (int r = rows - 1; r >= 0; r--) {
            for (int c = cols - 1; c >= 0; c--) {
                apples[r][c] = (pizza[r].charAt(c) == 'A' ? 1 : 0) + apples[r + 1][c] + apples[r][c + 1] - apples[r + 1][c + 1];
            }
        }
        memo = new int[k + 1][rows][cols];
        for (int p = 0; p <= k; p++) {
            for (int r = 0; r < rows; r++) {
                java.util.Arrays.fill(memo[p][r], -1);
            }
        }
        return dp(k, 0, 0);
    }

    private int dp(int pieces, int r, int c) {
        if (apples[r][c] == 0) return 0;
        if (pieces == 1) return 1;
        if (memo[pieces][r][c] != -1) return memo[pieces][r][c];
        int total = 0;
        for (int nr = r + 1; nr < rows; nr++) {
            if (apples[r][c] - apples[nr][c] > 0) {
                total = (total + dp(pieces - 1, nr, c)) % MOD;
            }
        }
        for (int nc = c + 1; nc < cols; nc++) {
            if (apples[r][c] - apples[r][nc] > 0) {
                total = (total + dp(pieces - 1, r, nc)) % MOD;
            }
        }
        memo[pieces][r][c] = total;
        return total;
    }
}
