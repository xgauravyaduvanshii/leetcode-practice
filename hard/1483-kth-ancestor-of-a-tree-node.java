class TreeAncestor {
    private int[][] up;

    public TreeAncestor(int n, int[] parent) {
        // My thinking: jump up the tree in powers of two —
        // precompute the 1st, 2nd, 4th, 8th... ancestor of
        // every node, then walk k's binary digits upward.
        int LOG = 1;
        while ((1 << LOG) <= n) LOG++;
        up = new int[LOG][n];
        for (int i = 0; i < n; i++) up[0][i] = parent[i];
        for (int j = 1; j < LOG; j++) {
            for (int i = 0; i < n; i++) {
                int mid = up[j - 1][i];
                up[j][i] = mid == -1 ? -1 : up[j - 1][mid];
            }
        }
    }

    public int getKthAncestor(int node, int k) {
        for (int j = 0; j < up.length && node != -1; j++) {
            if ((k & (1 << j)) != 0) node = up[j][node];
        }
        return node;
    }
}
