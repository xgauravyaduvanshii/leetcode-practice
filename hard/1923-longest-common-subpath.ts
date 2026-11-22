// LeetCode 1923. Longest Common Subpath — Hard
// https://leetcode.com/problems/longest-common-subpath/
// Submission 2201235792 — Accepted, TypeScript
//
// My thinking: I binary search the length and
// check it with a rolling hash — for each path I
// collect the hashes of all its windows of that
// length, and the length works when some hash
// survives in every path.

function longestCommonSubpath(n: number, paths: number[][]): number {
    const MOD1 = 1000000007, MOD2 = 1000000009, BASE = 100007;
    function feasible(L: number): boolean {
        if (L === 0) return true;
        let common: Set<string> | null = null;
        for (const path of paths) {
            if (path.length < L) return false;
            let h1 = 0, h2 = 0, p1 = 1, p2 = 1;
            for (let i = 0; i < L; i++) {
                h1 = (h1 * BASE + path[i] + 1) % MOD1;
                h2 = (h2 * BASE + path[i] + 1) % MOD2;
                if (i < L - 1) {
                    p1 = p1 * BASE % MOD1;
                    p2 = p2 * BASE % MOD2;
                }
            }
            const s = new Set<string>();
            s.add(h1 + "," + h2);
            for (let i = L; i < path.length; i++) {
                h1 = (((h1 - (path[i - L] + 1) * p1) % MOD1 + MOD1) % MOD1 * BASE + path[i] + 1) % MOD1;
                h2 = (((h2 - (path[i - L] + 1) * p2) % MOD2 + MOD2) % MOD2 * BASE + path[i] + 1) % MOD2;
                s.add(h1 + "," + h2);
            }
            if (common === null) {
                common = s;
            } else {
                const next = new Set<string>();
                for (const h of s) if (common.has(h)) next.add(h);
                common = next;
            }
            if (common.size === 0) return false;
        }
        return common !== null && common.size > 0;
    }
    let lo = 0, hi = Math.min(...paths.map(p => p.length));
    while (lo < hi) {
        const mid = Math.floor((lo + hi + 1) / 2);
        if (feasible(mid)) lo = mid;
        else hi = mid - 1;
    }
    return lo;
}
