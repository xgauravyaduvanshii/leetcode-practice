function minCost(n: number, cuts: number[]): number {
    // My thinking: the first cut splits the stick in two
    // and costs the whole length — so try every cut first
    // and add the best bills of the two pieces.
    const pts = [0, ...cuts, n].sort((a, b) => a - b);
    const memo = new Map<string, number>();
    function dp(i: number, j: number): number {
        if (j - i <= 1) return 0;
        const key = `${i}|${j}`;
        const hit = memo.get(key);
        if (hit !== undefined) return hit;
        let best = Infinity;
        for (let k = i + 1; k < j; k++) {
            best = Math.min(best, dp(i, k) + dp(k, j));
        }
        const res = pts[j] - pts[i] + best;
        memo.set(key, res);
        return res;
    }
    return dp(0, pts.length - 1);
}
