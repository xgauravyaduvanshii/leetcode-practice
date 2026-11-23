// LeetCode 2290. Minimum Obstacle Removal to Reach Corner — Hard
// https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/
// Submission 2201662161 — Accepted, TypeScript
//
// My thinking: stepping on an empty cell
// costs nothing and an obstacle costs one,
// so I walk the grid with a 0-1 queue and
// the first time I reach the corner I have
// paid the fewest obstacles possible.

function minimumObstacles(grid: number[][]): number {
    const m = grid.length, n = grid[0].length;
    const dist: number[][] = Array.from({ length: m }, () => Array(n).fill(-1));
    dist[0][0] = 0;
    const dq: [number, number][] = [[0, 0]];
    const dirs: [number, number][] = [[1, 0], [-1, 0], [0, 1], [0, -1]];
    while (dq.length > 0) {
        const [x, y] = dq.shift()!;
        const d = dist[x][y];
        if (x === m - 1 && y === n - 1) return d;
        for (const [dx, dy] of dirs) {
            const nx = x + dx, ny = y + dy;
            if (nx >= 0 && nx < m && ny >= 0 && ny < n && dist[nx][ny] === -1) {
                const cost = d + grid[nx][ny];
                dist[nx][ny] = cost;
                if (grid[nx][ny] === 0) dq.unshift([nx, ny]);
                else dq.push([nx, ny]);
            }
        }
    }
    return dist[m - 1][n - 1];
}
