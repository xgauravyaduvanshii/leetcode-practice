// LeetCode 4095. Count Frequency Staircase Subarrays II — Hard
// https://leetcode.com/problems/count-frequency-staircase-subarrays-ii/
// Submission 2203727645 — Accepted, JavaScript

// My thinking: a subarray is a frequency staircase
// when the distinct values, in the order they first
// appear, have frequencies exactly 1, 2, 3, ..., k.
// A staircase with k distinct values is at least
// 1 + 2 + ... + k = k(k+1)/2 long, so k never exceeds
// the largest K with K(K+1)/2 <= n. First, a sliding
// window over distinct values gives limit[l], the
// last index of the all-distinct stretch starting at
// l. If that stretch is longer than K, then every
// subarray starting at l already needs more than K
// distinct values before it can close, so only the
// singleton [l, l] can be a staircase — count it and
// move on (this is the fast path that keeps the
// whole scan fast). Otherwise extend r from l,
// tracking for each distinct value how many times it
// has appeared (freq) and how many it must reach
// (req = its order of first appearance), plus a bad
// counter of values that have not yet reached their
// required count. A new value is fine only while the
// distinct count stays <= K and the minimal staircase
// length still fits in the array; a repeat that
// overshoots its required count ends the scan, since
// adding more of it can never fix the excess. Each
// time bad hits 0 the frequencies are exactly
// 1, 2, ..., distinct, so the subarray nums[l..r]
// is a staircase and we count it.
var countStaircase = function(nums) {
    const n = nums.length;
    let K = 1;
    while ((K + 1) * (K + 2) / 2 <= n) K++;
    let maxV = 0;
    for (const x of nums) if (x > maxV) maxV = x;
    const size = maxV + 1;
    const limit = new Int32Array(n);
    const inWindow = new Int32Array(size);
    let r = 0;
    for (let l = 0; l < n; l++) {
        if (r < l) r = l;
        while (r < n && inWindow[nums[r]] === 0) {
            inWindow[nums[r]] = 1;
            r++;
        }
        limit[l] = r - 1;
        inWindow[nums[l]] = 0;
    }
    const freq = new Int32Array(size);
    const req = new Int32Array(size);
    const seen = new Int32Array(size);
    let ans = 0;
    for (let l = 0; l < n; l++) {
        if (limit[l] - l + 1 > K) {
            ans++;
            continue;
        }
        let distinct = 0;
        let bad = 0;
        const mark = l + 1;
        for (let rr = l; rr < n; rr++) {
            const v = nums[rr];
            if (seen[v] !== mark) {
                seen[v] = mark;
                distinct++;
                if (distinct > K) break;
                if (l + Math.floor(distinct * (distinct + 1) / 2) > n) break;
                freq[v] = 1;
                req[v] = distinct;
                if (distinct > 1) bad++;
            } else {
                const c = freq[v] + 1;
                freq[v] = c;
                if (c === req[v]) bad--;
                else if (c > req[v]) break;
            }
            if (bad === 0) ans++;
        }
    }
    return ans;
};
