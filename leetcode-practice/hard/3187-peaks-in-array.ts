// LeetCode 3187. Peaks in Array — Hard
// https://leetcode.com/problems/peaks-in-array/
// Submission 2202070701 — Accepted, TypeScript
//
// My thinking: a peak can only change at
// the updated index and its two
// neighbours, so I keep all peaks in a
// Fenwick tree: point updates on at most
// three positions, and a range query
// counts the peaks strictly inside
// [l, r]. A range shorter than two holds
// no peak.

function countOfPeaks(nums: number[], queries: number[][]): number[] {
    const n = nums.length;
    const bit: number[] = new Array(n + 2).fill(0);
    const bitAdd = (i: number, delta: number): void => {
        for (let x = i + 1; x <= n + 1; x += x & -x) bit[x] += delta;
    };
    const bitSum = (i: number): number => {
        if (i < 0) return 0;
        let s = 0;
        for (let x = i + 1; x > 0; x -= x & -x) s += bit[x];
        return s;
    };
    const isPeak = (i: number): number => (i > 0 && i < n - 1 && nums[i] > nums[i - 1] && nums[i] > nums[i + 1] ? 1 : 0);
    const peak: number[] = new Array(n).fill(0);
    for (let i = 0; i < n; i++) {
        peak[i] = isPeak(i);
        if (peak[i]) bitAdd(i, 1);
    }
    const ans: number[] = [];
    for (const q of queries) {
        if (q[0] === 1) {
            const l = q[1], r = q[2];
            ans.push(r - l < 2 ? 0 : bitSum(r - 1) - bitSum(l));
        } else {
            const idx = q[1], val = q[2];
            nums[idx] = val;
            for (const i of [idx - 1, idx, idx + 1]) {
                if (i > 0 && i < n - 1) {
                    const nv = isPeak(i);
                    if (nv !== peak[i]) { bitAdd(i, nv - peak[i]); peak[i] = nv; }
                }
            }
        }
    }
    return ans;
};
