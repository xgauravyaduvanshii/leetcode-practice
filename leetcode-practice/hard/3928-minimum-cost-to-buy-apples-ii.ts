// LeetCode 3928. Minimum Cost to Buy Apples II — Hard
// https://leetcode.com/problems/minimum-cost-to-buy-apples-ii/
// Submission 2203427090 — Accepted, TypeScript
function minCost(n: number, prices: number[], roads: number[][]): number[] {
    // My thinking: for shop i the cheapest plan is either
    // buying locally, or travelling empty to some shop j,
    // buying there, and carrying the apples back. The
    // forward and return legs may differ, and the graph
    // is undirected, so the empty leg costs the shortest
    // path from i to j in the plain-cost metric and the
    // return leg costs the shortest path from j to i in
    // the cost-times-tax metric. That makes the answer
    // min over j of distCost[i][j] + distTax[i][j] +
    // prices[j], where the two distance tables are
    // all-pairs shortest paths in the two metrics. Each
    // row comes from a heap Dijkstra run from one source
    // (n up to 1000, so a quadratic Dijkstra would be
    // too slow); the j = i term is just prices[i], so
    // the local purchase is covered automatically.
    type Edge = [number, number];
    const adjCost: Edge[][] = Array.from({ length: n }, () => []);
    const adjTax: Edge[][] = Array.from({ length: n }, () => []);
    for (const [u, v, c, t] of roads) {
        adjCost[u].push([v, c]);
        adjCost[v].push([u, c]);
        adjTax[u].push([v, c * t]);
        adjTax[v].push([u, c * t]);
    }
    // Binary heap of [distance, node] pairs.
    const heapPush = (h: [number, number][], item: [number, number]): void => {
        h.push(item);
        let i = h.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (h[p][0] <= h[i][0]) break;
            [h[p], h[i]] = [h[i], h[p]];
            i = p;
        }
    };
    const heapPop = (h: [number, number][]): [number, number] => {
        const top = h[0];
        const last = h.pop()!;
        if (h.length > 0) {
            h[0] = last;
            let i = 0;
            for (;;) {
                const l = 2 * i + 1;
                const r = 2 * i + 2;
                let s = i;
                if (l < h.length && h[l][0] < h[s][0]) s = l;
                if (r < h.length && h[r][0] < h[s][0]) s = r;
                if (s === i) break;
                [h[s], h[i]] = [h[i], h[s]];
                i = s;
            }
        }
        return top;
    };
    const dijkstra = (src: number, adj: Edge[][]): number[] => {
        const dist: number[] = new Array(n).fill(Infinity);
        dist[src] = 0;
        const h: [number, number][] = [[0, src]];
        while (h.length > 0) {
            const [d, u] = heapPop(h);
            if (d !== dist[u]) continue;
            for (const [v, w] of adj[u]) {
                const nd = d + w;
                if (nd < dist[v]) {
                    dist[v] = nd;
                    heapPush(h, [nd, v]);
                }
            }
        }
        return dist;
    };
    const distCost: number[][] = [];
    const distTax: number[][] = [];
    for (let s = 0; s < n; s++) {
        distCost.push(dijkstra(s, adjCost));
        distTax.push(dijkstra(s, adjTax));
    }
    const ans: number[] = new Array(n);
    for (let i = 0; i < n; i++) {
        let best = prices[i];
        for (let j = 0; j < n; j++) {
            const a = distCost[i][j];
            const b = distTax[i][j];
            if (a !== Infinity && b !== Infinity) {
                const cand = a + b + prices[j];
                if (cand < best) best = cand;
            }
        }
        ans[i] = best;
    }
    return ans;
}
