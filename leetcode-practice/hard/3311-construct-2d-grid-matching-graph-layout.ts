// 3311. Construct 2D Grid Matching Graph Layout (Hard)
// https://leetcode.com/problems/construct-2d-grid-matching-graph-layout/
// Submission 2202320084 -- Accepted, TypeScript
function constructGridLayout(n: number, edges: number[][]): number[][] {
    // My thinking: a grid's corners have degree 2, so I start from one. I
    // walk the top edge from the corner: at a degree-3 edge node the next
    // node along the edge is the neighbour that is NOT adjacent to the node
    // below the previous node, and the other neighbour is the node below.
    // The same walk down the left edge gives the first column. Then every
    // interior cell is the common neighbour of the cell above it and the
    // cell to its left, other than the diagonal cell. A graph whose degrees
    // are all at most 2 is a single row (or a 2x2 cycle, handled below).
    const adj: Set<number>[] = Array.from({ length: n }, () => new Set<number>());
    for (const [u, v] of edges) {
        adj[u].add(v);
        adj[v].add(u);
    }
    const deg = adj.map((s) => s.size);

    if (Math.max(...deg) <= 2) {
        const start = deg.findIndex((d) => d === 1);
        if (start === -1) {
            // A 2x2 grid: a 4-cycle. Lay it out as two rows of two.
            // Stop when the walk returns to the start node.
            const cycle: number[] = [0];
            let prev = -1;
            let cur = 0;
            for (;;) {
                const nxt = [...adj[cur]].filter((w) => w !== prev);
                if (nxt.length === 0 || nxt[0] === 0) break;
                prev = cur;
                cur = nxt[0];
                cycle.push(cur);
            }
            return [[cycle[0], cycle[1]], [cycle[3], cycle[2]]];
        }
        const row: number[] = [start];
        let prev = -1;
        let cur = start;
        for (;;) {
            const nxt = [...adj[cur]].filter((w) => w !== prev);
            if (nxt.length === 0) break;
            prev = cur;
            cur = nxt[0];
            row.push(cur);
        }
        return [row];
    }

    const corner = deg.findIndex((d) => d === 2);
    const nb = [...adj[corner]];

    function walkFirst(start: number, firstStep: number, other: number): [number[], Map<number, number>] {
        // Walk one side of the grid from the corner; returns the side as a
        // list and, for each node on it, the node just inside the grid.
        const line: number[] = [start, firstStep];
        const inside = new Map<number, number>([[start, other]]);
        let prev = start;
        let cur = firstStep;
        for (;;) {
            if (deg[cur] === 2) {
                inside.set(cur, [...adj[cur]].find((w) => w !== prev)!);
                break;
            }
            const cands = [...adj[cur]].filter((w) => w !== prev);
            // The inside neighbour is adjacent to the inside node of prev;
            // the other candidate continues along the side.
            const downNode = cands.find((w) => adj[inside.get(prev)!].has(w))!;
            const nextNode = cands.find((w) => w !== downNode)!;
            inside.set(cur, downNode);
            line.push(nextNode);
            prev = cur;
            cur = nextNode;
        }
        return [line, inside];
    }

    const [firstRow] = walkFirst(corner, nb[0], nb[1]);
    const [firstCol] = walkFirst(corner, nb[1], nb[0]);
    const rows = firstCol.length;
    const cols = firstRow.length;
    const grid: number[][] = Array.from({ length: rows }, () => Array(cols).fill(-1));
    firstRow.forEach((v, c) => { grid[0][c] = v; });
    firstCol.forEach((v, r) => { grid[r][0] = v; });
    for (let r = 1; r < rows; r++) {
        for (let c = 1; c < cols; c++) {
            const common = [...adj[grid[r - 1][c]]].filter((w) => adj[grid[r][c - 1]].has(w) && w !== grid[r - 1][c - 1]);
            grid[r][c] = common[0];
        }
    }
    return grid;
}
