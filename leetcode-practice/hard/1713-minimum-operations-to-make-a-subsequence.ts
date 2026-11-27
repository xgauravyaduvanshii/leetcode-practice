// LeetCode 1713. Minimum Operations to Make a Subsequence — Hard
// https://leetcode.com/problems/minimum-operations-to-make-a-subsequence/
// Submission 2201109062 — Accepted, TypeScript
//
// My thinking: I keep only the target values that also
// appear in the array, turn them into positions, and
// the longest increasing run of those positions is the
// longest subsequence I already have — everything else
// has to be inserted.

function minOperations(target: number[], arr: number[]): number {
    const pos = new Map<number, number>();
    target.forEach((v, i) => pos.set(v, i));
    const tails: number[] = [];
    for (const v of arr) {
        if (!pos.has(v)) continue;
        const p = pos.get(v)!;
        let left = 0, right = tails.length;
        while (left < right) {
            const mid = (left + right) >> 1;
            if (tails[mid] < p) left = mid + 1;
            else right = mid;
        }
        if (left === tails.length) tails.push(p);
        else tails[left] = p;
    }
    return target.length - tails.length;
}
