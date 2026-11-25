// LeetCode 3677. Count Binary Palindromic Numbers — Hard
// https://leetcode.com/problems/count-binary-palindromic-numbers/
// Submission 2203035526 — Accepted, JavaScript
//
// My thinking: a binary palindrome is fixed by its first
// half — mirror the first half to get the whole number.
// I count 0 on its own, then every palindrome shorter
// than n: for a length L the first bit is 1 and the
// remaining ceil(L/2) - 1 free bits give 2 ** ((L - 1) // 2)
// palindromes. For n's own length I take the first half
// of n, count the smaller halves, and add one more only
// if the palindrome built from n's own half is still <= n.
/**
 * @param {number} n
 * @return {number}
 */
var countBinaryPalindromes = function(n) {
    if (n === 0) return 1;
    const s = n.toString(2);
    const length = s.length;
    let count = 1; // the number 0
    for (let shorter = 1; shorter < length; shorter++) {
        count += 2 ** Math.floor((shorter - 1) / 2);
    }
    const halfLen = Math.ceil(length / 2);
    const half = parseInt(s.slice(0, halfLen), 2);
    const base = 2 ** (halfLen - 1);
    const prefix = s.slice(0, halfLen);
    const mirrored = prefix + (length % 2 === 0 ? [...prefix].reverse().join("") : [...prefix.slice(0, -1)].reverse().join(""));
    count += half - base;
    if (parseInt(mirrored, 2) <= n) count += 1;
    return count;
};
