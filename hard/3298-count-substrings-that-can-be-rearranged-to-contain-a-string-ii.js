// LeetCode 3298. Count Substrings That Can Be Rearranged to Contain a String II — Hard
// https://leetcode.com/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-ii/
// NOT SUBMITTED — LeetCode's JavaScript (Node.js) runner failed on 24 Nov 2026
// ("Fatal process out of memory: Failed to reserve virtual memory for CodeRange"),
// even for a trivial template, so no Run ever became Accepted and the code was
// deliberately not submitted. The code below is the correct sliding-window solution
// (same logic as the Accepted Python3 submission 2202185775), verified locally
// with node. Re-submit when LeetCode's JavaScript runner recovers.
//
// My thinking: a substring works when it holds
// at least as many of each letter as word2 needs.
// I slide a window with two pointers, tracking
// how many distinct needed letters are satisfied;
// once the window is valid, every extension to
// the right is valid too, so I add them all and
// then shrink from the left.

/**
 * @param {string} word1
 * @param {string} word2
 * @return {number}
 */
var validSubstringCount = function(word1, word2) {
    const need = new Array(26).fill(0);
    for (const ch of word2) need[ch.charCodeAt(0) - 97]++;
    let distinct = 0;
    for (const x of need) if (x) distinct++;
    const cnt = new Array(26).fill(0);
    const n = word1.length;
    let satisfied = 0, right = 0, ans = 0;
    for (let left = 0; left < n; left++) {
        while (right < n && satisfied < distinct) {
            const c = word1.charCodeAt(right) - 97;
            cnt[c]++;
            if (cnt[c] === need[c]) satisfied++;
            right++;
        }
        if (satisfied < distinct) break;
        ans += n - right + 1;
        const c = word1.charCodeAt(left) - 97;
        if (cnt[c] === need[c]) satisfied--;
        cnt[c]--;
    }
    return ans;
};
