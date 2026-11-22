// LeetCode 1960. Maximum Product of the Length of Two Palindromic Substrings — Hard
// https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-substrings/
// Submission 2201273466 — Accepted, TypeScript
//
// My thinking: I grow every palindrome from its
// centre and note the longest one ending and
// starting at each spot — then the best split is
// the best left length times the best right length.

function maxProduct(s: string): number {
    const n = s.length;
    const endMax = new Array(n).fill(0);
    const startMax = new Array(n).fill(0);
    for (let c = 0; c < n; c++) {
        let l = c, r = c;
        while (l >= 0 && r < n && s[l] === s[r]) {
            endMax[r] = Math.max(endMax[r], r - l + 1);
            startMax[l] = Math.max(startMax[l], r - l + 1);
            l--;
            r++;
        }
    }
    for (let c = 0; c < n - 1; c++) {
        let l = c, r = c + 1;
        while (l >= 0 && r < n && s[l] === s[r]) {
            endMax[r] = Math.max(endMax[r], r - l + 1);
            startMax[l] = Math.max(startMax[l], r - l + 1);
            l--;
            r++;
        }
    }
    const pre = new Array(n).fill(0);
    let best = 0;
    for (let i = 0; i < n; i++) {
        best = Math.max(best, endMax[i]);
        pre[i] = best;
    }
    const suf = new Array(n).fill(0);
    best = 0;
    for (let i = n - 1; i >= 0; i--) {
        best = Math.max(best, startMax[i]);
        suf[i] = best;
    }
    let ans = 0;
    for (let i = 0; i < n - 1; i++) ans = Math.max(ans, pre[i] * suf[i + 1]);
    return ans;
}
