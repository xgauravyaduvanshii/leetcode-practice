function maxStudents(seats: string[][]): number {
    // My thinking: each row is a bitmask of who sits where —
    // no neighbours in the row, no broken seats, and no one
    // diagonally above — then carry the best count forward
    // row by row.
    const rows = seats.length, cols = seats[0].length;
    const valid: number[][] = [];
    for (let r = 0; r < rows; r++) {
        const rowMasks: number[] = [];
        for (let mask = 0; mask < (1 << cols); mask++) {
            let ok = true;
            for (let c = 0; c < cols; c++) {
                if ((mask >> c) & 1) {
                    if (seats[r][c] === "#") { ok = false; break; }
                    if (c > 0 && ((mask >> (c - 1)) & 1)) { ok = false; break; }
                }
            }
            if (ok) rowMasks.push(mask);
        }
        valid.push(rowMasks);
    }
    let dp = new Map<number, number>([[0, 0]]);
    for (let r = 0; r < rows; r++) {
        const next = new Map<number, number>();
        for (const mask of valid[r]) {
            const count = mask.toString(2).split("1").length - 1;
            for (const [prevMask, prevVal] of dp) {
                if ((mask & (prevMask << 1)) === 0 && (mask & (prevMask >> 1)) === 0) {
                    next.set(mask, Math.max(next.get(mask) ?? 0, prevVal + count));
                }
            }
        }
        dp = next;
    }
    return Math.max(...dp.values());
}
