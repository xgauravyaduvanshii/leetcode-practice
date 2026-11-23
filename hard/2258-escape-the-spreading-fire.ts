// LeetCode 2258. Escape the Spreading Fire — Hard
// https://leetcode.com/problems/escape-the-spreading-fire/
// Submission 2201640952 — Accepted, TypeScript
//
// My thinking: I first time when the fire
// reaches every cell, then I binary-search
// the longest I can wait — a wait works
// when I can still outrun the fire to the
// safehouse, arriving there no later than
// the flames do.

function maximumMinutes(grid: number[][]): number {
    const m = grid.length, n = grid[0].length;
    const INF = Number.POSITIVE_INFINITY;
    const fire: number[][] = Array.from({ length: m }, () => Array(n).fill(INF));
    const q: [number, number][] = [];
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] === 1) {
                fire[i][j] = 0;
                q.push([i, j]);
            }
        }
    }
    const dirs: [number, number][] = [[1, 0], [-1, 0], [0, 1], [0, -1]];
    for (let head = 0; head < q.length; head++) {
        const [x, y] = q[head];
        for (const [dx, dy] of dirs) {
            const nx = x + dx, ny = y + dy;
            if (nx >= 0 && nx < m && ny >= 0 && ny < n && grid[nx][ny] !== 2 && fire[nx][ny] === INF) {
                fire[nx][ny] = fire[x][y] + 1;
                q.push([nx, ny]);
            }
        }
    }
    const can = (wait: number): boolean => {
        if (wait >= fire[0][0]) return false;
        const dist: number[][] = Array.from({ length: m }, () => Array(n).fill(-1));
        dist[0][0] = wait;
        const qq: [number, number][] = [[0, 0]];
        for (let head = 0; head < qq.length; head++) {
            const [x, y] = qq[head];
            const t = dist[x][y];
            if (x === m - 1 && y === n - 1) return true;
            for (const [dx, dy] of dirs) {
                const nx = x + dx, ny = y + dy;
                if (nx >= 0 && nx < m && ny >= 0 && ny < n && grid[nx][ny] !== 2 && dist[nx][ny] === -1) {
                    const nt = t + 1;
                    if (nx === m - 1 && ny === n - 1) {
                        if (nt <= fire[nx][ny]) {
                            dist[nx][ny] = nt;
                            qq.push([nx, ny]);
                        }
                    } else if (nt < fire[nx][ny]) {
                        dist[nx][ny] = nt;
                        qq.push([nx, ny]);
                    }
                }
            }
        }
        return false;
    };
    if (!can(0)) return -1;
    let lo = 0, hi = 1e9;
    while (lo < hi) {
        const mid = Math.floor((lo + hi + 1) / 2);
        if (can(mid)) lo = mid;
        else hi = mid - 1;
    }
    return lo;
}
