// LeetCode 1771. Maximize Palindrome Length From Subsequences — Hard
// https://leetcode.com/problems/maximize-palindrome-length-from-subsequences/
// Submission 2201157519 — Accepted, JavaScript
//
// My thinking: the finished palindrome starts with
// a letter from the first word and ends with the
// same letter from the second word, so I try every
// such matching pair and fill the middle with the
// longest palindromic subsequence between them.

function longestPalindrome(word1, word2) {
    const s = word1 + word2;
    const n = s.length;
    const m = word1.length;
    const dp = Array.from({ length: n }, () => new Array(n).fill(0));
    for (let i = 0; i < n; i++) dp[i][i] = 1;
    for (let len = 2; len <= n; len++) {
        for (let i = 0; i + len - 1 < n; i++) {
            const j = i + len - 1;
            if (s[i] === s[j]) {
                dp[i][j] = len > 2 ? dp[i + 1][j - 1] + 2 : 2;
            } else {
                dp[i][j] = Math.max(dp[i + 1][j], dp[i][j - 1]);
            }
        }
    }
    let ans = 0;
    for (let i = 0; i < m; i++) {
        for (let j = m; j < n; j++) {
            if (s[i] === s[j]) {
                const inner = j - i > 1 ? dp[i + 1][j - 1] : 0;
                ans = Math.max(ans, 2 + inner);
            }
        }
    }
    return ans;
}
