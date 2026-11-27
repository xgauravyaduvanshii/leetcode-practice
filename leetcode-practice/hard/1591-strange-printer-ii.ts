function isPrintable(targetGrid: number[][]): boolean {
    // My thinking: the last colour printed sits clean on
    // its rectangle — so peel off any colour whose whole
    // rectangle is already gone, and repeat.
    const m = targetGrid.length, n = targetGrid[0].length;
    const rect = new Map<number, [number, number, number, number]>();
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            const c = targetGrid[i][j];
            const r = rect.get(c);
            if (r === undefined) rect.set(c, [i, i, j, j]);
            else {
                r[0] = Math.min(r[0], i);
                r[1] = Math.max(r[1], i);
                r[2] = Math.min(r[2], j);
                r[3] = Math.max(r[3], j);
            }
        }
    }
    const removed = new Set<number>();
    let changed = true;
    while (changed) {
        changed = false;
        for (const [c, r] of rect) {
            if (removed.has(c)) continue;
            let ok = true;
            outer: for (let i = r[0]; i <= r[1]; i++) {
                for (let j = r[2]; j <= r[3]; j++) {
                    const v = targetGrid[i][j];
                    if (v !== c && !removed.has(v)) { ok = false; break outer; }
                }
            }
            if (ok) { removed.add(c); changed = true; }
        }
    }
    return removed.size === rect.size;
}
