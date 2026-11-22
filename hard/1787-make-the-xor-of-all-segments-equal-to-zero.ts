// LeetCode 1787. Make the XOR of All Segments Equal to Zero — Hard
// https://leetcode.com/problems/make-the-xor-of-all-segments-equal-to-zero/
// Submission 2201165014 — Accepted, TypeScript
//
// My thinking: positions that are k apart must all
// end up equal, so I group them and, group by
// group, keep the cheapest cost for every xor so
// far — keeping the group's most common value is
// cheapest, changing the whole group costs the
// group size no matter what value I pick.

function minChanges(nums: number[], k: number): number {
    const groups: Map<number, number>[] = Array.from({ length: k }, () => new Map());
    for (let i = 0; i < nums.length; i++) {
        const g = groups[i % k];
        g.set(nums[i], (g.get(nums[i]) ?? 0) + 1);
    }
    const INF = 1e9;
    let dp = new Array(1024).fill(INF);
    dp[0] = 0;
    for (let i = 0; i < k; i++) {
        const cnt = groups[i];
        let size = 0;
        for (const f of cnt.values()) size += f;
        const best = Math.min(...dp);
        const ndp = new Array(1024).fill(best + size);
        for (let x = 0; x < 1024; x++) {
            if (dp[x] === INF) continue;
            for (const [v, f] of cnt) {
                const nx = x ^ v;
                ndp[nx] = Math.min(ndp[nx], dp[x] + size - f);
            }
        }
        dp = ndp;
    }
    return dp[0];
}
