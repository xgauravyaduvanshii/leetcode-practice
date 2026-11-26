// LeetCode 5. Longest Palindromic Substring — Medium
// https://leetcode.com/problems/longest-palindromic-substring/
// Submission 2203754633 — Accepted, JavaScript

// My thinking:
// A palindrome reads the same forwards and backwards, so every palindrome
// has a center. I try every position as a center and expand outwards as
// long as the characters on both sides match, keeping the longest one found.
// Each center needs two expansions: odd length (center is one character)
// and even length (center is between two characters). If the whole string
// is already a palindrome I return it straight away — that also avoids the
// slow case of a long all-same-character input, where expanding would be
// quadratic anyway but with a trivial answer.

/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
    if (s === s.split('').reverse().join('')) return s;
    const n = s.length;
    let start = 0, maxLen = 1;
    for (let center = 0; center < n; center++) {
        // Odd-length palindromes: center is one character.
        let l = center, r = center;
        while (l >= 0 && r < n && s[l] === s[r]) {
            if (r - l + 1 > maxLen) { start = l; maxLen = r - l + 1; }
            l--; r++;
        }
        // Even-length palindromes: center is between two characters.
        l = center; r = center + 1;
        while (l >= 0 && r < n && s[l] === s[r]) {
            if (r - l + 1 > maxLen) { start = l; maxLen = r - l + 1; }
            l--; r++;
        }
    }
    return s.substring(start, start + maxLen);
};
