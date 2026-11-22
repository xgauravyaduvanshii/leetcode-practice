// LeetCode 2030. Smallest K-Length Subsequence With Occurrences of a Letter — Hard
// https://leetcode.com/problems/smallest-k-length-subsequence-with-occurrences-of-a-letter/
// Submission 2201554640 — Accepted, JavaScript
//
// My thinking: I build the smallest answer with
// a stack, always dropping a bigger letter when
// a smaller one arrives — but only if enough
// letters and enough room are still left to
// finish the length and the count.

/**
 * @param {string} s
 * @param {number} k
 * @param {string} letter
 * @param {number} repetition
 * @return {string}
 */
function smallestSubsequence(s, k, letter, repetition) {
    const n = s.length;
    let remain = 0;
    for (const ch of s) if (ch === letter) ++remain;
    const stack = [];
    let have = 0;
    for (let i = 0; i < n; ++i) {
        const ch = s[i];
        while (stack.length > 0 && stack[stack.length - 1] > ch) {
            if (stack.length - 1 + (n - i) < k) break;
            if (stack[stack.length - 1] === letter && have - 1 + remain < repetition) break;
            if (stack[stack.length - 1] === letter) --have;
            stack.pop();
        }
        if (stack.length < k) {
            if (ch === letter) {
                stack.push(ch);
                ++have;
            } else {
                const need = repetition - have;
                if (need <= remain && need <= k - stack.length - 1) stack.push(ch);
            }
        }
        if (ch === letter) --remain;
    }
    return stack.join("");
}
