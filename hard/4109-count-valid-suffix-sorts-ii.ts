// LeetCode 4109. Count Valid Suffix Sorts II — Hard
// https://leetcode.com/problems/count-valid-suffix-sorts-ii/
// Submission 2203737902 — Accepted, TypeScript
function countSuffix(nums: number[], target: number[]): number[] {
    // My thinking: sorting a suffix nums[i..] in
    // non-increasing order only rearranges the
    // multiset, so a window target[k..k+n-1] can
    // match only when it holds exactly the same
    // values as nums. Slide a frequency-difference
    // count over target and keep a "bad" tally of
    // values whose counts disagree; bad == 0 means
    // the window is a multiset match. For such a
    // window, a suffix sort starting at i keeps the
    // prefix nums[0..i-1] untouched and sorts the
    // rest, so the result must agree with target
    // on that prefix: i can be at most p, the
    // matching-prefix length, found for every k by
    // one Z-function run on nums + [0] + target.
    // The sorted suffix is non-increasing, so the
    // window must be non-increasing from i on:
    // i must lie after the last adjacent increase
    // in the window (tracked by lastInc), giving
    // a lower bound q. The valid i are then
    // q..min(p, n-1), counted per window.
    const n = nums.length;
    const m = target.length;
    const s = nums.concat([0], target);
    const N = s.length;
    const z = new Array<number>(N).fill(0);
    let l = 0, r = 0;
    for (let i = 1; i < N; i++) {
        if (i <= r) z[i] = Math.min(r - i + 1, z[i - l]);
        while (i + z[i] < N && s[z[i]] === s[i + z[i]]) z[i]++;
        if (i + z[i] - 1 > r) { l = i; r = i + z[i] - 1; }
    }
    const lastInc = new Array<number>(m).fill(-1);
    let cur = -1;
    for (let j = 0; j < m - 1; j++) {
        if (target[j] < target[j + 1]) cur = j;
        lastInc[j] = cur;
    }
    lastInc[m - 1] = cur;
    const diff = new Array<number>(100001).fill(0);
    for (const v of nums) diff[v]++;
    for (let j = 0; j < n; j++) diff[target[j]]--;
    let bad = 0;
    for (const d of diff) if (d !== 0) bad++;
    const ans = new Array<number>(m - n + 1).fill(0);
    for (let k = 0; k <= m - n; k++) {
        if (k > 0) {
            let v = target[k - 1];
            if (diff[v] === 0) bad++;
            diff[v]++;
            if (diff[v] === 0) bad--;
            v = target[k + n - 1];
            if (diff[v] === 0) bad++;
            diff[v]--;
            if (diff[v] === 0) bad--;
        }
        if (bad === 0) {
            let p = z[n + 1 + k];
            if (p > n) p = n;
            const j = n >= 2 ? lastInc[k + n - 2] : -1;
            const q = j < k ? 0 : j + 1 - k;
            const hi = p < n - 1 ? p : n - 1;
            const cnt = hi - q + 1;
            if (cnt > 0) ans[k] = cnt;
        }
    }
    return ans;
}
