// LeetCode 3272. Find the Count of Good Integers — Hard
// https://leetcode.com/problems/find-the-count-of-good-integers/
// Submission 2202171646 — Accepted, JavaScript
//
// My thinking: a "good" integer's digits can be
// rearranged into a palindrome divisible by k.
// I build every palindrome of length n from its
// first half, keep the ones divisible by k, and
// group them by their digit-count signature —
// palindromes with the same signature share the
// same rearrangement count. For each signature I
// count all permutations minus the ones with a
// leading zero, using factorials.

/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var countGoodIntegers = function(n, k) {
    const fact = [1];
    for (let i = 1; i <= 10; i++) fact[i] = fact[i - 1] * i;
    const halfLen = Math.floor((n + 1) / 2);
    const start = 10 ** (halfLen - 1);
    const end = 10 ** halfLen;
    const seen = new Set();
    for (let half = start; half < end; half++) {
        const s = String(half);
        let pal;
        if (n % 2 === 0) {
            pal = s + s.split('').reverse().join('');
        } else {
            pal = s + s.slice(0, -1).split('').reverse().join('');
        }
        if (Number(pal) % k !== 0) continue;
        const cnt = new Array(10).fill(0);
        for (const ch of pal) cnt[ch.charCodeAt(0) - 48]++;
        seen.add(cnt.join(','));
    }
    let total = 0;
    for (const key of seen) {
        const cnt = key.split(',').map(Number);
        let perms = fact[n];
        for (const c of cnt) perms /= fact[c];
        if (cnt[0] > 0) {
            let lead = fact[n - 1] / fact[cnt[0] - 1];
            for (let d = 1; d < 10; d++) lead /= fact[cnt[d]];
            perms -= lead;
        }
        total += perms;
    }
    return total;
};
