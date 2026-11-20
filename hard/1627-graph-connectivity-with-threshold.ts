function areConnected(n: number, threshold: number, queries: number[][]): boolean[] {
    // My thinking: two numbers link when they share a
    // divisor bigger than the threshold — so join every
    // multiple of each big divisor and read the answers off.
    const parent = Array.from({ length: n + 1 }, (_, i) => i);
    function find(x: number): number {
        while (parent[x] !== x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }
    function union(x: number, y: number): void {
        const rx = find(x), ry = find(y);
        if (rx !== ry) parent[rx] = ry;
    }
    for (let d = threshold + 1; d <= n; d++) {
        for (let m = d * 2; m <= n; m += d) union(d, m);
    }
    return queries.map(([a, b]) => find(a) === find(b));
}
