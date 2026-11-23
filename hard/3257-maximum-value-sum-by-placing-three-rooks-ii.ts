// LeetCode 3257. Maximum Value Sum by Placing Three Rooks II — Hard
// https://leetcode.com/problems/maximum-value-sum-by-placing-three-rooks-ii/
// Submission 2202153909 — Accepted, TypeScript
//
// My thinking: this is an assignment problem —
// pick 3 rows and 3 distinct columns to maximise
// the sum. A row's optimal cell must be among its
// top 3, since only two other rooks can block its
// columns. I build a min-cost max-flow network
// (source to rows, rows to their top-3 columns,
// columns to sink) and push 3 units of flow; the
// negated cost is the answer.

function maximumValueSum(board: number[][]): number {
    const m = board.length;
    const n = board[0].length;
    const N = 2 + m + n;
    const S = 0;
    const T = N - 1;
    type Edge = { to: number; rev: number; cap: number; cost: number };
    const graph: Edge[][] = Array.from({ length: N }, () => []);
    const addEdge = (fr: number, to: number, cap: number, cost: number) => {
        graph[fr].push({ to, rev: graph[to].length, cap, cost });
        graph[to].push({ to: fr, rev: graph[fr].length - 1, cap: 0, cost: -cost });
    };
    for (let i = 0; i < m; i++) addEdge(S, 1 + i, 1, 0);
    for (let j = 0; j < n; j++) addEdge(1 + m + j, T, 1, 0);
    for (let i = 0; i < m; i++) {
        const idx = Array.from({ length: n }, (_, j) => j).sort((a, b) => board[i][b] - board[i][a]).slice(0, 3);
        for (const j of idx) addEdge(1 + i, 1 + m + j, 1, -board[i][j]);
    }
    const INF = 1e18;
    let res = 0;
    let flow = 0;
    while (flow < 3) {
        const dist = new Array<number>(N).fill(INF);
        const inq = new Array<boolean>(N).fill(false);
        const prevv = new Array<number>(N).fill(-1);
        const preve = new Array<number>(N).fill(-1);
        dist[S] = 0;
        const q: number[] = [S];
        inq[S] = true;
        let head = 0;
        while (head < q.length) {
            const v = q[head++];
            inq[v] = false;
            for (let ei = 0; ei < graph[v].length; ei++) {
                const e = graph[v][ei];
                if (e.cap > 0 && dist[e.to] > dist[v] + e.cost) {
                    dist[e.to] = dist[v] + e.cost;
                    prevv[e.to] = v;
                    preve[e.to] = ei;
                    if (!inq[e.to]) { q.push(e.to); inq[e.to] = true; }
                }
            }
        }
        if (dist[T] === INF) break;
        let v = T;
        while (v !== S) {
            const e = graph[prevv[v]][preve[v]];
            e.cap -= 1;
            graph[v][e.rev].cap += 1;
            v = prevv[v];
        }
        res += dist[T];
        flow++;
    }
    return -res;
};
