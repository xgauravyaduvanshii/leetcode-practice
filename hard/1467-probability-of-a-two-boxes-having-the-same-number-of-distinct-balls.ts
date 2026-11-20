function getProbability(balls: number[]): number {
    // My thinking: go colour by colour, splitting each
    // colour's balls between the two boxes — count how
    // many splits end even with the same number of
    // distinct colours on both sides.
    const total = balls.reduce((a, b) => a + b, 0);
    const half = Math.floor(total / 2);
    const k = balls.length;
    function comb(n: number, r: number): number {
        if (r < 0 || r > n) return 0;
        let res = 1;
        for (let i = 0; i < r; i++) res = res * (n - i) / (i + 1);
        return res;
    }
    const memo = new Map<string, number>();
    function dp(i: number, inBox1: number, distinct1: number, distinct2: number): number {
        if (i === k) return (inBox1 === half && distinct1 === distinct2) ? 1 : 0;
        const key = `${i}|${inBox1}|${distinct1}|${distinct2}`;
        const hit = memo.get(key);
        if (hit !== undefined) return hit;
        let ways = 0;
        const c = balls[i];
        for (let x = 0; x <= c; x++) {
            ways += comb(c, x) * dp(i + 1, inBox1 + x, distinct1 + (x > 0 ? 1 : 0), distinct2 + (x < c ? 1 : 0));
        }
        memo.set(key, ways);
        return ways;
    }
    return dp(0, 0, 0, 0) / comb(total, half);
}
