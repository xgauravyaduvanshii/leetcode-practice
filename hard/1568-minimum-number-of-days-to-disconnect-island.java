class Solution {
    public int minDays(int[][] grid) {
        // My thinking: an island already in pieces needs no
        // days; otherwise look for one cell whose removal
        // breaks it — if none exists, two days always do it.
        int m = grid.length, n = grid[0].length;
        if (countIslands(grid) != 1) return 0;
        int land = 0;
        for (int[] row : grid) for (int v : row) land += v;
        if (land <= 2) return land;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    grid[i][j] = 0;
                    if (countIslands(grid) != 1) return 1;
                    grid[i][j] = 1;
                }
            }
        }
        return 2;
    }

    private int countIslands(int[][] g) {
        int m = g.length, n = g[0].length;
        boolean[][] seen = new boolean[m][n];
        int count = 0;
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (g[i][j] == 1 && !seen[i][j]) {
                    count++;
                    java.util.ArrayDeque<int[]> stack = new java.util.ArrayDeque<>();
                    stack.push(new int[]{i, j});
                    seen[i][j] = true;
                    while (!stack.isEmpty()) {
                        int[] cell = stack.pop();
                        for (int[] d : dirs) {
                            int nx = cell[0] + d[0], ny = cell[1] + d[1];
                            if (nx >= 0 && nx < m && ny >= 0 && ny < n && g[nx][ny] == 1 && !seen[nx][ny]) {
                                seen[nx][ny] = true;
                                stack.push(new int[]{nx, ny});
                            }
                        }
                    }
                }
            }
        }
        return count;
    }
}
