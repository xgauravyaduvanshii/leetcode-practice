// LeetCode 3505. Minimum Operations to Make Elements Within K Subarrays Equal — Hard
// https://leetcode.com/problems/minimum-operations-to-make-elements-within-k-subarrays-equal/
// Submission 2202758450 — Accepted, TypeScript
function minOperations(nums: number[], x: number, k: number): number {
    // My thinking: the cheapest way to make one window of length x
    // all equal is to move every element to the window's median, so
    // I slide a window across the array keeping its median and the
    // cost of levelling it (two heaps, lower half and upper half,
    // with lazy deletion for the element sliding out). Then a
    // knapsack-style DP picks k non-overlapping windows: dp[i][j]
    // is the cheapest cost using j windows inside the first i
    // elements, either skipping position i or ending a window there.
    const n = nums.length;
    const lo: number[] = []; // max-heap of original values, lower half
    const hi: number[] = []; // min-heap of original values, upper half
    let sumLo = 0;
    let sumHi = 0;
    let szLo = 0;
    let szHi = 0;
    const rem = new Map<number, number>();
    function heapPush(h: number[], v: number, isMax: boolean): void {
        h.push(v);
        let i = h.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (isMax ? h[p] >= h[i] : h[p] <= h[i]) break;
            [h[p], h[i]] = [h[i], h[p]];
            i = p;
        }
    }
    function heapPop(h: number[], isMax: boolean): number {
        const top = h[0];
        const last = h.pop()!;
        if (h.length > 0) {
            h[0] = last;
            let i = 0;
            for (;;) {
                const l = 2 * i + 1;
                const r = 2 * i + 2;
                let best = i;
                if (l < h.length && (isMax ? h[l] > h[best] : h[l] < h[best])) best = l;
                if (r < h.length && (isMax ? h[r] > h[best] : h[r] < h[best])) best = r;
                if (best === i) break;
                [h[i], h[best]] = [h[best], h[i]];
                i = best;
            }
        }
        return top;
    }
    function prune(h: number[], isMax: boolean): void {
        while (h.length > 0) {
            const v = h[0];
            const c = rem.get(v) ?? 0;
            if (c > 0) {
                rem.set(v, c - 1);
                heapPop(h, isMax);
            } else break;
        }
    }
    function rebalance(): void {
        prune(lo, true);
        prune(hi, false);
        while (szLo > szHi + 1) {
            const v = heapPop(lo, true);
            sumLo -= v;
            szLo--;
            heapPush(hi, v, false);
            sumHi += v;
            szHi++;
            prune(lo, true);
        }
        while (szLo < szHi) {
            const v = heapPop(hi, false);
            sumHi -= v;
            szHi--;
            heapPush(lo, v, true);
            sumLo += v;
            szLo++;
            prune(hi, false);
        }
    }
    function add(v: number): void {
        prune(lo, true);
        if (lo.length === 0 || v <= lo[0]) {
            heapPush(lo, v, true);
            sumLo += v;
            szLo++;
        } else {
            heapPush(hi, v, false);
            sumHi += v;
            szHi++;
        }
        rebalance();
    }
    function remove(v: number): void {
        prune(lo, true);
        prune(hi, false);
        rem.set(v, (rem.get(v) ?? 0) + 1);
        if (lo.length > 0 && v <= lo[0]) {
            sumLo -= v;
            szLo--;
        } else {
            sumHi -= v;
            szHi--;
        }
        prune(lo, true);
        prune(hi, false);
        rebalance();
    }
    function windowCost(): number {
        prune(lo, true);
        prune(hi, false);
        const med = lo[0];
        return med * szLo - sumLo + sumHi - med * szHi;
    }
    const cost: number[] = new Array(n).fill(0);
    for (let i = 0; i < n; i++) {
        add(nums[i]);
        if (i >= x) remove(nums[i - x]);
        if (i >= x - 1) cost[i] = windowCost();
    }
    const INF = Number.POSITIVE_INFINITY;
    let dpPrev: number[] = new Array(n + 1).fill(0);
    for (let jj = 0; jj < k; jj++) {
        const dpCur: number[] = new Array(n + 1).fill(INF);
        for (let i = 1; i <= n; i++) {
            dpCur[i] = dpCur[i - 1];
            if (i >= x && dpPrev[i - x] < INF) {
                dpCur[i] = Math.min(dpCur[i], dpPrev[i - x] + cost[i - 1]);
            }
        }
        dpPrev = dpCur;
    }
    return dpPrev[n];
}
