// LeetCode 3830. Longest Alternating Subarray After Removing At Most One Element — Hard
// https://leetcode.com/problems/longest-alternating-subarray-after-removing-at-most-one-element/
// Submission 2203201076 — Accepted, TypeScript
function longestAlternating(nums: number[]): number {
    // My thinking: write cmp[i] for the sign of nums[i+1] -
    // nums[i]. A subarray is alternating exactly when its
    // comparisons are nonzero and keep flipping sign.
    // left[i] is the longest alternating subarray ending at
    // i and right[i] the longest one starting at i: each
    // extends the previous run by one when the new
    // comparison flips the last one, restarts as a pair
    // when it does not (a single comparison is always
    // alternating), and collapses to 1 on an equal
    // neighbour. The no-deletion answer is max(left).
    // Deleting an interior element d makes d-1 and d+1
    // neighbours, with junction comparison j between them;
    // the two sides can join only when j is nonzero and
    // differs from the last comparison of the left run
    // (cmp[d-2], when that run has length at least 2) and
    // from the first comparison of the right run (cmp[d+1],
    // when that run has length at least 2). Either side
    // whose comparison agrees with j can only contribute
    // its single end element — any longer suffix or prefix
    // of that run ends (or starts) with the same
    // comparison, so it would clash with the junction too.
    // Deleting an end element never helps beyond the
    // no-deletion answer, since every subarray of the
    // shortened array is already a subarray of the whole
    // array.
    const n = nums.length;
    const cmp: number[] = new Array(n - 1);
    for (let i = 0; i < n - 1; i++) {
        cmp[i] = Math.sign(nums[i + 1] - nums[i]);
    }
    const left: number[] = new Array(n).fill(1);
    for (let i = 1; i < n; i++) {
        if (cmp[i - 1] === 0) left[i] = 1;
        else if (left[i - 1] === 1 || cmp[i - 1] !== cmp[i - 2]) left[i] = left[i - 1] + 1;
        else left[i] = 2;
    }
    const right: number[] = new Array(n).fill(1);
    for (let i = n - 2; i >= 0; i--) {
        if (cmp[i] === 0) right[i] = 1;
        else if (right[i + 1] === 1 || cmp[i] !== cmp[i + 1]) right[i] = right[i + 1] + 1;
        else right[i] = 2;
    }
    let ans = Math.max(...left);
    for (let d = 1; d <= n - 2; d++) {
        const j = Math.sign(nums[d + 1] - nums[d - 1]);
        if (j === 0) continue;
        const llen = left[d - 1] === 1 || cmp[d - 2] === -j ? left[d - 1] : 1;
        const rlen = right[d + 1] === 1 || cmp[d + 1] === -j ? right[d + 1] : 1;
        ans = Math.max(ans, llen + rlen);
    }
    return ans;
}
