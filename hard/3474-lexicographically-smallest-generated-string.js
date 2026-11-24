// LeetCode 3474. Lexicographically Smallest Generated String — Hard
// https://leetcode.com/problems/lexicographically-smallest-generated-string/
// Submission 2202665565 — Accepted 742/742, JavaScript
//
// My thinking: every 'T' in str1 pins a whole copy of str2 into the word,
// so I write those in first and give up if two of them disagree on a
// position. The remaining free positions default to 'a'. Then I walk the
// 'F' windows left to right: if a window still spells str2, I change its
// rightmost free position to the smallest letter different from str2's
// letter there ('b' when str2 has 'a', else 'a'). Changing the rightmost
// free spot keeps the word as small as possible, and once a window is made
// different it stays different, because the changed position is fixed from
// then on. If a window that spells str2 has no free position left, there
// is no valid word at all.

/**
 * @param {string} str1
 * @param {string} str2
 * @return {string}
 */
var generateString = function(str1, str2) {
    const n = str1.length, m = str2.length;
    const word = new Array(n + m - 1).fill(null);
    for (let i = 0; i < n; i++) {
        if (str1[i] === 'T') {
            for (let j = 0; j < m; j++) {
                if (word[i + j] === null) word[i + j] = str2[j];
                else if (word[i + j] !== str2[j]) return "";
            }
        }
    }
    for (let i = 0; i < n; i++) {
        if (str1[i] === 'F') {
            let cur = "";
            for (let j = 0; j < m; j++) cur += word[i + j] === null ? 'a' : word[i + j];
            if (cur === str2) {
                let fixed = false;
                for (let j = m - 1; j >= 0; j--) {
                    if (word[i + j] === null) {
                        word[i + j] = str2[j] === 'a' ? 'b' : 'a';
                        fixed = true;
                        break;
                    }
                }
                if (!fixed) return "";
            }
        }
    }
    return word.map(c => c === null ? 'a' : c).join('');
};
