// LeetCode 3594. Minimum Time to Transport All Individuals — Hard
// https://leetcode.com/problems/minimum-time-to-transport-all-individuals/
// Submission 2202865524 — Accepted, TypeScript
function minTime(n: number, k: number, m: number, time: number[], mul: number[]): number {
    // My thinking: the whole situation is which people are
    // already across, which stage we are in, and which side the
    // boat is on — that is the full state. From a state I either
    // send a group of up to k people across (the crossing takes
    // the slowest member's time times the stage multiplier) or
    // send one person back, and the stage advances by the whole
    // minutes of the trip, modulo m. Dijkstra over that state
    // space gives the cheapest way to get everyone across; if
    // the boat can only carry one person at a time and there are
    // two or more people, nobody can ever finish, so it is -1.
    const FULL = (1 << n) - 1;
    const INF = Infinity;
    type Key = string;
    const key = (mask: number, stage: number, boat: boolean) => `${mask},${stage},${boat ? 1 : 0}`;
    const dist = new Map<Key, number>();
    const start = key(0, 0, false);
    dist.set(start, 0);
    // a small binary heap of [d, mask, stage, boat]
    const pq: [number, number, number, boolean][] = [[0, 0, 0, false]];
    function push(item: [number, number, number, boolean]) {
        pq.push(item);
        let i = pq.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (pq[p][0] <= pq[i][0]) break;
            [pq[p], pq[i]] = [pq[i], pq[p]];
            i = p;
        }
    }
    function pop(): [number, number, number, boolean] {
        const top = pq[0];
        const last = pq.pop()!;
        if (pq.length) {
            pq[0] = last;
            let i = 0;
            for (;;) {
                const l = 2 * i + 1, r = l + 1;
                let s = i;
                if (l < pq.length && pq[l][0] < pq[s][0]) s = l;
                if (r < pq.length && pq[r][0] < pq[s][0]) s = r;
                if (s === i) break;
                [pq[s], pq[i]] = [pq[i], pq[s]];
                i = s;
            }
        }
        return top;
    }
    function combos<T>(arr: T[], r: number): T[][] {
        const out: T[][] = [];
        const cur: T[] = [];
        function rec(start: number) {
            if (cur.length === r) { out.push([...cur]); return; }
            for (let i = start; i < arr.length; i++) {
                cur.push(arr[i]);
                rec(i + 1);
                cur.pop();
            }
        }
        rec(0);
        return out;
    }
    while (pq.length) {
        const [d, mask, stage, boat] = pop();
        if (d > (dist.get(key(mask, stage, boat)) ?? INF) + 1e-9) continue;
        if (mask === FULL) return d;
        if (!boat) {
            const base: number[] = [];
            for (let i = 0; i < n; i++) if (!((mask >> i) & 1)) base.push(i);
            for (let r = 1; r <= Math.min(k, base.length); r++) {
                for (const combo of combos(base, r)) {
                    const mx = Math.max(...combo.map((i) => time[i]));
                    const cross = mx * mul[stage];
                    const ns = (stage + Math.floor(cross)) % m;
                    let nmask = mask;
                    for (const i of combo) nmask |= 1 << i;
                    const nd = d + cross;
                    const kk = key(nmask, ns, true);
                    if (nd < (dist.get(kk) ?? INF) - 1e-9) {
                        dist.set(kk, nd);
                        push([nd, nmask, ns, true]);
                    }
                }
            }
        } else {
            for (let r = 0; r < n; r++) {
                if (!((mask >> r) & 1)) continue;
                const ret = time[r] * mul[stage];
                const ns = (stage + Math.floor(ret)) % m;
                const nmask = mask & ~(1 << r);
                const nd = d + ret;
                const kk = key(nmask, ns, false);
                if (nd < (dist.get(kk) ?? INF) - 1e-9) {
                    dist.set(kk, nd);
                    push([nd, nmask, ns, false]);
                }
            }
        }
    }
    return -1;
}
