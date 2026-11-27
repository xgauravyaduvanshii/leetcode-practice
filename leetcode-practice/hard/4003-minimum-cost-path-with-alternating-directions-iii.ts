// LeetCode 4003. Minimum Cost Path with Alternating Directions III — Hard
// https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-iii/
// Submission 2203505304 — Accepted, TypeScript
function minCost(m: number, n: number, penalty: number[][]): number {
    // My thinking: the only thing that matters besides
    // the cell is the parity of the next action — odd
    // actions move right or down for free, even actions
    // move left or up for free, and every action flips
    // the parity. So Dijkstra over states (i, j, p):
    // from a state you may wait, paying penalty[i][j],
    // or step to a neighbour, paying its entrance cost
    // (i+1)*(j+1) plus penalty[i][j] when the step
    // breaks the parity rule. All costs are
    // non-negative, the start state costs the entrance
    // of (0, 0), and the first time the target is
    // popped from the heap its cost is minimal. The
    // total stays far below 2^53, so a JS number is
    // exact.
    const INF = Infinity;
    const dist: number[][][] = [];
    for (let i = 0; i < m; i++) {
        dist.push([]);
        for (let j = 0; j < n; j++) dist[i].push([INF, INF]);
    }
    dist[0][0][0] = 1;
    // Binary min-heap of [cost, i, j, parity].
    const heap: number[][] = [[1, 0, 0, 0]];
    function push(item: number[]): void {
        heap.push(item);
        let c = heap.length - 1;
        while (c > 0) {
            const p = (c - 1) >> 1;
            if (heap[p][0] <= heap[c][0]) break;
            const t = heap[p]; heap[p] = heap[c]; heap[c] = t;
            c = p;
        }
    }
    function pop(): number[] {
        const top = heap[0];
        const last = heap.pop() as number[];
        if (heap.length > 0) {
            heap[0] = last;
            let c = 0;
            for (;;) {
                const l = 2 * c + 1, r = 2 * c + 2;
                let s = c;
                if (l < heap.length && heap[l][0] < heap[s][0]) s = l;
                if (r < heap.length && heap[r][0] < heap[s][0]) s = r;
                if (s === c) break;
                const t = heap[s]; heap[s] = heap[c]; heap[c] = t;
                c = s;
            }
        }
        return top;
    }
    const dirs: number[][] = [[0, 1], [1, 0], [0, -1], [-1, 0]];
    while (heap.length > 0) {
        const cur = pop();
        const d = cur[0], i = cur[1], j = cur[2], p = cur[3];
        if (d !== dist[i][j][p]) continue;
        if (i === m - 1 && j === n - 1) return d;
        const nd = d + penalty[i][j];
        if (nd < dist[i][j][1 - p]) {
            dist[i][j][1 - p] = nd;
            push([nd, i, j, 1 - p]);
        }
        for (let k = 0; k < 4; k++) {
            const ni = i + dirs[k][0], nj = j + dirs[k][1];
            if (ni < 0 || ni >= m || nj < 0 || nj >= n) continue;
            const free = (p === 0 && (dirs[k][0] > 0 || dirs[k][1] > 0)) ||
                (p === 1 && (dirs[k][0] < 0 || dirs[k][1] < 0));
            const cost = d + (ni + 1) * (nj + 1) + (free ? 0 : penalty[i][j]);
            if (cost < dist[ni][nj][1 - p]) {
                dist[ni][nj][1 - p] = cost;
                push([cost, ni, nj, 1 - p]);
            }
        }
    }
    return Math.min(dist[m - 1][n - 1][0], dist[m - 1][n - 1][1]);
}
