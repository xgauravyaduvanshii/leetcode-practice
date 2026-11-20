function maxSizeSlices(slices: number[]): number {
    // My thinking: a circle breaks two ways — skip the
    // first slice or skip the last — and each straight
    // line is a take-it-or-leave-it table over how many
    // slices are taken.
    const n = Math.floor(slices.length / 3);
    function best(arr: number[]): number {
        const m = arr.length;
        const dp: number[][] = Array.from({ length: m + 1 }, () => new Array(n + 1).fill(0));
        for (let i = 1; i <= m; i++) {
            for (let j = 1; j <= n; j++) {
                dp[i][j] = dp[i - 1][j];
                if (i >= 2) {
                    dp[i][j] = Math.max(dp[i][j], dp[i - 2][j - 1] + arr[i - 1]);
                } else if (j === 1) {
                    dp[i][j] = Math.max(dp[i][j], arr[i - 1]);
                }
            }
        }
        return dp[m][n];
    }
    return Math.max(best(slices.slice(1)), best(slices.slice(0, -1)));
}
