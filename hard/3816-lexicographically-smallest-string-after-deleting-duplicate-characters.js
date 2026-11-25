// LeetCode 3816. Lexicographically Smallest String After Deleting Duplicate Characters — Hard
// https://leetcode.com/problems/lexicographically-smallest-string-after-deleting-duplicate-characters/
// Submission 2203193710 — Accepted, JavaScript
/**
 * @param {string} s
 * @return {string}
 */
var lexSmallestAfterDeletion = function(s) {
    // My thinking: deleting an occurrence is only allowed
    // while its letter still appears at least twice, so
    // every distinct letter must survive at least once,
    // and any subsequence keeping each distinct letter at
    // least once can be reached by deleting the rest one
    // by one. So the task is the lexicographically smallest
    // subsequence of s that contains every distinct letter
    // at least once. I build it left to right: at each
    // step I take the smallest letter that occurs at or
    // after the current position and still leaves every
    // not-yet-taken letter occurring after the chosen spot.
    // A letter is safe exactly when its position lies
    // before the last occurrence of every still-missing
    // letter except possibly its own, so I keep the
    // smallest and second smallest such last occurrences
    // and test each candidate against them in O(1); the
    // earliest occurrence of the chosen letter (found by
    // binary search) leaves the longest suffix, so the
    // choice is safe. Once every distinct letter is taken
    // I stop — appending anything more would only make
    // the string longer with the same prefix, hence
    // larger. A feasible candidate always exists: the
    // still-missing letter whose first occurrence from
    // here is earliest can always be taken next.
    const n = s.length;
    const positions = Array.from({ length: 26 }, () => []);
    const last = new Array(26).fill(-1);
    for (let i = 0; i < n; i++) {
        const c = s.charCodeAt(i) - 97;
        positions[c].push(i);
        last[c] = i;
    }
    const distinct = [];
    for (let c = 0; c < 26; c++) if (positions[c].length > 0) distinct.push(c);
    const missing = new Set(distinct);
    const taken = new Set();
    // Smallest and second smallest last occurrence among
    // the letters still missing; recomputed only when a
    // letter is taken, since the missing set only shrinks
    // then. (Last occurrences are distinct positions, so
    // the smallest one belongs to exactly one letter.)
    let m1 = Infinity, m2 = Infinity, argm1 = -1;
    const refresh = () => {
        m1 = Infinity; m2 = Infinity; argm1 = -1;
        for (const d of missing) {
            if (last[d] < m1) { m2 = m1; m1 = last[d]; argm1 = d; }
            else if (last[d] < m2) { m2 = last[d]; }
        }
    };
    refresh();
    let pos = 0;
    let ans = "";
    while (taken.size < distinct.length) {
        for (let c = 0; c < 26; c++) {
            const arr = positions[c];
            let lo = 0, hi = arr.length;
            while (lo < hi) {
                const mid = (lo + hi) >> 1;
                if (arr[mid] < pos) lo = mid + 1;
                else hi = mid;
            }
            if (lo === arr.length) continue;
            const p = arr[lo];
            const threshold = (c === argm1) ? m2 : m1;
            if (p < threshold) {
                ans += String.fromCharCode(c + 97);
                taken.add(c);
                pos = p + 1;
                if (missing.has(c)) {
                    missing.delete(c);
                    refresh();
                }
                break;
            }
        }
    }
    return ans;
};
