// LeetCode 3562. Maximum Profit from Trading Stocks with Discounts — Hard
// https://leetcode.com/problems/maximum-profit-from-trading-stocks-with-discounts/
// Submission 2202847966 — Accepted, TypeScript
function maxProfit(n: number, present: number[], future: number[], hierarchy: number[][], budget: number): number {
    // My thinking: a tree knapsack. For each employee I keep two
    // tables over the budget: one for when their boss bought
    // (so their own price is halved) and one for when the boss
    // did not. Whether the employee buys or not, the children
    // only care about that choice — not about the boss — so both
    // tables share the same "employee does not buy" case (the
    // children see no discount) and differ only in the price the
    // employee pays when they do buy.
    const NEG = -1e9;
    const children: number[][] = Array.from({ length: n + 1 }, () => []);
    for (const [u, v] of hierarchy) children[u].push(v);

    function merge(a: number[], b: number[]): number[] {
        const res = new Array(budget + 1).fill(NEG);
        for (let x = 0; x <= budget; x++) {
            if (a[x] === NEG) continue;
            for (let y = 0; y + x <= budget; y++) {
                if (b[y] === NEG) continue;
                if (a[x] + b[y] > res[x + y]) res[x + y] = a[x] + b[y];
            }
        }
        let best = NEG;
        for (let i = 0; i <= budget; i++) { best = Math.max(best, res[i]); res[i] = best; }
        return res;
    }

    function solve(u: number): [number[], number[]] {
        let comb0 = new Array(budget + 1).fill(0);
        let comb1 = new Array(budget + 1).fill(0);
        for (const v of children[u]) {
            const [d0, d1] = solve(v);
            comb0 = merge(comb0, d0);
            comb1 = merge(comb1, d1);
        }
        const dp0 = comb0.slice();
        const dp1 = comb0.slice();
        const c0 = present[u - 1];
        if (c0 <= budget) {
            const profit = future[u - 1] - c0;
            for (let b = c0; b <= budget; b++) dp0[b] = Math.max(dp0[b], profit + comb1[b - c0]);
        }
        const c1 = Math.floor(present[u - 1] / 2);
        if (c1 <= budget) {
            const profit = future[u - 1] - c1;
            for (let b = c1; b <= budget; b++) dp1[b] = Math.max(dp1[b], profit + comb1[b - c1]);
        }
        return [dp0, dp1];
    }

    const [dp0] = solve(1);
    return Math.max(...dp0);
}
