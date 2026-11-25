// LeetCode 3640. Trionic Array II — Hard
// https://leetcode.com/problems/trionic-array-ii/
// Submission 2202926873 — Accepted, JavaScript
var maxTrionicSum = function(nums) {
    // My thinking: a trionic subarray is an increasing run up
    // to a peak p, a decreasing run down to a valley q, then an
    // increasing run again. For the outer runs I take the best
    // suffix/prefix of the run: because the run is strictly
    // increasing, extending it only helps while the new element
    // is positive, so the best increasing subarray ending at p
    // (or starting at q) is the run trimmed at the first
    // non-positive element. For the middle run, fixing q, the
    // value of a peak p is L[p] plus the stretch p+1..q, which
    // is L[p] - prefix[p+1] plus a term that only depends on q,
    // so I sweep q left to right keeping the best peak of the
    // current decreasing run in a sliding-window deque.
    const n = nums.length;
    const prefix = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) prefix[i + 1] = prefix[i] + nums[i];

    // best1[i]: best sum of an increasing subarray ending at i
    // (length >= 1). L[i]: same with length >= 2, else null.
    const best1 = new Array(n).fill(0);
    const L = new Array(n).fill(null);
    for (let i = 0; i < n; i++) {
        if (i > 0 && nums[i - 1] < nums[i]) {
            best1[i] = nums[i] + Math.max(0, best1[i - 1]);
            L[i] = nums[i] + best1[i - 1];
        } else {
            best1[i] = nums[i];
        }
    }

    // best1r[i]: best sum of an increasing subarray starting
    // at i (length >= 1). R[i]: same with length >= 2.
    const best1r = new Array(n).fill(0);
    const R = new Array(n).fill(null);
    for (let i = n - 1; i >= 0; i--) {
        if (i + 1 < n && nums[i] < nums[i + 1]) {
            best1r[i] = nums[i] + Math.max(0, best1r[i + 1]);
            R[i] = nums[i] + best1r[i + 1];
        } else {
            best1r[i] = nums[i];
        }
    }

    let ans = null;
    // Deque of [p, L[p] - prefix[p+1]] with decreasing values,
    // p ranging over the current decreasing run ending at q.
    const dq = [];
    let runStart = 0;
    for (let q = 0; q < n; q++) {
        if (q > 0 && nums[q - 1] > nums[q]) {
            // run continues, runStart unchanged
        } else {
            runStart = q;
        }
        const p = q - 1;
        if (p >= 0 && L[p] !== null) {
            const val = L[p] - prefix[p + 1];
            while (dq.length && dq[dq.length - 1][1] <= val) dq.pop();
            dq.push([p, val]);
        }
        while (dq.length && dq[0][0] < runStart) dq.shift();
        if (dq.length && R[q] !== null) {
            const total = dq[0][1] + prefix[q + 1] + R[q] - nums[q];
            ans = ans === null ? total : Math.max(ans, total);
        }
    }
    return ans;
};
