// LeetCode 4037. Maximum Valid Split Positions II — Hard
// https://leetcode.com/problems/maximum-valid-split-positions-ii/
// Submission 2203527956 — Accepted, TypeScript
function maxValidSplits(nums: number[]): number {
    // My thinking: for one fixed array, a split i is
    // valid exactly when the prefix gcd up to i equals
    // the suffix gcd from i + 1, so the score is the
    // count of i with pre[i] === suf[i + 1], where pre
    // and suf are the prefix and suffix gcd arrays.
    // Scoring every possible deletion in O(n) each is
    // too slow for n = 10^5. But a prefix gcd only
    // changes O(log M) times: each change at least
    // halves the value, since every new gcd divides
    // the previous one. If neither the prefix gcd nor
    // the suffix gcd changes at index i, deleting
    // nums[i] leaves every other prefix and suffix gcd
    // untouched and only merges the two neighbouring
    // split positions into one, so the score cannot
    // grow. Only the O(log M) indices where a gcd
    // actually changes (plus index 0, and the mirrored
    // end from the reversed pass) are worth deleting
    // and rescoring; the answer is the best of those
    // and of deleting nothing.
    const n = nums.length;

    function calc(arr: number[]): number {
        const m = arr.length;
        const pre: number[] = new Array(m);
        const suf: number[] = new Array(m);
        pre[0] = arr[0];
        for (let i = 1; i < m; ++i) {
            pre[i] = gcd(pre[i - 1], arr[i]);
        }
        suf[m - 1] = arr[m - 1];
        for (let i = m - 2; i >= 0; --i) {
            suf[i] = gcd(suf[i + 1], arr[i]);
        }
        let ans = 0;
        for (let i = 0; i + 1 < m; ++i) {
            if (pre[i] === suf[i + 1]) {
                ++ans;
            }
        }
        return ans;
    }

    function mark(arr: number[]): boolean[] {
        const pos: boolean[] = new Array(n).fill(false);
        pos[0] = true;
        let g = arr[0];
        for (let i = 1; i < n; ++i) {
            const ng = gcd(g, arr[i]);
            pos[i] = ng !== g;
            g = ng;
        }
        return pos;
    }

    function gcd(a: number, b: number): number {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    }

    const pos1 = mark(nums);
    const pos2 = mark([...nums].reverse());
    let ans = calc(nums);
    for (let i = 0; i < n; ++i) {
        if (pos1[i] || pos2[n - 1 - i]) {
            const arr = nums.slice(0, i).concat(nums.slice(i + 1));
            ans = Math.max(ans, calc(arr));
        }
    }
    return ans;
}
