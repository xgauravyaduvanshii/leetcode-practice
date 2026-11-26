// LeetCode 3897. Maximum Value of Concatenated Binary Segments — Hard
// https://leetcode.com/problems/maximum-value-of-concatenated-binary-segments/
// Submission 2203364641 — Accepted, TypeScript
function maxValue(nums1: number[], nums0: number[]): number {
    // My thinking: the concatenated string always has the
    // same total length, so the largest binary value is
    // the lexicographically largest string. Compare two
    // segments A = 1^a 0^b and B = 1^c 0^d. If both have
    // zeros, AB beats BA exactly when a > c, or a == c
    // and b < d: the first differing position is where
    // the segment with more ones still shows a 1 while
    // the other already shows a 0, and with equal ones
    // the segment with fewer zeros reaches its ones
    // again first. A segment with no zeros at all always
    // goes before any segment with zeros, whatever their
    // ones counts: AB = 1^a 1^c 0^d against
    // BA = 1^c 0^d 1^a, and the first position where they
    // differ has a 1 in AB and the 0 of B's tail in BA.
    // So sort by (has zeros, -ones, zeros): zero-zero
    // segments first, then more ones first, then fewer
    // zeros first. The value is then built bit by bit,
    // modulo 1e9 + 7.
    const MOD = 1_000_000_007;
    const segs = nums1.map((ones, i): [number, number] => [ones, nums0[i]]);
    segs.sort((x, y) => (x[1] !== 0 ? 1 : 0) - (y[1] !== 0 ? 1 : 0) || y[0] - x[0] || x[1] - y[1]);
    let ans = 0;
    for (const [ones, zeros] of segs) {
        for (let i = 0; i < ones; i++) ans = (ans * 2 + 1) % MOD;
        for (let i = 0; i < zeros; i++) ans = (ans * 2) % MOD;
    }
    return ans;
}
