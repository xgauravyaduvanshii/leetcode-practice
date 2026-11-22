// LeetCode 2045. Second Minimum Time to Reach Destination — Hard
// https://leetcode.com/problems/second-minimum-time-to-reach-destination/
// Submission 2201558640 — Accepted, TypeScript
//
// My thinking: a red light only makes me wait
// for the next green, so I walk the graph keeping
// the two quickest distinct arrivals at every
// stop — the second one at the end is the answer.

function secondMinimum(n: number, edges: number[][], time: number, change: number): number {
    const graph: number[][] = Array.from({ length: n + 1 }, () => []);
    for (const [u, v] of edges) {
        graph[u].push(v);
        graph[v].push(u);
    }
    const dist: number[][] = Array.from({ length: n + 1 }, () => []);
    // Simple min-heap of [time, node].
    const heap: [number, number][] = [[0, 1]];
    const push = (item: [number, number]) => {
        heap.push(item);
        let i = heap.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (heap[p][0] <= heap[i][0]) break;
            [heap[p], heap[i]] = [heap[i], heap[p]];
            i = p;
        }
    };
    const pop = (): [number, number] => {
        const top = heap[0];
        const last = heap.pop()!;
        if (heap.length > 0) {
            heap[0] = last;
            let i = 0;
            for (;;) {
                const l = 2 * i + 1;
                const r = 2 * i + 2;
                let smallest = i;
                if (l < heap.length && heap[l][0] < heap[smallest][0]) smallest = l;
                if (r < heap.length && heap[r][0] < heap[smallest][0]) smallest = r;
                if (smallest === i) break;
                [heap[smallest], heap[i]] = [heap[i], heap[smallest]];
                i = smallest;
            }
        }
        return top;
    };
    while (heap.length > 0) {
        const [t, u] = pop();
        if (dist[u].length === 2 && t >= dist[u][1]) continue;
        if (dist[u].includes(t)) continue;
        dist[u].push(t);
        dist[u].sort((a, b) => a - b);
        if (dist[u].length > 2) dist[u] = dist[u].slice(0, 2);
        if (u === n && dist[n].length === 2) return dist[n][1];
        const depart = Math.floor(t / change) % 2 === 1 ? (Math.floor(t / change) + 1) * change : t;
        for (const v of graph[u]) push([depart + time, v]);
    }
    return -1;
}
