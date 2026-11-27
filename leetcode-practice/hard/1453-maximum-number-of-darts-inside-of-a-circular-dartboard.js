/**
 * @param {number[][]} darts
 * @param {number} r
 * @return {number}
 */
var numPoints = function(darts, r) {
    // My thinking: the best circle can always be slid
    // until two darts sit on its edge — so try every
    // circle through each pair of darts, and every circle
    // centred on a dart, and count what each one holds.
    const n = darts.length;
    if (n === 1) return 1;
    let best = 1;
    for (let i = 0; i < n; i++) {
        const [xi, yi] = darts[i];
        let count = 0;
        for (const [x, y] of darts) {
            if ((x - xi) ** 2 + (y - yi) ** 2 <= r * r + 1e-9) count++;
        }
        best = Math.max(best, count);
    }
    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            const [x1, y1] = darts[i];
            const [x2, y2] = darts[j];
            const dx = x2 - x1, dy = y2 - y1;
            const d = Math.hypot(dx, dy);
            if (d > 2 * r + 1e-9 || d === 0) continue;
            const mx = (x1 + x2) / 2, my = (y1 + y2) / 2;
            const h = Math.sqrt(Math.max(0, r * r - (d / 2) ** 2));
            const ux = -dy / d, uy = dx / d;
            for (const sign of [1, -1]) {
                const cx = mx + sign * h * ux, cy = my + sign * h * uy;
                let count = 0;
                for (const [x, y] of darts) {
                    if ((x - cx) ** 2 + (y - cy) ** 2 <= r * r + 1e-9) count++;
                }
                best = Math.max(best, count);
            }
        }
    }
    return best;
};
