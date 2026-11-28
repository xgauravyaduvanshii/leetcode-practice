// LeetCode 2734. Lexicographically Smallest String After Substring Operation — Medium
// https://leetcode.com/problems/lexicographically-smallest-string-after-substring-operation/
// Submission 2205221028 — Accepted, JavaScript
//
// My thinking: same idea as the Python version — decrease the
// first contiguous run of non-'a' letters; if the string is
// all 'a's, turn the last letter into a 'z'.
/**
 * @param {string} s
 * @return {string}
 */
var smallestString = function(s) {
    const chars = s.split('');
    const n = chars.length;
    let i = 0;
    while (i < n && chars[i] === 'a') i++;
    if (i === n) {
        chars[n - 1] = 'z';
    } else {
        while (i < n && chars[i] !== 'a') {
            chars[i] = String.fromCharCode(chars[i].charCodeAt(0) - 1);
            i++;
        }
    }
    return chars.join('');
};
