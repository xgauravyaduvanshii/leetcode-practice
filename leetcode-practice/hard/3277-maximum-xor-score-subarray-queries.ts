// LeetCode 3277. Maximum XOR Score Subarray Queries — Hard
// https://leetcode.com/problems/maximum-xor-score-subarray-queries/
// Submission 2202175509 — Accepted, TypeScript
//
// My thinking: the XOR of a subarray is the XOR
// of two adjacent subarrays of the level below,
// so I build the XOR triangle row by row, and
// alongside it the best XOR seen for every
// (start, length). A query [l, r] is then just
// best[length r-l][l].

function maximumSubarrayXor(nums: number[], queries: number[][]): number[] {
    const n = nums.length;
    let cur: number[] = nums.slice();
    let best: number[] = nums.slice();
    const bestByLen: number[][] = [best];
    for (let len = 2; len <= n; len++) {
        const prevBest = best;
        const nextCur: number[] = new Array(cur.length - 1);
        for (let i = 0; i < nextCur.length; i++) {
            nextCur[i] = cur[i] ^ cur[i + 1];
        }
        cur = nextCur;
        const nextBest: number[] = new Array(cur.length);
        for (let i = 0; i < cur.length; i++) {
            nextBest[i] = Math.max(cur[i], prevBest[i], prevBest[i + 1]);
        }
        best = nextBest;
        bestByLen.push(best);
    }
    return queries.map(([l, r]) => bestByLen[r - l][l]);
};
