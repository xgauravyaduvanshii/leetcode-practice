class Solution {
    public String kthSmallestPath(int[] destination, int k) {
        // My thinking: 'H' comes before 'V', so at each step
        // count how many paths start with 'H' — if k fits
        // inside, take it, otherwise take 'V' and skip past.
        // destination is (row, column): 'V' moves down a row,
        // 'H' moves right a column.
        int v = destination[0], h = destination[1];
        StringBuilder res = new StringBuilder();
        while (h > 0 || v > 0) {
            if (h == 0) { res.append('V'); v--; }
            else if (v == 0) { res.append('H'); h--; }
            else {
                long cnt = comb(h + v - 1, h - 1);
                if (k <= cnt) { res.append('H'); h--; }
                else { res.append('V'); k -= cnt; v--; }
            }
        }
        return res.toString();
    }

    private long comb(int n, int r) {
        // small numbers only — n <= 30 here
        long res = 1;
        r = Math.min(r, n - r);
        for (int i = 0; i < r; i++) res = res * (n - i) / (i + 1);
        return res;
    }
}
