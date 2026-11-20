class Solution {
    public int minTaps(int n, int[] ranges) {
        // My thinking: each tap waters one stretch of the garden,
        // so turn them into intervals and take the fewest that
        // cover the whole garden, always reaching as far as
        // possible from where we already stand.
        int[] furthest = new int[n + 1];
        for (int i = 0; i <= n; i++) {
            int left = Math.max(0, i - ranges[i]);
            int right = Math.min(n, i + ranges[i]);
            furthest[left] = Math.max(furthest[left], right);
        }
        int taps = 0, currentEnd = 0, nextEnd = 0;
        for (int i = 0; i < n; i++) {
            nextEnd = Math.max(nextEnd, furthest[i]);
            if (i == currentEnd) {
                if (nextEnd == currentEnd) return -1;
                taps++;
                currentEnd = nextEnd;
                if (currentEnd >= n) return taps;
            }
        }
        return -1;
    }
}
